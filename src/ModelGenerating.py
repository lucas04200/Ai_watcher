import tensorflow as tf

class ModelGenerating:
    def __init__(self, model_path):
        self.model = tf.saved_model.load(model_path)
        self.movenet = self.model.signatures['serving_default']