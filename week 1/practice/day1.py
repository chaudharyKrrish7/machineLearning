# Day 1
# Task 1: The Data "Janitor" (Comprehensions & Lambdas)
# You are given a list of messy "sensor data" strings. You need to clean it using only one line of code for each step.
# Python
# raw_data = ["  23.5 ", " 10.1", "error", "45.0", "  98.2 ", "NA", " 12.5"]

# Clean it: Use a list comprehension to strip the whitespace and remove any strings that are not numbers (like "error" or "NA").
# Transform it: Use the map() function and a lambda to convert the remaining strings into floats.
# Filter it: Use the filter() function and a lambda to keep only values greater than 20.0.

# Task 2: The Multi-Purpose Calculator (*args & **kwargs)
# Write a function called analyze_data that is flexible enough to handle any amount of input.
# It should accept any number of integers via *args.
# It should accept an optional keyword argument operation via **kwargs.
# If operation="sum", return the sum.
# If operation="mean", return the average.
# Bonus: If no operation is provided, default to returning the maximum value.

# Task 3: The "Model" Class (OOP Foundations)
# In ML, models are often structured as classes with fit and predict methods. Let's build a dummy version to practice your OOP.
# Create a class named SimpleStats:
# __init__: Should take a name for the model (e.g., "MyFirstModel") and store it.
# fit(data): Should take a list of numbers and store them as an attribute called self.history.
# predict(new_value): Should return True if the new_value is greater than the average of the self.history, and False otherwise.

#task 1
raw_data = ["  23.5 ", " 10.1", "error", "45.0", "  98.2 ", "NA", " 12.5"]

cleaned = [x.strip() for x in raw_data if x.strip().replace('.' , "" , 1).isdigit()] 
transformed  = list(map(lambda x: float(x) , cleaned))
filtered = list(filter(lambda x : x > 20.0 , transformed))


print(cleaned)
print(transformed)
print(filtered)

#task 2
def analyze_data(*args, **kwargs):
    operation = kwargs.get('operation')

    if operation == 'sum':
        return sum(args)
    elif operation == 'mean':
        return sum(args) / len(args) if args else 0
    else:
        return max(args) if args else None
    
print(analyze_data(1, 5, 48, operation='sgdfcvjgsd '))  

#task 3

class SimpleStats:
    def __init__(self, name):
        self.name = name
        self.history = []

    def fit(self, data):
        """Stores the training data history."""
        self.history = data

    def predict(self, new_value):
        """Returns True if new_value > average of history."""
        if not self.history:
            return False
        
        avg = sum(self.history) / len(self.history)
        return new_value > avg


model = SimpleStats("MyFirstModel")
model.fit([1, 2, 3])
print(model.predict(1))