# a = input("enter a number: ")
# print ("the table of {a} is: ")
# try:
#     for i in range(1 ,3):
#         print (f"{a} x {i} = {int(a)*i}")
# except ValueError as e:
#     print ("some errror occured: ", e)

# print ("the program continues...")

try : 
    a  = int(input("enter a number: "))
    b = [3,5,6]
    print (b[a])

except ValueError as e:
    print ("invalid integer input" , e)

except IndexError as e:
    print ("index out of range" , e)

