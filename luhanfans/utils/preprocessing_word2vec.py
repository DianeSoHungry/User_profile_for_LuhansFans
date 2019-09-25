"""
@author: Qingyun Hu
@contact: dianesohungry@gmail.com
"""
from concurrent.futures import ProcessPoolExecutor
import json
def ParseLine(line):
    '''
    ParseWord2Vec2Ways函数的工具函数，用于解析Corpus中的单行输入。
    Args:
        line: Corpus中的一行
    Return:
        二元组: 第一个元素为词，第二个为词向量
    '''
    tmp = line.strip().split()
    return (tmp[0],list(map(float, tmp[1:])))

def ParseWord2Vec2Ways(corpus_dir = "../data/corpus/", corpus_filename = "sgns.weibo.bigram-char", word2vec_filename = "word_to_vec.json", vec2word_filename = "vec_2_word.json", save = False, ret = True):
    '''
    从预训练词库中提取词向量的双向映射，并以JSON格式保存至硬盘。
    Args:
        corpus_dir: 语料库所在目录
        corpus_filename: 语料库名称
        word2vec_filename: 词到词向量的字典
        vec2word_filename: 词向量到词的字典
        save: 是否保存JSON文件
        ret: 是否返回
        
    '''
    corpus_path = corpus_dir + corpus_filename
    with open(corpus_path) as f:
        word2vec = {}
        vec2word = {}
        lines = f.readlines()
        for k, v in ProcessPoolExecutor(4).map(ParseLine, lines):    # 4个进程并发处理
            word2vec[k] = tuple(v)
            vec2word[tuple(v)] = k
    
    if save == True:
        with open(corpus_dir + word2vec_filename, "w") as w2v_f:
            w2v_f.write(json.dumps(word2vec))
        with open(corpus_dir + vec2word_filename, "w") as v2w_f:
            v2w_f.write(json.dumps(vec2word))
        
    if ret == True:
        return word2vec, vec2word