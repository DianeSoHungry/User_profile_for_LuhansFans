"""
@author: Qingyun Hu
@contact: dianesohungry@gmail.com
"""
import os
import jieba
import json
import jieba.analyse


def MergeStopwords(sw_dir = "../../data/dict/stopwords/", ret_sw = False):
    '''
    载入所有停用词表，汇总后保存至同目录下的merged_stopwords.txt文件中，并返回汇总后的停用词。
    Args:
        sw_dir: 所有停用词表所在目录
        ret_sw: 返回汇总后的停用词merged_stopwords
    Returns:
        my_stopwords: 当参数ret_sw为真时，返回合并后的停用词表 
    '''
    
    my_stopwords=set()
    sw_filenames = os.listdir(sw_dir)
    for filename in sw_filenames:
        if filename[0] == '.' or filename == "merged_stopwords.txt":
            continue
        with open(sw_dir + filename, "r") as f:
            for line in f.readlines():
                my_stopwords.add(line.strip())
    my_stopwords = list(my_stopwords) + ["\n","\u200b","\xa0"," ","......."]
    with open(sw_dir + "merged_stopwords.txt", "w") as f:
        f.writelines("\n".join(my_stopwords))
    if ret_sw:
        return my_stopwords 
    return


def EmojiDictMaking(emoji_dir = "../../data/dict/user_dictionaries/emoji_dictionaries/"):
    '''
    制作表情字典,下载的表情字符源文件转换成jieba标准字典格式，并汇总写入同目录下的merged_emoji_dictionary.txt文件
    Args:
        emoji_dir: 表情符所有文件所在目录
    Returns:
        
    '''
    emoji_set = set()
    emoji_filenames = os.listdir(emoji_dir)
    for emoji_raw_file in emoji_filenames:
        if emoji_raw_file[0] in [".", "merged_emoji_dictionary.txt"]:
            continue
        with open(emoji_dir + emoji_raw_file,'r') as f:
            emoji_set = emoji_set.union(set(f.readline().strip().replace('[','').split(']')[:-1]))
    with open(emoji_dir + 'merged_emoji_dictionary.txt','w') as f:
        f.writelines("\n".join(list(emoji_set)))

    
def init_dicts(sw_dir = "../../data/dict/stopwords/", emoji_dir = "../../data/dict/user_dictionaries/emoji_dictionaries/"):
    '''
    初始化停用词表、表情字典
    Args:
        sw_dir: 所有停用词表所在目录
        emoji_dir: 表情符所有文件所在目录
    Return:
    
        
    '''
    MergeStopwords(sw_dir)
    EmojiDictMaking(emoji_dir)
    