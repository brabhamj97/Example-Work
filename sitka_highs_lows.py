from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


# path reference to our text file
path = Path('weather_data/sitka_weather_2021_simple.csv')
# read the text file and split into individual lines
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high and low temps
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# styling plot
ax.set_title("Sitka, Daily High & Low Temperatures 2021", fontsize=18)
ax.set_xlabel('', fontsize=16)
# draws date values diagonally to stop them overlapping
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=10)
plt.ylim(10, 120)

plt.show()


