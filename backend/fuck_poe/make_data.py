import os
import numpy as np
import pickle
# 处理初始数据集
def preprocess_poetry(outdir,datadir):
    with open(os.path.join(outdir,'new_poetry.txt'),'w',encoding='utf-8') as out_f:
        with open(os.path.join(datadir,'poetry.txt'),'r',encoding='utf-8') as f:
            for i,line in enumerate(f):
                #print(line)
                try:
                    title,content = line.strip().rstrip('\n').split(':')
                except:
                    continue    # 遇见异常就跳过
                # 去除空格
                content = content.replace(' ','')
                #print(content)
                # 舍弃含有非法字符的唐诗
                if '】' in content or '_' in content or '(' in content or '（' in content \
                        or '《' in content or '[' in content:
                    continue
                # 舍弃过短的唐诗
                if len(content) < 20:
                    continue
                out_f.write(content+'\n')

# 数据集预处理
def create_lookup_tables(file='data\\newtxt.txt'):
    text = open(file,'r',encoding='utf-8').read()   # 读取文本
    vocab =sorted(set(text))
    #print(vocab)
    vocab_to_int = {u:i for i,u in enumerate(vocab)}

    int_to_vocab = np.array(vocab)
    #print(int_to_vocab,int_to_vocab.shape)
    # 将文本转为数字
    int_text = np.array([vocab_to_int[word] for word in text if word != '\n'])
    # 将数据通过特殊的形式转换为只有python语言认识的字符串
    pickle.dump((int_text, vocab_to_int, int_to_vocab), open('preprocess.p', 'wb'))

# 读取保存的数据
def get_batches(int_text,batch_size,seq_length):
    print('vocab size',len(int_text))
    print('batch_size',batch_size)
    print('seq_length',seq_length)
    batchCnt = len(int_text)    // (batch_size * seq_length)
    print('batchCnt',batchCnt)

    # y 取x的下一个
    int_text_inputs = int_text[:batchCnt*(batch_size*seq_length)]
    int_text_targets = int_text[1 : batchCnt*(batch_size * seq_length)+1]

    x = np.array(int_text_inputs).reshape(1,batch_size,-1)
    y = np.array(int_text_targets).reshape(1,batch_size,-1)

    # 这里不是很理解
    x_new = np.dsplit(x,batchCnt)
    y_new = np.dsplit(y,batchCnt)
    result_list = []
    for ii in range(batchCnt):
        x_list = []
        x_list.append(x_new[ii][0])
        x_list.append(y_new[ii][0])
        result_list.append(x_list)

    return np.array(result_list)