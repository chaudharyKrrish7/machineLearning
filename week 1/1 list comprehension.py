print("hello world")           
triples  = [y * 3 for y in range (1,11)]
print(triples)

fruits = ["apple" , "banana" , "coconut"]
fruits = [fruits.upper() for fruits in fruits]
fruit_char = [fruits[0] for fruits in fruits]
print(fruit_char)
print(fruits)


num = [1,2,-3,4,-5,-6,7,-8,9]
evenNum = [num for num in num if num % 2 == 0]
oddNum = [num for num in num if num % 2 != 0]
posNum = [num for num in num if num >= 0 ]
negNum = [num for num in num if num < 0 ]

print(evenNum)
print(oddNum)
print(posNum)
print(negNum)   


grades = [33, 45 , 67 , 12 ,  23 , 45 , 89 , 90 , 34 , 56]
passedGrades = [grades for grades in grades if grades >= 33]
print(passedGrades)
