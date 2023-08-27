class LossGenerator:
    def __init__(self, parameters):
        self.parameters = parameters

    def generate_loss(self):
        raise NotImplementedError("generate_loss method must be implemented in subclasses")

    def generate_losses(self, num_losses):
        losses = []
        for _ in range(num_losses):
            losses.append(self.generate_loss())
        return losses