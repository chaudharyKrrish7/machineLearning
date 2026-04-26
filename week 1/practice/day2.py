# Day 2
#  Question 1: The Memory Duel (Generators)
# You are tasked with processing a range of 10 million integers (0 to 9,999,999).
# Part A: Create a List using [x for x in range(10000000)].
# Part B: Create a Generator Expression using (x for x in range(10000000)).
# The Test: Use the sys.getsizeof() function to find the memory size of both objects.
# Explanation Required: Why is the Generator's size so much smaller even though it can "access" the same amount of data?

# Question 2: The Data Cleaner (Error Handling)
# In Machine Learning, we often divide numbers to normalize data. However, datasets often contain zeros or invalid characters.
# The Task: Write a function safe_divide(numerator_list, denominator) that:
# Uses a try-except-finally block.
# Catches ZeroDivisionError if the denominator is 0.
# Catches TypeError if the denominator is a string.
# Uses the finally block to print "Division attempt finished" regardless of success or failure.
# Input to test: safe_divide([10, 20, 30], 0) and safe_divide([10, 20, 30], "2").

# Question 3: The Custom Iterator (OOP + Yield)
# Machine Learning batches are often custom-made.
# The Task: Create a class called BatchFetcher.
# The __init__ should take a large list of data and a batch_size.
# Create a method (or use __iter__) that yields a small "chunk" (batch) of the data at a time.
# Example: If data is [1, 2, 3, 4, 5, 6] and batch size is 2, it should yield [1, 2], then [3, 4], then [5, 6].


# task1
import sys

genlis = [x for x in range(10000000)]
print(sys.getsizeof(genlis))

genite = (x for x in range(10000000))
print( sys.getsizeof(genite)) 

#task2

def safe_divide(numList , denominator):
    try:
        result = [x / denominator for x in numList]
        return result
    except ZeroDivisionError:
        print("cannot divide by zero")
    except TypeError:
        print("denominator cannot be a string")
    finally:
        print("Division attempt finished")
    
safe_divide([10, 20, 30], 0)
safe_divide([10, 20, 30], "2")


# task 3

class BatchFetcher:
    def __init__(self , data , batch_size):
        self.data = data
        self.batch_size = batch_size

    def __iter__(self):
        for i in range(0 , len(self.data) , self.batch_size):
            yield self.data[i : i + self.batch_size]

batch = BatchFetcher([1, 2, 3, 4, 5, 6] , 2)
for b in batch:
    print(b)
