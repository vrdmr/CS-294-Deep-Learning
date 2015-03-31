__author__ = 'varadmeru'

from pybrain.structure import LSTMLayer
from pybrain.tools.shortcuts import buildNetwork

net = buildNetwork(2, 3, 1, recurrent=True, hiddenclass=LSTMLayer)
net.activate([2, 1])