"""Peform hyperparemeters search"""

import argparse
import os
from subprocess import check_call
import sys

import utils


PYTHON = sys.executable
parser = argparse.ArgumentParser()
parser.add_argument('--parent_dir', default='experiments/learning_rate',
                    help='Directory containing params.json')
parser.add_argument('--data_dir', default='data/small', help="Directory containing the dataset")


def launch_training_job(parent_dir, data_dir, job_name, params):
    """Launch training of the model with a set of hyperparameters in parent_dir/job_name

    Args:
        model_dir: (string) directory containing config, weights and log
        data_dir: (string) directory containing the dataset
        params: (dict) containing hyperparameters
    """
    # Create a new folder in parent_dir with unique_name "job_name"
    model_dir = os.path.join(parent_dir, job_name)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Write parameters in json file
    json_path = os.path.join(model_dir, 'params.json')
    params.save(json_path)

    # Launch training with this config
    cmd = "{python} train.py --model_dir={model_dir} --data_dir {data_dir}".format(python=PYTHON, model_dir=model_dir,
                                                                                   data_dir=data_dir)
    print(cmd)
    check_call(cmd, shell=True)


if __name__ == "__main__":
    # Load the "reference" parameters from parent_dir json file
    args = parser.parse_args()
    json_path = os.path.join(args.parent_dir, 'params.json')
    assert os.path.isfile(json_path), "No json configuration file found at {}".format(json_path)
    params = utils.Params(json_path)

    # Perform hypersearch over one parameter
    # learning_rates = [1e-4, 1e-3, 1e-2]
        # for learning_rate in learning_rates:
        #     # Modify the relevant parameter in params
        #     params.learning_rate = learning_rate

        #     # Launch job (name has to be unique)
        #     job_name = "learning_rate_{}".format(learning_rate)
        #     launch_training_job(args.parent_dir, args.data_dir, job_name, params)

    # learning_rates = [1e-4, 1e-3, 1e-2, 0.1]
    learning_rates = [1e-3, 1e-2, 0.1]
    attention_weights = [32, 64, 128, 512, 1024, 2048]
    dropouts = [0.0, 0.2, 0.5]
    # attention_weights = [512, 1024]
    for lr in learning_rates:
        for attn_size in attention_weights:
            for d in dropouts:
                if attn_size in [512]: params.batch_size = 50
                elif attn_size in [1024, 2048]: params.batch_size = 25
                else: params.batch_size = 100
                # if lr == 1e-3 and attn_size in [32, 64, 128, 512, 1024]: continue
                if lr == 1e-3: continue
                if lr == 1e-2: continue
                if lr == 0.1 and attn_size in [32] and d in [0.0]: continue
                params.dropout = d
                params.attention_size = attn_size
                params.learning_rate = lr
                job_name = "attn_size_{}-lr_{}-drop_{}".format(attn_size, lr, d)
                launch_training_job(args.parent_dir, args.data_dir, job_name, params)
