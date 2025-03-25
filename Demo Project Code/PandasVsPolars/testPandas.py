import pandas as pd # Import pandas library
import time # Import time module for measuring execution time

start = time.time() # Start time

#load the csv file into a pandas dataframe
df = pd.read_csv("USAccidents2023.csv") #reading the csv file 
print("Pandas Load Time:", time.time() - start, "seconds") # Print the time taken to load the csv file

# Now using filtering to see how fast Pandas can do it
severe_accidents = df[df['Severity'] == 4]
print(severe_accidents.shape)  # Returns (rows, columns)
print(len(severe_accidents)) # Total count of severity 4 accidents







