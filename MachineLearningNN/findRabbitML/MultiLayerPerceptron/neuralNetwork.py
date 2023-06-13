import numpy as np
from classes.Perceptron import Perceptron


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
  fx = sigmoid(x)
  return fx * (1 - fx)


def mse_loss(y_true, y_pred):
  return ((y_true - y_pred) ** 2).mean()


class NeuralNetwork:

    def getAllPerceptronsResults(self, dataTest):
        res = []

        dataTest = dataTest.copy()
        for l in self.neirons:
            layerTest = []
            for n in l:
                layerTest.append(n.getValueWithFuncs(dataTest))
            dataTest = np.array(layerTest)
            res.append(dataTest)
        return res

    def getResult(self, x):
        data = np.array(x)

        for l in self.neirons:
            dataLayer = []
            for n in l:

                dataLayer.append(n.getValueWithFuncs(data))
            data = np.array(dataLayer)
        return data[0]

    def test(self, dataX):
        res = []
        for x in dataX:
            resF = self.getResult(x)
            if 1 - resF > resF:
                res.append(0)
            else:
                res.append(1)
        return res

    def __init__(self, hideLayers=1, epochs=1000, neironsInLayers=None):
        if neironsInLayers is None:
            neironsInLayers = [3]*hideLayers
        self.neirons = []
        self.epochs = epochs
        for l in range(hideLayers):
            neironsLayer = []
            for n in range(neironsInLayers[l]):
                neironsLayer.append(Perceptron(sigmoid, deriv_sigmoid))
            self.neirons.append(neironsLayer)
        self.neirons.append([Perceptron(sigmoid, deriv_sigmoid)])

    def fit(self, dataX, dataY):
        for n in range(len(self.neirons[0])):
            self.neirons[0][n].setParameteres(len(dataX[0]))
        for l in range(1,len(self.neirons)):
            for n in range(len(self.neirons[l])):
                self.neirons[l][n].setParameteres(len(self.neirons[l-1]))

        for e in range(self.epochs):
            for x, y in zip(dataX, dataY):


                results = self.getAllPerceptronsResults(x)
                for n in self.neirons[0]:
                    n.countDeriv(x)

                for layer in range(1, len(self.neirons)):
                    for n in range(len(self.neirons[layer])):
                        self.neirons[layer][n].countDeriv(results[layer-1])
                        self.neirons[layer][n].countDerivWeights(results[layer-1])

                testingYpred = -2 * (y - results[-1][0])

                for layer in range(len(self.neirons)):
                    for n in range(len(self.neirons[layer])):
                        if layer+1 >= len(self.neirons):
                            self.neirons[layer][n].setWeigths(testingYpred)
                            continue
                        for neironNext in range(len(self.neirons[layer+1])):
                            self.neirons[layer][n].setWeigths(testingYpred, self.neirons[layer+1][neironNext].getPastNeirons()[n])

            if e % 10 == 0:
                y_preds = np.apply_along_axis(self.getResult, 1, dataX)
                loss = mse_loss(dataY, y_preds)
                print("Epoch %d loss: %.3f" % (e, loss))



                #print(allWeights, allNeironWeights)








