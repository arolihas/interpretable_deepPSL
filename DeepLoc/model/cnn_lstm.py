"""Defines the neural network, losss function and metrics"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self, params):
        super(Net, self).__init__()

        #hyperparameters
        self.conv_out = 10
        # the embedding takes as input the vocab_size and the embedding_dim
        self.embedding = nn.Embedding(params.vocab_size, params.embedding_dim)

        #Conv layer
        self.conv3 = nn.Conv1d(
            in_channels=params.embedding_dim, 
            out_channels=self.conv_out,
            kernel_size=3, 
            padding=1, 
            stride=1)
        self.conv5 = nn.Conv1d(
            in_channels=params.embedding_dim, 
            out_channels=self.conv_out,
            kernel_size=5, 
            padding=2, 
            stride=1)
        self.relu = nn.ReLU()
        
        # the LSTM takes as input the size of its input (embedding_dim), its hidden size
        # for more details on how to use it, check out the documentation
        self.lstm = nn.LSTM(
            params.embedding_dim,
            params.lstm_hidden_dim,
            num_layers=params.n_layers, 
            bidirectional=True,
            dropout=params.dropout)
        self.dropout = nn.Dropout(params.dropout)

        # the fully connected layer transforms the output to give the final output layer
        self.fc = nn.Linear(params.lstm_hidden_dim*2, params.number_of_classes)
        self.attention_type = params.attention_type
        if self.attention_type == "average":
            # do stuff for average attention_type
            pass
        else:
            self.w_omega = nn.Linear(params.lstm_hidden_dim * params.n_layers, self.attention_size, bias=False)
            self.u_omega = nn.Linear(self.attention_size, 1, bias=False)
        
    def forward(self, s):

        embedded = self.embedding(s)            # dim: batch_size x seq_len x embedding_dim
        embedded = embedded.permute(0, 2, 1) # dim: batch_size, embedding_dim, seq_len
        
        conv_3 = self.relu(self.conv3(embedded)) # dim: batch_size, embedding_dim, seq_len
        conv_5 = self.relu(self.conv5(embedded))
        concat = torch.cat((conv_3, conv_5), dim=1)
        # run the LSTM along the sentences of length seq_len
        embedded = concat.permute(2, 0, 1)  # dim: seq_len, batch_size, embedding_dim
        output, (hidden_state, cell_state)  = self.lstm(embedded) 

        hidden = self.dropout(torch.cat((hidden_state[-2], hidden_state[-1]), dim=1))
        #hidden = [batch size, lstm_hidden_dim * num directions]

        return self.fc(hidden) # dim: batch_size x num_tags


def loss_fn(outputs, labels):
    return F.cross_entropy(outputs, labels)
    
    
def accuracy(outputs, labels):
    # reshape labels to give a flat vector of length batch_size*seq_len
    labels = labels.ravel()

    # np.argmax gives us the class predicted for each token by the model
    outputs = np.argmax(outputs, axis=1)

    # compare outputs with labels and divide by number of tokens (excluding PADding tokens)
    return np.sum(outputs==labels)/float(len(labels))


# maintain all metrics required in this dictionary- these are used in the training and evaluation loops
metrics = {
    'accuracy': accuracy,
    # could add more metrics such as accuracy for each token type
}