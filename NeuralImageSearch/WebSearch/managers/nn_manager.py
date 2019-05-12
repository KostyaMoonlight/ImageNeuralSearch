import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np
import os

class NNManager:
    def __init__(self, path2pb='siamese_model/OptimizedGraph.pb'):
        self.input_ph = 'import/inputs/anchor_ph:0'
        self.output_ph = 'import/siamese/output/Sigmoid:0'
        self.sess = tf.Session()
        with tf.gfile.GFile(path2pb, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            self.sess.graph.as_default()
            tf.import_graph_def(graph_def)
        self.input = self.sess.graph.get_tensor_by_name(self.input_ph)
        self.output = self.sess.graph.get_tensor_by_name(self.output_ph)

    def eval(self, data):
        data = np.expand_dims(data, axis=0)
        predictions = self.sess.run(self.output, feed_dict={self.input: data})
        predictions = np.squeeze(predictions)
        return predictions

if __name__=='__main__':
    data = np.random.rand(28, 28, 1).astype(np.float32)
    nn = NNManager('WebSearch\\managers\\Graph.pb')
   
    prediction = nn.eval(data)
    print(prediction)
