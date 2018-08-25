#This is the first simple project
#Take user name, age, batch as input
#Display the three outputs in a single line as:
# <username> is <age> years old and is in batch of <batch> .

print("Enter Name:")
name = input()
print("Enter Age:")
age = int(input())
print("Enter Batch Year:")
batch = int(input())
print(name + " is " + str(age) + " years old and is in batch of " + str(batch))

#Explicit definition of str is done for age and batch as they are integer variables
#Addition of an integer to a string doesnt make sense
#name variable however can be simply added to the rest of the string as it takes in standard input which is a string

