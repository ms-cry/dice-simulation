import numpy as np
import matplotlib.pyplot as plt

# simulate dice rolls
rolls = np.random.randint(1,7,10000)

# count occurrences
counts = np.bincount(rolls)[1:]

# calculate probability
probabilities = counts / len(rolls)

# dice faces
faces = np.arange(1,7)

print("Counts:", counts)
print("Probabilities:", probabilities)

# plot
plt.bar(faces, probabilities)

plt.axhline(1/6, color='red')

plt.xlabel("Dice Face")
plt.ylabel("Probability")
plt.title("Experimental vs Theoretical Probability")

plt.show()