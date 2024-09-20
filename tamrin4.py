a = "*       amir \"\" mohammad      "
a = a.replace("*", "")
print(a.strip())

# x= (input("Enter namber :   "))
# x = float(x)
# print(type(x))
# if x >100 :
#     print(0.5)
# elif x < 100 :
#     print(1)
# else :
#     print(0)

# eig = input("Enter eig : ")
# eig = float(eig)
# massage= "bozorg sal" if eig > 60 else "biansal" 
# print(massage)

khosh_hesab_ya_bad_hesab = input("khosh hesab(1) ya bad hesab(2) : ")
if khosh_hesab_ya_bad_hesab == "1" :
    khosh_hesab_ya_bad_hesab = True
else:
    khosh_hesab_ya_bad_hesab = False

pool_dar_ya_bypool = input("Enter pool(1) dar ya by pool(2) : ")
if pool_dar_ya_bypool == "1" :
    pool_dar_ya_bypool = True
else: pool_dar_ya_bypool = False

print(khosh_hesab_ya_bad_hesab and pool_dar_ya_bypool)
if khosh_hesab_ya_bad_hesab and pool_dar_ya_bypool == True :
    print("vam dade shavad")
else: print("vam dade nashavad")

