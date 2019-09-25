"""
@author: Qingyun Hu
@contact: dianesohungry@gmail.com
"""
import os
import numpy as np
from collections import defaultdict
def Tags2Target(tags, targets, wv):
    '''
    为单个用户的所有tags选择targets中的最合适标签(词向量的cosine相似度最高)，并返回选取的target值。
    Args:
        tags: 单个用户ID对应的TF-IDF标签
        targets: 预测值目标列表
        wv: 选良好的词向量
    Return:
        选取的标签值
    
    '''
    targets_vecs = list(map(lambda x:wv[x], targets))
    votes = defaultdict(int)
    for tag in tags:
        try:
            idx = np.argmax(wv.cosine_similarities(wv[tag], targets_vecs))
            votes[idx] += 1
        except KeyError as e:
            continue
    try:
        return targets[max(votes, key = votes.get)]
    except:
        pass
    
        
def CreateTargetDict(target_dir):
    '''
    载入target_dir目录下所有的target表，以字典形式返回，键值对形式为{分类方式:分类列表}
    Args:
        target_dir: 各个分类表所在目录
    Return:
        target_dict
        
    
    '''
    target_dict = defaultdict()
    for filename in os.listdir(target_dir):
        if(filename[0] == "."):
            continue
        with open(target_dir + filename) as f:
             target_dict[filename[:4]] = f.read().strip().split("\n")
    return target_dict