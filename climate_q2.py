import matplotlib.pyplot as plt
import pandas as pd



import csv

years = []
co2_values = []
temperature_values = []


with open('climate.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists
    for row in csv_reader:
        year, co2, temperature = row
        years.append(int(year))
        co2_values.append(float(co2))
        temperature_values.append(float(temperature))

# figure and plot the data
plt.figure(figsize=(10, 5))

#  CO2 data
plt.subplot(2, 1, 1)
plt.plot(years, co2_values, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

# Plot temperature data
plt.subplot(2, 1, 2)
plt.plot(years, temperature_values, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

# Show the plot
plt.tight_layout()  # Ensures proper spacing between subplots
plt.show()