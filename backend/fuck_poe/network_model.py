import tensorflow as tf
import time
import os
from tensorflow.python.ops import summary_ops_v2
#------
# from defaults import *
from backend.fuck_poe.defaults import *
class poetry_network(object):
    def __init__(self,vocab_size,batch_size=32):
        '''
        :param vocab_size:
        :param batch_size:
        '''
        self.batch_size = batch_size
        self.best_loss = 9999
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size,embed_dim,batch_input_shape=[batch_size,None]),
            tf.keras.layers.LSTM(rnn_size,
                                 return_sequences=True,
                                 stateful=True,
                                 recurrent_initializer='glorot_uniform'),
            tf.keras.layers.Dense(vocab_size)
        ])
        self.model.summary()
        self.optimizer = tf.keras.optimizers.Adam(0.001)
        # 用于计算损失
        # 根据预测结果(logits)进行计算损失
        self.computeLoss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        # 要存放训练出来的模型，先生成文件
        if tf.io.gfile.exists(MODEL_DIR):
            pass
        else:
            tf.io.gfile.makedirs(MODEL_DIR)
        train_dir = os.path.join(MODEL_DIR,'summaries','train')
        # 用于记录日志
        self.train_summary_writer = summary_ops_v2.create_file_writer(train_dir,flush_millis=10000)

        # 生成节点和保存模型
        # prefix: 前缀
        checkpoint_dir = os.path.join(MODEL_DIR, 'checkpoints')
        self.checkpoint_prefix = os.path.join(checkpoint_dir, 'ckpt')
        self.checkpoint = tf.train.Checkpoint(model = self.model,optimizer=self.optimizer)
        # 加载已存在的模型
        self.checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
    @tf.function
    def train_step(self,x,y):
        with tf.GradientTape() as tape:
            logits = self.model(x,training=True)
            loss = self.computeLoss(y,logits)
        grads = tape.gradient(loss,self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads,self.model.trainable_variables))
        return loss,logits
    def training(self,train_batches,epochs=1,log_freq=50):
        # batchCnt = len(int_text) // (batch_size * seq_length)
        # print("batchCnt的值是", batchCnt)

        # 训练的循环
        for i in range(epochs):
            train_start = time.time()   # 记录开始时间
            with self.train_summary_writer.as_default():
                start = time.time()

                # 定义平均指标用来计算平均损失
                # 指标是有状态的，它们会累加值并返回累加结果。使用.reset_states()清楚累积值
                avg_loss = tf.keras.metrics.Mean('loss',dtype=tf.float32)

                for batch_i,(x,y) in enumerate(train_batches):
                    # 单步训练
                    loss,logits = self.train_step(x,y)
                    avg_loss(loss)
                    losses['train'].append(loss)

                    if tf.equal(self.optimizer.iterations %log_freq,0):
                        summary_ops_v2.scalar('loss',avg_loss.result(),step=self.optimizer.iterations)
                        rate = log_freq / (time.time()-start)
                        print('Step #{}\tLoss:{:0.6f}({}steps/sec)'.format(self.optimizer.iterations.numpy(), loss, rate))
                        avg_loss.reset_states()
                        start = time.time()
                self.checkpoint.save(self.checkpoint_prefix)
                print("save model\n")