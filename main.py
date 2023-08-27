from generators.normal_generator import NormalLossGenerator
from generators.uniform_generator import UniformLossGenerator
from generators.xol_treaty_loss_generator import XoLTreatyLossGenerator
from treaties.xol_treaty import XoLTreaty

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
