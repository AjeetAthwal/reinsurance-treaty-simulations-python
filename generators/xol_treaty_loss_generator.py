from .loss_generator import LossGenerator

class XoLTreatyLossGenerator(LossGenerator):
    def __init__(self, generator, treaty):
        super().__init__(generator.parameters)
        self.generator = generator
        self.treaty = treaty

    def generate_loss(self):
        original_loss = self.generator.generate_loss()
        return self.treaty.apply_treaty(original_loss)

    def generate_losses_with_treaty(self, num_losses):
        gross_losses = self.generator.generate_losses(num_losses)
        net_losses = [self.treaty.apply_treaty(loss) for loss in gross_losses]
        return {'gross_losses': gross_losses, 'net_losses': net_losses}
