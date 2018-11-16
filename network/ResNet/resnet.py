# coding=utf-8

__all__ = ['create', 'build', 'predict', 'train']

import os
import numpy as np
import tensorflow as tf


class NetworkData:
        x = None
        y = None
        pred_y = None
        dropout_prob = None
        train_step = None
        accuracy = None
        saver = None
        batch_count = 0
        batch_size = 1000


def create():
        return NetworkData()


def _weight_variable(shape: list):
        initial = tf.truncated_normal(shape, stddev=.1)
        return tf.Variable(initial)


def _bias_variable(shape: list):
        initial = tf.constant(.1, shape=shape)
        return tf.Variable(initial)


def _layer_pool(flow):
        return tf.nn.max_pool(flow, ksize=[1, 3, 3, 1],
                              strides=[1, 2, 2, 1], padding='SAME')


def _layer_relu(flow):
        return tf.nn.relu(flow)


def _layer_conv(flow, weight_size: list, bias_size: list, relu=False):
        weight = _weight_variable(weight_size)
        bias = _bias_variable(bias_size)
        flow = tf.nn.conv2d(flow, weight, strides=[1, 1, 1, 1],
                            padding='SAME') + bias
        if relu:
                flow = _layer_relu(flow)
        return flow


def _layer_fc(flow, weight_size: list, bias_size: list, relu=False):
        weight = _weight_variable(weight_size)
        bias = _bias_variable(bias_size)
        flow = tf.matmul(flow, weight) + bias
        if relu:
                flow = _layer_relu(flow)
        return flow


def build(network_data: NetworkData):
        def build_layer(flow_main, in_size: int, out_size: int):
                flow_residual = _layer_conv(flow_main, [3, 3, in_size, out_size], [out_size], relu=True)
                flow_residual = _layer_conv(flow_residual, [3, 3, out_size, out_size], [out_size], relu=False)
                flow_main = _layer_conv(flow_main, [1, 1, in_size, out_size], [out_size], relu=False)
                flow_main += flow_residual
                return _layer_relu(flow_main)

        network_data.x = tf.placeholder('float', shape=[None, 784])
        network_data.y = tf.placeholder('float', shape=[None, 10])
        flow = tf.reshape(network_data.x, [-1, 28, 28, 1])  # grey
        flow = build_layer(flow, 1, 8)  # CONV1_1
        flow = build_layer(flow, 8, 8)  # CONV1_2
        flow = _layer_pool(flow)  # MAXPOOL1
        flow = build_layer(flow, 8, 16)  # CONV2_1
        flow = build_layer(flow, 16, 16)  # CONV2_2
        flow = _layer_pool(flow)  # MAXPOOL2
        flow = build_layer(flow, 16, 32)  # CONV3_1
        flow = build_layer(flow, 32, 32)  # CONV3_2
        flow = tf.reshape(flow, [-1, 7 * 7 * 32])
        flow = _layer_fc(flow, [7 * 7 * 32, 120], [120], relu=True)  # FC1
        network_data.dropout_prob = tf.placeholder('float')
        flow = tf.nn.dropout(flow, network_data.dropout_prob)  # Dropout
        flow = _layer_fc(flow, [120, 10], [10], relu=True)  # FC2
        network_data.pred_y = flow = tf.nn.softmax(flow)  # Softmax
        # learning
        cross_entropy = -tf.reduce_sum(network_data.y * tf.log(flow))
        network_data.train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        correct_predict = tf.equal(tf.argmax(flow, 1), tf.argmax(network_data.y, 1))
        network_data.accuracy = tf.reduce_mean(tf.cast(correct_predict, 'float'))


def train_session(network_data: NetworkData):
        sess = tf.InteractiveSession()
        sess.run(tf.global_variables_initializer())
        network_data.saver = tf.train.Saver()
        checkpoint = tf.train.get_checkpoint_state(os.path.dirname(__file__))
        if checkpoint and checkpoint.model_checkpoint_path:
                network_data.saver.restore(sess, checkpoint.model_checkpoint_path)
        return sess


def train(sess, batch, network_data: NetworkData):
        if network_data.batch_count > network_data.batch_size:
                train_accuracy = network_data.accuracy.eval(feed_dict={
                        network_data.x: batch[0], network_data.y: batch[1],
                        network_data.dropout_prob: 1})
                print('training accuracy %g' % (train_accuracy))
                network_data.saver.save(sess, _prefix_path() + './model.ckpt')
                network_data.batch_count -= network_data.batch_size
        network_data.train_step.run(feed_dict={network_data.x: batch[0], network_data.y: batch[1],
                                               network_data.dropout_prob: 0.5})
        network_data.batch_count += len(batch[1])


def predict(network_data: NetworkData):
        sess = tf.InteractiveSession()
        sess.run(tf.global_variables_initializer())
        network_data.saver = tf.train.Saver(tf.global_variables())
        network_data.saver.restore(sess, _prefix_path() + './model.ckpt')
        print("test accuracy %g" % network_data.accuracy.eval(feed_dict={
                network_data.x: mnist.test.images, network_data.y: mnist.test.labels,
                network_data.dropout_prob: 1}))
        sess.close()


def read(network_data: NetworkData, input_image):
        sess = tf.InteractiveSession()
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver(tf.global_variables())
        saver.restore(sess, _prefix_path() + './model.ckpt')
        output_number = network_data.pred_y.eval(feed_dict={network_data.x: [input_image],
                                                            network_data.dropout_prob: 1})
        result = np.where(output_number == np.max(output_number))[1][0]
        sess.close()
        return result


def _prefix_path() -> str:
        return os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
        import input_data

        mnist = input_data.read_data_sets('data', one_hot=True)
        resnet = create()
        build(resnet)

        sess = train_session(resnet)
        for i in range(200):
                batch = mnist.train.next_batch(50)
                train(sess, batch, resnet)
        sess.close()

        predict(resnet)
