import matplotlib.pyplot as plt
from die import Die


# Model the dice
dice_one = Die(8)
dice_two = Die(8)

# Rolling die
results = []
for num_roll in range(1000000):
    result = dice_one.roll_die() + dice_two.roll_die()
    results.append(result)

# Analyse the results
frequencies = []
max_result = dice_one.num_sides + dice_two.num_sides
result_range = range(2, max_result+1)
for value in result_range:
    frequency = results.count(value)
    frequencies.append(frequency)

plt.style.use('seaborn')
fig, ax = plt.subplots()
# controls thickness of line plot
ax.scatter(result_range, frequencies, c=frequencies, cmap=plt.cm.inferno, edgecolor=None, s=10)

# Set chart title and label axis
ax.set_title("Dice Roll Two D8s 1 Million Times", fontsize=24)  # sets overall title for chart
ax.set_xlabel("Number Rolled", fontsize=14)  # controls font size on x axis (horizontal)
ax.set_ylabel("Frequency", fontsize=14)  # font size on vertical

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()
