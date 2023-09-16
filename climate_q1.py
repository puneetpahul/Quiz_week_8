import matplotlib.pyplot as plt
import sqlite3

# Connect to the database
connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

# Fetch data from the database
cursor.execute("SELECT Year, CO2, Temperature FROM climateData")
data = cursor.fetchall()



# data to be inserted or updated
data_to_insert = [
    (1950, 250, 14.1),
    (1960, 265, 15.5),
    (1970, 272, 16.3),
    (1980, 260, 18.1),
    (1990, 300, 17.3),
    (2000, 320, 19.1),
    (2010, 389, 20.2)
]

for year, co2, temperature in data_to_insert:
    cursor.execute("SELECT Year FROM climateData WHERE Year=?", (year,))
    existing_data = cursor.fetchone()

    if existing_data:
        # Update existing data
        cursor.execute("UPDATE climateData SET CO2=?, Temperature=? WHERE Year=?", (co2, temperature, year))
    else:
        # Insert new data
        cursor.execute("INSERT INTO climate_data (Year, CO2, Temperature) VALUES (?, ?, ?)", (year, co2, temperature))

# Commit the transaction
connection.commit()



# Close the database connection
connection.close()




        
years = []
co2 = []
temp = []
for row in data:
    year, co2_val, temp_val = row
    years.append(year)
    co2.append(co2_val)
    temp.append(temp_val)

# Plotting
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

# Save the figure before showing
plt.savefig("co2_temp_1.png")

# Show the plot
plt.show()
