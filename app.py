import argparse
import pandas as pd
import numpy as np
import sklearn

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # training data import
    parser.add_argument('--training', default='training_data.csv',
    help='input training data file name')
    # predict data export
    parser.add_argument('--output', default='submission.csv',
    help='output file name')
    print("No problem ")

    args = parser.parse_args()

    trainingData = pd.read_csv(args.training)

    print(trainingData)