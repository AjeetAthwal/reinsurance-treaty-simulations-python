import random
import math

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

class NormalLossGenerator(LossGenerator):
    def generate_loss(self):
        mean, standard_deviation = self.parameters['mean'], self.parameters['standardDeviation']
        u1, u2 = random.random(), random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        loss_value = mean + standard_deviation * z0
        return max(0, loss_value)

class UniformLossGenerator(LossGenerator):
    def generate_loss(self):
        min_val, max_val = self.parameters['min'], self.parameters['max']
        return random.uniform(min_val, max_val)

class XoLTreaty:
    def __init__(self, attachment, limit):
        self.attachment = attachment
        self.limit = limit

    def apply_treaty(self, loss):
        capped_loss = min(loss - self.attachment, self.limit)
        return max(capped_loss, 0)

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

def calculate_results():
    # You can get input values from the command line arguments or user input
    # and create the generator and treaty instances accordingly.

    # For example:
    distribution_type = input("Distribution Type (normal/uniform): ")
    mean = float(input("Mean: "))
    standard_deviation = float(input("Standard Deviation: "))
    min_val = float(input("Min: "))
    max_val = float(input("Max: "))
    attachment = float(input("Attachment: "))
    limit = float(input("Limit: "))
    num_losses = int(input("Number of Losses: "))

    generator_parameters = {
        'mean': mean,
        'standardDeviation': standard_deviation,
        'min': min_val,
        'max': max_val
    }

    generator = NormalLossGenerator(generator_parameters) if distribution_type == 'normal' else UniformLossGenerator(generator_parameters)
    treaty = XoLTreaty(attachment, limit)
    xol_generator = XoLTreatyLossGenerator(generator, treaty)

    result = xol_generator.generate_losses_with_treaty(num_losses)

    # Display the results
    print("Results:")
    for index, (gross_loss, net_loss) in enumerate(zip(result['gross_losses'], result['net_losses']), start=1):
        print(f"Index: {index}, Gross Loss: {gross_loss}, Net Loss with XoL Treaty: {net_loss}")

if __name__ == '__main__':
    calculate_results()
