"""
@author: Qingyun Hu
@contact: dianesohungry@gmail.com
"""
import sys
sys.path.append("./utils/")

from preprocessing_dictionary import * 
from preprocessing_word2vec import *
from preprocessing_weibo import CreateTagsByID
from preprocessing_weibo_corpus import *

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

import numpy as np

EMOJI_DIR = "../data/dict/emoji_dictionaries/"
EMOJI_FILENAME = "merged_emoji_dictionary.txt"

CUSTOMIZED_DICTIONARY_DIR = "../data/dict/customized_dictionaries/"
CUSTOMIZED_DICTIONARY_FILENAME = "merged_customized_dictionary.txt"

STOPWORDS_DIR = "../data/dict/stopwords/"
STOPWORDS_FILENAME = "merged_stopwords.txt"

CORPUS_DIR = "../data/corpus/"
CORPUS_FILENAME = "sgns.weibo.bigram-char"

DATA_DIR = "../data/scraped_data/"

USER_TAGS_DIR = "../data/user_tags/"

WORD2VEC_PATH = "../data/corpus/word_to_vec.json"

TARGET_DIR = "../data/dict/targets/"

USER_PROFILE = "../data/results/"


def main():
    if(len([filename for filename in os.listdir(USER_TAGS_DIR) if "txt.json" == filename[-8:]]) == 0):
        CreateTagsByID(weibo_dir= DATA_DIR, 
               topK = 40,
               dest_dir = USER_TAGS_DIR,
               emoji_path = EMOJI_DIR + EMOJI_FILENAME, 
               customized_path = CUSTOMIZED_DICTIONARY_DIR + CUSTOMIZED_DICTIONARY_FILENAME, 
               stopwords_path = STOPWORDS_DIR + STOPWORDS_FILENAME
               )
    wv = KeyedVectors.load_word2vec_format(CORPUS_DIR + CORPUS_FILENAME)
    target_dict = CreateTargetDict(TARGET_DIR)
    for user_tags_filename in os.listdir(USER_TAGS_DIR):
        if("txt.json" != user_tags_filename[-8:]):
            continue
        with open(USER_TAGS_DIR + user_tags_filename) as f:
            user_tags = json.load(f)
        with open(USER_PROFILE + user_tags_filename[:-8] + ".csv", "w") as res_f:
            for id_, tags in user_tags.items():
                res_f.write(id_)
                for target_name, target_values in target_dict.items():
                    try:
                        res_f.write("," + Tags2Target(tags, target_values, wv))
                    except TypeError as none_type:
                        res_f.write(",")
                res_f.write("\n")
    print("运行结束，结果请前往%s" % USER_PROFILE )
                
                
if __name__ == "__main__":
    main()