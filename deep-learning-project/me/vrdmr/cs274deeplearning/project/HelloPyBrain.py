__author__ = 'varadmeru'

from pybrain.structure.networks.rbm import Rbm
from pybrain.unsupervised.trainers.rbm import (RbmGibbsTrainerConfig,RbmBernoulliTrainer)
from pybrain.datasets import UnsupervisedDataSet


def __main__():
    ds = UnsupervisedDataSet(6)
    ds.addSample([0, 1] * 3)
    ds.addSample([1, 0] * 3)
    ds.addSample([1, 0] * 3)
    ds.addSample([1, 0] * 3)
    ds.addSample([0, 0] * 3)
    ds.addSample([1, 1] * 3)
    ds.addSample([1, 0] * 3)

    for i in ds:
        print i

    cfg = RbmGibbsTrainerConfig()
    cfg.maxIter = 3
    rbm = Rbm.fromDims(6,6)
    trainer = RbmBernoulliTrainer(rbm, ds, cfg)
    print rbm.params, rbm.biasParams

    for _ in xrange(50):
        trainer.train()

    print rbm.params, rbm.biasParams

if __name__ == '__main__':
    __main__()