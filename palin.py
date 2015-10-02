# input = raw_input('Prompt:')
# print "The entered Value:" +(input)
# print type(input)

# Program to check if a string
#  is palindrome or not

# take input from the user
my_str = raw_input("Enter a string: ")

# make it suitable for caseless comparison
my_str = my_str.lower()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")

# if __name__ == "__main__":
# 	print "hello"