# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import input_data

import tensorflow as tf
import mnist

FLAGS = None

import datetime

# initialize weight
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

# initialize bias
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

# Convolution
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# Pooling
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def main(_):
    sess = tf.InteractiveSession()

    # 取数据
    input_data_set = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    # 占位符
    x = tf.placeholder("float", shape=[None, 784])
    y_ = tf.placeholder("float", shape=[None, 10])

    # 第一层卷积, (1 #28x28->32 #28x28)
    # 在每个5x5网格中，提取出32张特征图
    W_conv1 = weight_variable([5, 5, 1, 32])
    # 每个输出通道都有一个偏置项，因此偏置项个数为32
    b_conv1 = bias_variable([32])
    # 为了使之能用于计算, 使用reshape将其转换为四维的tensor
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    # 利用ReLU激活函数，对其进行第一次卷积
    # h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_conv1 = tf.sigmoid(conv2d(x_image, W_conv1) + b_conv1) # 替换激活函数为sigmoid

    # 第一次池化, (32 #28x28->32 #14x14)
    h_pool1 = max_pool_2x2(h_conv1)

    # 第二层卷积与第二次池化, (32  # 14x14->64 #14x14->64 #7x7)
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    # h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_conv2 = tf.sigmoid(conv2d(h_pool1, W_conv2) + b_conv2) # 替换激活函数为sigmoid
    h_pool2 = max_pool_2x2(h_conv2)

    # 加入一个有1024个神经元的密集连接层(全连接层), 图片大小 7*7, 特征数64
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    # 把刚才池化后输出的张量reshape成一个一维向量，再将其与权重相乘，加上偏置项，再通过一个ReLU激活函数。
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    # h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    h_fc1 = tf.sigmoid(tf.matmul(h_pool2_flat, W_fc1) + b_fc1) # 替换激活函数为sigmoid

    # 丢弃法 "dropout" regularization, 防止过拟合
    # 完全随机选取经过神经网络流一半的数据来训练，在每次训练过程中用0来替代被丢掉的激活值，其它激活值合理缩放。
    keep_prob = tf.placeholder("float")
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    # 应用了简单的softmax，输出
    w_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    # y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, w_fc2) + b_fc2) # 包含dropout
    y_conv = tf.nn.softmax(tf.matmul(h_fc1, w_fc2) + b_fc2) # 去掉dropout

    # 计算交叉熵的代价函数
    loss = -tf.reduce_sum(y_ * tf.log(y_conv))

    # 使用优化算法AdamOptimizer使得代价函数最小化
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

    # 找出预测正确的标签
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))

    # 得出通过正确个数除以总数得出准确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    # 开始训练模型, 先初始化
    sess.run(tf.initialize_all_variables())

    # 每100次迭代输出一次日志，共迭代20000次
    for step in range(20000):
        train_batch = input_data_set.train.next_batch(50)
        train_feed_dict = {x: train_batch[0], y_: train_batch[1], keep_prob: 0.5}
        # train_step.run(feed_dict=feed_dict)
        # sess.run(train_step, feed_dict=feed_dict)
        _, train_loss_value = sess.run([train_step, loss], feed_dict=train_feed_dict)

        test_batch = input_data_set.test.next_batch(50)
        test_feed_dict = {x: test_batch[0], y_: test_batch[1], keep_prob: 0.5}
        test_loss_value = sess.run(loss, feed_dict=test_feed_dict)

        if step % 100 == 0:
            print('Step %d: train loss = %.2f, test loss = %.2f. ' % (step, train_loss_value, test_loss_value))
            # train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
            # print("step %d, training accuracy %g" % (step, train_accuracy))

    print("test accuracy %g" % accuracy.eval(feed_dict={x: input_data_set.test.images, y_: input_data_set.test.labels, keep_prob: 1.0}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                        help="Directory for storing input data")
    FLAGS, unparsed = parser.parse_known_args()
    print(datetime.datetime.now())
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
    print(datetime.datetime.now())
