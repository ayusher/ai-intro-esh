import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import argparse
import pickle
# add imports as needed


def train(train_path, test_path, model_path):
    # read in training data
    # train sklearn.SVC model
    # read in testing data
    # evaluate model, print out classification_report and confusion_matrix
    # save model to model_path in a pickle file
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-path', help='path to read training data')
    parser.add_argument('--test-path', help='path to read test data')
    parser.add_argument('--model-path', help='path to save the model')

    args = parser.parse_args()

    train(args.train_path, args.test_path, args.model_path)
