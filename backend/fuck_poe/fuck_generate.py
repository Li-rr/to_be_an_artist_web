# from network_model import poetry_network
from backend.fuck_poe.network_model import poetry_network
# from make_data import *
from backend.fuck_poe.network_model import *
import tensorflow as tf
import numpy as np
import pickle

def gen_poetry(restore_net,vocab_to_int,int_to_vocab,prime_word='白',top_n=5,rule=7,sentence_lines=4,hidden_head=None):
    '''
    :param prime_word: 开始的头一个字
    :param top_n: 从前N个候选汉字随机选择
    :param rule: 默认是7言绝句
    :param sentence_lines: 生成几句古诗，默认是4句
    :param hidden_head: 藏头诗的前几个字
    :return:
    '''
    gen_length = sentence_lines *(rule+1) - len(prime_word)
    gen_sentences = [prime_word] if hidden_head==None else [hidden_head[0]]
    temperature =1.0

    dyn_input = [vocab_to_int[s] for s in prime_word]
    dyn_input = tf.expand_dims(dyn_input,0)

    dyn_seq_length = len(dyn_input[0])
    print('dyn_seq_length',dyn_seq_length)

    restore_net.model.reset_states()
    index = len(prime_word) if hidden_head == None else 1
    for n in range(gen_length):
        index += 1
        # 将数据喂入模型
        predictions = restore_net.model(np.array(dyn_input))
        print("-------------------------------->")
        print(predictions)
        predictions = tf.squeeze(predictions,0)
        print("================================>")
        print(predictions)

        if index!=0 and (index %(rule+1)) == 0:
            if ((index / (rule+1)) +1)%2 == 0:
                predicted_id = vocab_to_int['，']
            else:
                predicted_id = vocab_to_int['。']
        else:
            if hidden_head != None and (index-1)%(rule+1)==0 and (index-1)//(rule+1) < len(hidden_head):
                predicted_id = vocab_to_int[hidden_head[(index-1)//(rule+1)]]
            else:
                while True:
                    predictions = predictions / temperature
                    predicted_id = tf.random.categorical(predictions,num_samples=1)[-1,0].numpy()
                    if(predicted_id != vocab_to_int['，']and predicted_id!= vocab_to_int['。']):
                        break

        dyn_input = tf.expand_dims([predicted_id],0)
        gen_sentences.append(int_to_vocab[predicted_id])
    poetry_script = ' '.join(gen_sentences)
    poetry_script = poetry_script.replace('\n ', '\n')
    poetry_script = poetry_script.replace('( ', '(')
    return poetry_script

if __name__ == '__main__':
    # 加载数据
    int_text,vocab_to_int,int_to_vocab = \
        pickle.load(open('preprocess.p', mode='rb'))
    # 加载保存的模型，准备预测
    restore_net = poetry_network(vocab_size=len(int_to_vocab),batch_size=1)
    restore_net.model.build()


    poem3 = gen_poetry(restore_net=restore_net,vocab_to_int=vocab_to_int,
                       int_to_vocab=int_to_vocab,top_n=10,rule=7,
                       sentence_lines=4,hidden_head='上海电力')
    print(poem3)