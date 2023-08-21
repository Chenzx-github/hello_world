# -*- coding: utf-8 -*-

"""
    此脚本将语料库转为字符格式
    —————————————————
    usage: python3 trans_corpus.py

    Last commit info:
    ~~~~~~~~~~~~~~~~~
    $LastChangedDate: 2022/06/06
    $Annotation: Create.
    $Author: xiyan19
"""


import gensim

if __name__ == "__main__":
    corpus_file = '/home/czx/pycharm/JSob/JSob_seq/origin/test/raw_corpus'
    trans_corpus_file = '/home/czx/pycharm/JSob/JSob_seq/origin/test/char_corpus1'

    dict = gensim.corpora.dictionary.Dictionary.load('/home/czx/pycharm/JSob/JSob_seq/medium/train/ast1.dict')

    trans_list = []

    with open(corpus_file, 'r') as cf:
        context = cf.readlines()

        for line in context:
            # line = line.replace('\n', '')
            sp = line.split(' ')
            sp = sp[1:-1]
            trans = ''

            for s in sp:
                if s != '':
                    ascii = dict.token2id[s] + 65
                    if ascii > 90:
                        ascii += 6
                    trans += chr(ascii)

            trans_list.append(trans + '\n')

    with open(trans_corpus_file, 'w') as tf:
        tf.writelines(trans_list)

    print('Done!')