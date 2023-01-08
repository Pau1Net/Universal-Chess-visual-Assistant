import tensorflow as tf
import numpy as np

def get_model_paths():
    return ['../model/model.pb', join(dirname(__file__), 'model.pb')] #model.pb - trained chess model.

def load_graph(frozen_graph_filepath):
    with tf.io.gfile.GFile(frozen_graph_filepath, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name="tcb")
    return graph

def predict_pieces(model, tiles):
    validation_set = np.swapaxes(np.reshape(tiles, [32*32, 64]), 0, 1)
    guess_prob, guessed = model.sess.run(
        [model.probabilities, model.prediction],
        feed_dict={model.x: validation_set, model.keep_prob: 1.0})
    return guess_prob, guessed

def construct_fen(guess_prob, guessed, active):
    certanty = np.array(list(map(lambda x: x[0][x[1]], zip(guess_prob, guessed))))
    certainty = certanty.reshape([8, 8])[::-1, :]
    certanty = certanty.min()

    label_index_to_name = lambda label_index: ' KQRBNPkqrbnp'[label_index]
    piece_names = list(map(lambda k: '1' if k == 0 else label_index_to_name(k), guessed))
    fen = '/'.join([''.join(piece_names[i*8:(i+1)*8]) for i in reversed(range(8))])

    castling = get_castling_status(fen)
    if active == 'b':
        fen = unflip_fen(fen)
    fen = shorten_fen(fen)

    fen = '{} {} {} - 0 1'.format(fen, active, castling)
    return fen, certanty

class Board():
    def __init__(self, frozen_graph_paths=get_model_paths()):
        try:
            graph = load_graph(frozen_graph_paths[0])
        except Exception:
            graph = load_graph(frozen_graph_paths[1])
        self.sess = tf.compat.v1.Session(graph=graph)
        self.x = graph.get_tensor_by_name('tcb/Input:0')
        self.keep_prob = graph.get_tensor_by_name('tcb/KeepProb:0')
        self.prediction = graph.get_tensor_by_name('tcb/prediction:0')
        self.probabilities = graph.get_tensor_by_name('tcb/probabilities:0')

    def recognize_pieces(self, img, active):
    tiles, corners = find_grayscale_tiles(img)
    if tiles is None or len(tiles) == 0: return None, None

    guess_prob, guessed = predict_pieces(self, tiles)
    fen, certanty = construct_fen(guess_prob, guessed, active)
    return (fen, list(corners)) if certanty > .9 else (None, None)
  
    def close(self):
        self.sess.close()

