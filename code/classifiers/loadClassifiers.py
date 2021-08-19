import pdb

from classifiers.ActionClassifier import ClassifierArgs
from classifiers.ThreeLayerMLP import ThreeLayerMLP
from classifiers.STGCN import STGCN
from classifiers.CTRGCN import CTRGCN
from classifiers.MSG3D import MSG3D
from classifiers.SGN import SGN
from classifiers.BayesianClassifier import ExtendedBayesianClassifier

def loadClassifier(args):
    classifier = ''
    if args.classifier == '3layerMLP':
        classifier = ThreeLayerMLP(args)
    elif args.classifier == 'STGCN':
        classifier = STGCN(args)
    elif args.classifier == 'CTRGCN':
        classifier = CTRGCN(args)
    elif args.classifier == 'ExtendedBayesian':
        classifier = ExtendedBayesianClassifier(args)
    elif args.classifier == 'MSG3D':
        classifier = MSG3D(args)
    elif args.classifier == 'SGN':
        classifier = SGN(args)
    else:
        print('No classifier created')

    return classifier