double = lambda x : x * 2
add = lambda x , y : x + y
maxvalue = lambda x ,y: x if x > y else y
minvalue = lambda x ,y: x if x < y else y
ageChck = lambda age : True if age >= 18 else False

print(double(5))
print(add(5, 10))
print(maxvalue(5, 10))
print(minvalue(5, 10))
print(ageChck(20))