#method 1 with while loop

# user_input = int(input("How many rows you want to priint? : "))
# user_input2 = input("Enter 0/1('0' for down to up '1' for up to down): ")

# if user_input2 == "0":
#   i = 0
#   while i < user_input + 1:
#     print("*" * i)
#     i = i + 1

# elif user_input2 == "1":
#   i = 0
#   while i < user_input:
#     print("*" * user_input)
#     user_input = user_input - 1

# else:
#   print("wrong input!")




#method 2 with for loop
user_input = int(input("How many rows you want to print? : "))
user_input2 = input("Enter 0/1('0' for down to up '1' for up to down): ")

if user_input2 == "0":
  for i in range(1, user_input + 1):
    print("*"*i)
  
elif user_input2 == "1":
  for j in range(user_input, 0, -1):
    print("*"*j)
