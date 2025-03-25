import polars as pl #importing polars library
import time #importing time module

start = time.time() # Start time

#loading the csv file into a polars dataframe
df = pl.read_csv("USAccidents2023.csv") #reading the csv file
print("Polars Load Time:", time.time() - start, "seconds") # Print the time taken to load the csv file


# Now using filtering to see how fast Polars can do it
severe_accidents = df.filter(pl.col("Severity") == 4)
print(severe_accidents.shape)  # Returns (rows, columns)
print(severe_accidents.height)  # Total count of severity 4 accidents
