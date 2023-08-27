from .loss_generator import LossGenerator
import random

class UniformLossGenerator(LossGenerator):
    def generate_loss(self):
        min_val, max_val = self.parameters['min'], self.parameters['max']
        return random.uniform(min_val, max_val)

