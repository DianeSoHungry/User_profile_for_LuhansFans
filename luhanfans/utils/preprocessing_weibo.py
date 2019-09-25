"""
@author: Qingyun Hu
@contact: dianesohungry@gmail.com
"""

import os
import pandas as pd
import jieba
import json
from collections import defaultdict
from jieba import analyse

def CreateTagsByID(weibo_dir, dest_dir, emoji_path, customized_path, stopwords_path, topK = 40):
    '''
    遍历scraped_data夹中的所有文件，对同一ID的博文进行汇总，并根据TF-IDF提取属于该ID的标签，保存在user_tags文件夹中。
    Args:
        weibo_dir: 爬取的微博博文数据所在目录
        dest_dir: 聚合后，每个用户的TFIDF标签群保存目录
        emoji_path: 自制表情符地址（merge后）
        customized_path: 自制用户词典地址（merge后）
        stopwords_path: 停用词地址（merge后）
        topK: 选取最大topK个标签
    Returns:
    
    
    '''
    jieba.load_userdict(emoji_path)
    jieba.load_userdict(customized_path)
    analyse.set_stop_words(stopwords_path)
    jieba.enable_parallel()
    for filename in os.listdir(weibo_dir):
        res = defaultdict()
        if(filename[0] == "."):
            continue
        raw_data = pd.read_csv(weibo_dir + filename)
        text_per_uid = raw_data.groupby("uid")["weibotxt"].sum()
        for idx in text_per_uid.index:
            res[str(idx)] = jieba.analyse.extract_tags(text_per_uid[idx], topK = topK)
        with open(dest_dir + filename[:-4] + ".json", "w") as f:
            json.dump(res, f)