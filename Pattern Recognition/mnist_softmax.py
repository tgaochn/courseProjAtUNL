# encoding=utf-8

# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A very simple MNIST classifier.
See extensive documentation at
http://tensorflow.org/tutorials/mnist/beginners/index.md
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import input_data
import mnist

import tensorflow as tf

FLAGS = None

def fill_feed_dict(data_set, images_pl, labels_pl):
    """
    Fills the feed_dict for training the given step.

    A feed_dict takes the form of:
    feed_dict = {
      <placeholder>: <tensor of values to be passed for placeholder>,
      ....
    }

    Args:
    data_set: The set of images and labels, from input_data.read_data_sets()
    images_pl: The images placeholder, from placeholder_inputs().
    labels_pl: The labels placeholder, from placeholder_inputs().

    Returns:
    feed_dict: The feed dictionary mapping from placeholders to values.
    """
    # Create the feed_dict for the placeholders filled with the next
    # `batch size` examples.
    images_feed, labels_feed = data_set.next_batch(FLAGS.batch_size, FLAGS.fake_data)
    feed_dict = {images_pl: images_feed, labels_pl: labels_feed, }
    return feed_dict
#end_func

def main(_):
    x = tf.placeholder(tf.float32, [None, 784]) # 28*28的图像
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, W) + b  # 矩阵乘法
    y_ = tf.placeholder(tf.float32, [None, 10])

    # data_sets = input_data.read_data_sets(FLAGS.data_dir, FLAGS.fake_data)
    data_sets = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
    images_placeholder = tf.placeholder(tf.float32, shape=(FLAGS.batch_size, mnist.IMAGE_PIXELS))
    labels_placeholder = tf.placeholder(tf.int32, shape=(FLAGS.batch_size))
    logits = mnist.inference(images_placeholder, FLAGS.hidden1, FLAGS.hidden2)
    # loss = mnist.loss(logits, labels_placeholder)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    # train_step = mnist.training(loss, FLAGS.learning_rate)
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    for step in range(FLAGS.max_steps):
        # images_feed, labels_feed = data_sets.train.next_batch(100, FLAGS.fake_data)
        images_feed, labels_feed = data_sets.train.next_batch(100)
        # feed_dict = {images_placeholder: images_feed, labels_placeholder: labels_feed, }
        feed_dict = {x: images_feed, y_: labels_feed}
        _, loss_value = sess.run([train_step, loss], feed_dict=feed_dict)
        if step % 100 == 0:
            print('Step %d: loss = %.2f ' % (step, loss_value))

    print('end')
    exit(0)

    # 定义数据模板
    x = tf.placeholder(tf.float32, [None, 784]) # 28*28的图像
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, W) + b  # 矩阵乘法
    y_ = tf.placeholder(tf.float32, [None, 10])

    # images_placeholder, labels_placeholder = placeholder_inputs(FLAGS.batch_size)
    # 定义loss: cross_entropy, 迭代方法(梯度下降), 优化目标
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
    sess = tf.InteractiveSession()

    # 初始化
    tf.global_variables_initializer().run()

    # 数据输入
    data_sets = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    # Train
    for step in range(1000):
        # 取mnist下一个batch的数据
        images_feed, labels_feed = data_sets.train.next_batch(100)
        # 训练
        feed_dict = {x: images_feed, y_: labels_feed}
        sess.run(train_step, feed_dict=feed_dict)

        # Test trained model
        # correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        # print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


if __name__ == '__main__':
    # 使用parser定义各种参数, 放入FLAGS中, 之后调用
    parser = argparse.ArgumentParser()
    parser.add_argument('--learning_rate', type=float, default=0.01, help='Initial learning rate.')
    parser.add_argument('--max_steps', type=int, default=2000, help='Number of steps to run trainer.')
    parser.add_argument('--hidden1', type=int, default=128, help='Number of units in hidden layer 1.')
    parser.add_argument('--hidden2', type=int, default=32, help='Number of units in hidden layer 2.')
    parser.add_argument('--batch_size', type=int, default=100,
                        help='Batch size.  Must divide evenly into the dataset sizes.')
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                        help='Directory to put the input data.')
    parser.add_argument('--log_dir', type=str, default='/tmp/tensorflow/mnist/logs/fully_connected_feed',
                        help='Directory to put the log data.')
    parser.add_argument('--fake_data', default=False, help='If true, uses fake data for unit testing.',
                        action='store_true')
    FLAGS, unparsed = parser.parse_known_args()

    # 执行main函数
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
