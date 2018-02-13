''' Logistic Regression '''

import sys

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


def train(X_data, y_data):
  '''
  '''
  # Instantiate Logistic regression object and train with input data
  logreg = LogisticRegression()
  logreg.fit(X_data, y_data)

  return logreg


def test(X_data, y_data, model):
  '''
  '''
  accuracy = model.score(X_data, y_data)
  return accuracy


def plot(X, y, model):
  '''
  '''
  # Plot the data
  clr_list = ['blue' if y_val else 'red' for y_val in y]
  plt.scatter(X[:, 0], X[:, 1], color=clr_list)

  # Draw line using the model parameters (learned)
  m = model.coef_[0][0]
  c = model.coef_[0][1]
  x2 = max(X[:, 0])
  x1 = min(X[:, 0])
  y1 = x1 * m + c
  y2 = x2 * m + c
  x_coords = [x1, x2]
  y_coords = [y1, y2]
  plt.plot(x_coords, y_coords)
  plt.show()


def read_data(file_path):
  '''
  '''
  data = np.loadtxt(file_path)
  return data


def run_experiment(x_path, y_path):
  '''
  '''
  # Read X and y training matrices / data and train Logistic regression model
  X_data = read_data(x_path)
  y_data = read_data(y_path)
  model = train(X_data, y_data)

  # Test the trained model with the training data and calculate training error
  train_error = test(X_data, y_data, model)
  print('The training error ---> ', round(train_error * 100, 2))

  # Plot the data points and Hypothesis function which separates data
  plot(X_data, y_data, model)


if __name__ == '__main__':
  args = sys.argv[1:]
  X_PATH, Y_PATH = args
  run_experiment(X_PATH, Y_PATH)
