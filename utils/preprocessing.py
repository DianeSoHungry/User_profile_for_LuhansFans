import os
import jieba
import json
import jieba.analyse
def MergeStopwords(sw_dir = "./dict/stopwords/"):
    '''
    载入停用词表，汇总后保存至merged——stopwords.txt，并返回汇总后的停用词。
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
    return my_stopwords

def EmojiDictMaking(emoji_dir = "./dict/emoji_dictionaries/"):
    '''
    制作表情字典,下载的表情字符源文件转换成jieba标准字典格式
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