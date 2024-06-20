# CAGR Calculation

# Given data points
data_points = [515.10, 654.17, 848.99, 973.79, 1181.49, 1387.07, 1289.98, 1302.88, 1450.37, 1614.55]

# Number of periods (years) is the count of data points minus one
n = len(data_points) - 1

# Beginning value
beginning_value = data_points[0]

# Ending value
ending_value = data_points[-1]

# Calculate CAGR
CAGR = ((ending_value / beginning_value)**(1/n)) - 1
print(CAGR)
