
# print(y1.find("."))

# print(len(y2))

# spaese = a*" "

# print(str(y1[0]))
# # print(int(my_namber.find(str(y1[0]))))
# a1 = int(my_namber.find(str(y1[0]))) -1
# print(a1)
# print(type(my_namber))str
# new_my_namber = my_namber.replace(my_namber[:3] ,my_namber[a1] )

# y = input("Enter name(y): ")
# y1 = str(y)
# y = float(y)
# y2 =str(y1[:3])
# a = 25-len(y2)
# my_namber = "y = %25.3f" % y
# new_my_namber = a*" " +"y = " + my_namber[my_namber.find(str(y1[0])):]
# print(new_my_namber)


# a = 25
# print("the number is :{0:>+10d}".format(a))

#a = {10}
# a = 10
# print(f"a = {{{a}}}")

# import datetime

# today = (datetime.datetime.now())
# print(f"today is {today:%y / %M(%b) / %d(%A)}".format(today))

# my_string = "my string is"
# print(my_string.count("m"))
#23
my_string = " my a"
my_string = "\U00001570".join(my_string)
# print(my_string.split())
count = (my_string.count("\U00001570"))
count = (count) + 1
count = str(count)
# print(ord("آ")) #1570
# print("\U00001570")
print(f"my string has {count!r} characters")