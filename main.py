import matplotlib.pyplot as plt

def read_data(file_name):
    length_errors = []
    total_energies = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split(',')
            length_error = float(parts[0].split(':')[-1].strip())
            total_energy = float(parts[1].split(':')[-1].strip())
            length_errors.append(length_error)
            total_energies.append(total_energy)
    return length_errors, total_energies

# Read data from files
length_errors_1, total_energies_1 = read_data('condition_1.txt')
length_errors_10, total_energies_10 = read_data('condition_10.txt')
length_errors_100, total_energies_100 = read_data('condition_100.txt')

# Plot data
plt.figure(figsize=(10, 6))
plt.plot(total_energies_1, label='1 Relaxation Step', color='red')
plt.plot(total_energies_10, label='10 Relaxation Steps', color='blue')
plt.plot(total_energies_100, label='100 Relaxation Steps', color='green')

# Setting labels and title
plt.xlabel('Time (in units of Δt = 0.05)')
plt.ylabel('Total Energy')
plt.title('Total Energy over Time with Δt=0.05 and No Sub-stepping')
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
