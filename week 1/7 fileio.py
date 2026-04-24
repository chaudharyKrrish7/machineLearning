import os
# f = open("demo.txt" , "w+")
# # data  = f.read()
# # data  = f.readline ()
# # data1  = f.readline ()
# # print(data)
# # print(data1)

# f.write("i am good")
# f.seek(0)  # Move the file pointer to the beginning                                                                                    
# data = f.read()
# print(data)
# f.close()    
        
# # # os.remove("demo.txt")  # Remove the file after use

# with open("demo.txt", "r") as f:
    

#     data = f.read()
    
# newData = data.replace("i", "ronaldo")
# print(newData)

# with open("demo.txt", "w") as f:
#     f.write(newData)

with open("demo.txt", "r") as f:
    data = f.read()

    if "Hi" in data:
        print("Found in the file.")
    else:
        print(" not found in the file.")

