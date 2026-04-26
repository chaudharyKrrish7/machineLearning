# DAY5

# Task 1: Creating your first DataFrame
# Create a dictionary representing 5 of your favorite football players (Name, Team, Goals, and Value).
# Convert this dictionary into a Pandas DataFrame.
# Set the "Name" column as the Index.

# Task 2: Selection Mastery (loc vs iloc)
# Using the DataFrame from Task 1:
# Select the "Goals" of the 3rd player using .iloc.
# Select all data for "Manchester United" players (if any) using boolean indexing.
# Add a new column called "High Scorer" which is True if Goals > 15, and False otherwise.

# Task 3: Handling Missing Data (Intro)
# Create a Series with some np.nan (null) values.
# Use .isnull() to find them.
# Use .fillna(0) to replace them with zeros.

# task1
import numpy as np
import pandas as pd

players = {
    "Name": ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappé", "Kevin De Bruyne"],
    "Team": ["Paris Saint-Germain", "Manchester United", "Paris Saint-Germain", "Paris Saint-Germain", "Manchester City"],
    "Goals": [30, 25, 20, 28, 15],
    "Value": [100, 90, 80, 95, 85]
}

df = pd.DataFrame(players)
print(df)
df.set_index("Name", inplace=True)
print(df)


# task2
# goal = df.iloc[2]["Goals"]
goal = df.iloc[2,1]
print(goal)

manuts = df[df["Team"] == "Manchester United"]
print(manuts)

df["high scorer"] = df["Goals"] > 15
print(df)

# task3 
ser = pd.Series([1, 2, np.nan, 4, np.nan])
print(ser.isnull())
print(ser.fillna(0)) 