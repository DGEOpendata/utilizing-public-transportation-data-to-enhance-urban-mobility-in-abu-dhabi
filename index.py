python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Public_Transportation_Usage_2025.csv'
data = pd.read_csv(file_path)

# Processing the dataset
# Example: Calculate average number of passengers per route
average_passengers = data.groupby('Route')['Passengers'].mean()

# Visualizing the data
plt.figure(figsize=(10, 6))
average_passengers.plot(kind='bar')
plt.title('Average Passengers per Route in Abu Dhabi (2025)')
plt.xlabel('Route')
plt.ylabel('Average Number of Passengers')
plt.show()

# Further analysis can include peak times and monthly trends
# Peak usage times
peak_times = data['Time'].value_counts().nlargest(5)
print("Peak Usage Times:")
print(peak_times)

# Monthly usage trends
monthly_trends = data.groupby('Month')['Passengers'].sum()
plt.figure(figsize=(10, 6))
monthly_trends.plot(kind='line')
plt.title('Monthly Usage Trends')
plt.xlabel('Month')
plt.ylabel('Total Passengers')
plt.show()
