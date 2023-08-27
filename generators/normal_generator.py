from .loss_generator import LossGenerator
import random
import math

class NormalLossGenerator(LossGenerator):
    def generate_loss(self):
        mean, standard_deviation = self.parameters['mean'], self.parameters['standardDeviation']
        u1, u2 = random.random(), random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        loss_value = mean + standard_deviation * z0
        return max(0, loss_value)