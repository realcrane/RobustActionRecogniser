import numpy as np
import pdb
import os
import shutil

dataFolder = '../data/ntu60/'
retFolder = '../results/ntu60/STGCN/SMART/batch0_ab_clw_0.60_pl_l2_acc-bone_plw_0.40/'
# dataFolder = '../data/'

file = 'AdExamples_maxFoolRate_batch0_AttackType_ab_clw_0.60_pl_l2_acc-bone_reCon_0.40_fr_96.88'
# dirName = dataFolder

dirName = retFolder + '/' + file + '/'

if os.path.exists(dirName):
    shutil.rmtree(dirName)

os.makedirs(dirName)

data = np.load(retFolder + file + '.npz')

motions = data['clips']
orMotions = data['oriClips']
plabels = data['classes']
tlabels = data['tclasses']

# core = np.load(dataFolder + 'preprocess_core.npz')
#
# std = core['Xstd'].reshape(len(core['Xstd'][0]))
# mean = core['Xmean'].reshape(len(core['Xmean'][0]))
#
# for i in range(len(motions)):
#     motions[i] = motions[i] * std + mean
#     orMotions[i] = orMotions[i] * std + mean

np.save(dirName + 'ad_motions.npy', motions)
np.savetxt(dirName + 'ad_plabels.txt', plabels)
np.save(dirName + 'ori_motions.npy', orMotions)
np.savetxt(dirName + 'tlabels.txt', tlabels)