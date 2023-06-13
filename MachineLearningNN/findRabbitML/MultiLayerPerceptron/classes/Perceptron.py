import numpy as np
import random as rnd


class Perceptron:

  def __init__(self, func, derivFunc):
    self.weights = []
    self.b = round(rnd.random(), 1)
    self.func = func
    self.derivFunc = derivFunc
  def setParameteres(self, lenData, learning_rate=0.1):
    self.weights = list(map(lambda x: round(rnd.random(), 1) , range(lenData)))
    self.learn_rate = learning_rate

  def getValue(self, dataSet):

    return sum(self.weights * dataSet) + self.b

  def getValueWithFuncs(self,dataSet):
    return self.func(sum(self.weights * dataSet) + self.b)

  def countDeriv(self, dataSet):
    derivRes = self.derivFunc(self.getValue(dataSet))
    self.derivNeiron = np.append(np.array(dataSet)*derivRes, derivRes)
    self.PastNeirons = []
    for d in range(len(dataSet)):
      self.PastNeirons.append(self.derivNeiron[d])

  def countDerivWeights(self, dataSet):
    derivRes = self.derivFunc(self.getValue(dataSet))
    self.derivWeigths = np.array(self.weights) * derivRes

  def setWeigths(self, derivAllYPred, predNextNeiron=1):
    for w in range(len(self.weights)):
      self.weights[w] -= self.learn_rate * derivAllYPred* predNextNeiron * self.derivNeiron[w]
    self.b -= self.learn_rate * derivAllYPred* predNextNeiron * self.derivNeiron[-1]



  def getWeights(self):
    return np.array(self.weights)


  def getPastNeirons(self):
    return np.array(self.PastNeirons)


