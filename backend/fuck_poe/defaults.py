# 批次大小
batch_size = 32
# RNN的大小，隐藏节点的维度
rnn_size = 1000
# 嵌入层的维度
embed_dim = 256
# 序列的长度，在古诗预测里，这个可以大一点
seq_length = 15

save_dir = '.\\save'

MODEL_DIR = '.\\poetry_models'
losses = {'train': [], 'test': []}