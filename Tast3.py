import pandas as pd

# Read the dataset.
data = pd.read_csv("c:/Users/Lenovo/Downloads/motor_insure.csv/motor_data11-14lats.csv")

# Inspects its column by displaying the first 10 records.

print(data.head(10))
# Display records for make and usage for sets_num that are more than 40.
#print(data[data['sets_num']>40][['make','usage']])

# Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axis

import matplotlib.pyplot as plt

plt.plot(data['EFFECTIVE_YR'], data['CARRYING_CAPACITY'])
plt.ylabel('EFFECTIVE_YR')
plt.xlabel('CARRYING_CAPACITY')
plt.title('EFFECTIVE YEAR vs CARRYING_CAPACITY')
plt.show()