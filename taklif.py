#1

# my_string = input("enter my string :")
# count = input("Enter count :")
# count2 = count[0]
# print(f"number of characters of {count2!r} is {my_string.count(count2)} ")


#2

# my_string = "Enter number of characters of"
# print(len(my_string))
# print(len(my_string)-my_string.count(" "))

# my_string =input( """               *Enter String :""")
# caracters = len(my_string)
# kalamat = len(my_string) - my_string.count(" ")
# line = my_string.count("\n") + 1

# print(f"characters of string are {caracters!r} characters")
# print(f"kalamat of string are {kalamat!r} kalame")
# print(f"line of string is {line!r} lines")

my_string =input( """               *Enter String :""")
my_string = "\U00001570".join(my_string)
count = str(my_string.count("\U00001570")+1)
print(f"                my string has {count!r} characters")