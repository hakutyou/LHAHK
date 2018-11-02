# coding=utf-8

import os
import numpy as np
import tensorflow as tf


class ResNet:
        x = None
        y = None
        pred_y = None
        dropout_prob = None
        train_step = None
        accuracy = None
        saver = None

        def __init__(self):
                pass

        @staticmethod
        def weight_variable(shape: list):
                initial = tf.truncated_normal(shape, stddev=.1)
                return tf.Variable(initial)

        @staticmethod
        def bias_variable(shape: list):
                initial = tf.constant(.1, shape=shape)
                return tf.Variable(initial)

        @staticmethod
        def layer_pool(flow):
                return tf.nn.max_pool(flow, ksize=[1, 3, 3, 1],
                                      strides=[1, 2, 2, 1], padding='SAME')

        @staticmethod
        def layer_relu(flow):
                return tf.nn.relu(flow)

        def layer_conv(self, flow, weight_size: list, bias_size: list, relu=False):
                weight = self.weight_variable(weight_size)
                bias = self.bias_variable(bias_size)
                flow = tf.nn.conv2d(flow, weight, strides=[1, 1, 1, 1],
                                    padding='SAME') + bias
                if relu:
                        flow = self.layer_relu(flow)
                return flow

        def layer_fc(self, flow, weight_size: list, bias_size: list, relu=False):
                weight = self.weight_variable(weight_size)
                bias = self.bias_variable(bias_size)
                flow = tf.matmul(flow, weight) + bias
                if relu:
                        flow = self.layer_relu(flow)
                return flow

        def build(self):
                def build_layer(flow_main, in_size: int, out_size: int):
                        flow_residual = self.layer_conv(flow_main, [3, 3, in_size, out_size], [out_size], relu=True)
                        flow_residual = self.layer_conv(flow_residual, [3, 3, out_size, out_size], [out_size], relu=False)
                        flow_main = self.layer_conv(flow_main, [1, 1, in_size, out_size], [out_size], relu=False)
                        flow_main += flow_residual
                        return self.layer_relu(flow_main)

                self.x = tf.placeholder('float', shape=[None, 784])
                self.y = tf.placeholder('float', shape=[None, 10])

                flow = tf.reshape(self.x, [-1, 28, 28, 1])  # grey

                flow = build_layer(flow, 1, 8)  # CONV1_1
                flow = build_layer(flow, 8, 8)  # CONV1_2
                flow = self.layer_pool(flow)  # MAXPOOL1

                flow = build_layer(flow, 8, 16)  # CONV2_1
                flow = build_layer(flow, 16, 16)  # CONV2_2
                flow = self.layer_pool(flow)  # MAXPOOL2

                flow = build_layer(flow, 16, 32)  # CONV3_1
                flow = build_layer(flow, 32, 32)  # CONV3_2

                flow = tf.reshape(flow, [-1, 7 * 7 * 32])

                flow = self.layer_fc(flow, [7 * 7 * 32, 120], [120], relu=True)  # FC1
                self.dropout_prob = tf.placeholder('float')
                flow = tf.nn.dropout(flow, self.dropout_prob)  # Dropout
                flow = self.layer_fc(flow, [120, 10], [10], relu=True)  # FC2
                self.pred_y = flow = tf.nn.softmax(flow)  # Softmax

                # learning
                cross_entropy = -tf.reduce_sum(self.y * tf.log(flow))
                self.train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
                correct_predict = tf.equal(tf.argmax(flow, 1), tf.argmax(self.y, 1))
                self.accuracy = tf.reduce_mean(tf.cast(correct_predict, 'float'))

                # saver
                self.saver = tf.train.Saver()

        def train(self):
                sess = tf.InteractiveSession()
                sess.run(tf.global_variables_initializer())

                checkpoint = tf.train.get_checkpoint_state(os.path.dirname(__file__))
                if checkpoint and checkpoint.model_checkpoint_path:
                        self.saver.restore(sess, checkpoint.model_checkpoint_path)

                for i in range(20000):
                        batch = mnist.train.next_batch(50)
                        if i % 100 == 0:
                                train_accuracy = self.accuracy.eval(feed_dict={
                                        self.x: batch[0], self.y: batch[1], self.dropout_prob: 1})
                                print('step %d, training accuracy %g' % (i, train_accuracy))
                                self.saver.save(sess, self.prefix_path + './model.ckpt')
                        self.train_step.run(feed_dict={self.x: batch[0], self.y: batch[1], self.dropout_prob: 0.5})
                sess.close()

        def predict(self):
                sess = tf.InteractiveSession()
                sess.run(tf.global_variables_initializer())
                saver = tf.train.Saver(tf.global_variables())
                saver.restore(sess, self.prefix_path + './model.ckpt')
                print("test accuracy %g" % self.accuracy.eval(feed_dict={
                        self.x: mnist.test.images, self.y: mnist.test.labels, self.dropout_prob: 1}))
                sess.close()

        def read(self, input_image):
                sess = tf.InteractiveSession()
                sess.run(tf.global_variables_initializer())
                saver = tf.train.Saver(tf.global_variables())
                saver.restore(sess, self.prefix_path + './model.ckpt')
                output_number = self.pred_y.eval(feed_dict={self.x: [input_image], self.dropout_prob: 1})
                result = np.where(output_number == np.max(output_number))[1][0]
                sess.close()
                return result

        @property
        def prefix_path(self):
                return os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
        import input_data

        mnist = input_data.read_data_sets('data', one_hot=True)
        cnn = ResNet()
        cnn.build()
        # cnn.train()
        cnn.predict()
