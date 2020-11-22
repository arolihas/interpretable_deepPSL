"""Defines the neural network, losss function and metrics"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self, params):
        super(Net, self).__init__()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # the embedding takes as input the vocab_size and the embedding_dim
        self.embedding = nn.Embedding(params.vocab_size, params.embedding_dim)

        self.attention_size = params.attention_size
        self.lstm_hidden_dim = params.lstm_hidden_dim
        self.n_layers = params.n_layers
        self.directions = 2 if params.bidirectional == 1 else 1
        self.bidirectional = True if params.bidirectional == 1 else False
        # the LSTM takes as input the size of its input (embedding_dim), its hidden size
        # for more details on how to use it, check out the documentation
        self.lstm = nn.LSTM(params.embedding_dim, params.lstm_hidden_dim,\
                    num_layers=params.n_layers, bidirectional=True,\
                    dropout=params.dropout)
        self.dropout = nn.Dropout(params.dropout)

        # the fully connected layer transforms the output to give the final output layer
        self.fc = nn.Linear(params.lstm_hidden_dim*2, params.number_of_classes)
        self.use_attention = bool(params.attn)
        # Parameters for attention layer (from Hao's implementation)
        self.attention_type = params.attention_type
        if self.attention_type == "average":
            # do stuff for average attention_type
            pass
        else:
            self.w_omega = nn.Linear(params.lstm_hidden_dim * params.n_layers, self.attention_size, bias=False)
            self.u_omega = nn.Linear(self.attention_size, 1, bias=False)
            # self.w_omega = Variable(torch.zeros(params.lstm_hidden_dim * params.n_layers, self.attention_size).to(self.device), requires_grad=True)
            # self.u_omega = Variable(torch.zeros(self.attention_size).to(self.device), requires_grad=True)
        
    def attention_net(self, lstm_output, random=False, permute=False):
        sequence_length = lstm_output.size()[0]
        batch_size = lstm_output.size()[1]
        if self.attention_type != "average":
            output_reshape = torch.Tensor.reshape(lstm_output, [-1, self.lstm_hidden_dim*self.n_layers])
            # attn_tanh = torch.tanh(torch.mm(output_reshape, self.w_omega))
            # attn_hidden_layer = torch.mm(attn_tanh, torch.Tensor.reshape(self.u_omega, [-1, 1]))
            if random:
                # print("Random!")
                attn_hidden_layer = torch.rand(output_reshape.shape[0], 1)
            else:
                # print("Non Random")
                attn_tanh = torch.tanh(self.w_omega(output_reshape))
                attn_hidden_layer = self.u_omega(attn_tanh)
                # print(attn_hidden_layer)
                if permute:
                    # print("Permute!")
                    attn_hidden_layer = attn_hidden_layer.squeeze()
                    attn_hidden_layer = attn_hidden_layer[torch.randperm(attn_hidden_layer.shape[0])]
                    attn_hidden_layer = attn_hidden_layer.unsqueeze(1)
                # print(attn_hidden_layer)

            # print(attn_hidden_layer.shape)
            # exit()

            exps = torch.Tensor.reshape(torch.exp(attn_hidden_layer), [-1, sequence_length])
            alphas = exps / torch.Tensor.reshape(torch.sum(exps, 1), [-1, 1])
            #print(alphas.size()) = (batch_size, squence_length)

            alphas_reshape = torch.Tensor.reshape(alphas, [-1,sequence_length, 1])
            # print("REGULAR ATTENTION!")
            #print(alphas_reshape.size()) = (batch_size, squence_length, 1)
        else:
            alphas_reshape = torch.ones(batch_size, sequence_length, 1).to(self.device)
        state = lstm_output.permute(1, 0, 2)
        #print(state.size()) = (batch_size, squence_length, hidden_size*layer_size)

        attn_output = torch.sum(state * alphas_reshape, 1)
        #print(attn_output.size()) = (batch_size, hidden_size*layer_size)
        return attn_output, alphas_reshape


    def forward(self, s, random=False, permute=False):

        embedded = self.embedding(s)            # dim: batch_size x seq_len x embedding_dim
        embedded = embedded.permute(1, 0, 2)  # dim: seq_len, batch_size, embedding_dim

        # run the LSTM along the sentences of length seq_len
        output, (hidden_state, cell_state)  = self.lstm(embedded) 
        #output dim: seq_len, batch_size, num_directions*hidden_size
        # #hidden_state dim: num_layers*num_directions, batch_size, hidden_size
        #-----------------using attention layer---------------------
        if self.use_attention:
            attn_output, attn_weights = self.attention_net(output, random=random, permute=permute)
            hidden = self.dropout(attn_output)
        #----------------without attention---------------------
        else:
            hidden = self.dropout(torch.cat((hidden_state[-2], hidden_state[-1]), dim=1))
        # #hidden = [batch size, lstm_hidden_dim * num directions]


        return self.fc(hidden) # dim: batch_size x num_tags


def loss_fn(outputs, labels):
    return F.cross_entropy(outputs, labels)
    
from sklearn.metrics import f1_score, precision_score, recall_score, classification_report

def getpred(outputs):
    outputs = np.argmax(outputs, axis=1)
    return outputs
 
def accuracy(outputs, labels):
    # reshape labels to give a flat vector of length batch_size*seq_len
    labels = labels.ravel()

    # np.argmax gives us the class predicted for each token by the model
    outputs = np.argmax(outputs, axis=1)

    # compare outputs with labels and divide by number of tokens (excluding PADding tokens)
    return np.sum(outputs==labels)/float(len(labels))

def f1_micro(outputs, labels):
    labels = labels.ravel()
    outputs = getpred(outputs)
    return f1_score(labels, outputs, average='micro')

def f1_macro(outputs, labels):
    labels = labels.ravel()
    outputs = getpred(outputs)
    return f1_score(labels, outputs, average='macro')

def precision(outputs, labels):
    labels = labels.ravel()
    outputs = getpred(outputs)

    return precision_score(labels, outputs, average='micro')

def recall(outputs, labels):
    labels = labels.ravel()
    outputs = getpred(outputs)

    return recall_score(labels, outputs, average='micro')

import pprint
def report(outputs, labels):
    labels = labels.ravel()
    outputs = getpred(outputs)
    # TODO: add `target=` argument with actual classnames
    rep = classification_report(labels, outputs, output_dict=True)
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(rep) # pretty print?
    # print(rep)
    # exit()
    return rep


# maintain all metrics required in this dictionary- these are used in the training and evaluation loops
metrics = {
    'accuracy': accuracy,
    # could add more metrics such as accuracy for each token type
    'f1_micro' : f1_micro,
    'f1_macro' : f1_macro,
    'precision' : precision,
    'recall' : recall,
    # 'report' : report
}