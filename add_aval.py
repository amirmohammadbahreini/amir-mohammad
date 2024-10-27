while True :
    a = int(input("enter your namer>>>>"))
    if a==1 or a ==0:
        print(f"{a} is not aval and not morakab")
    elif a!=1 or a!=0:
        for i in range(2,a):
            if a%i==0 :
                print(f"{a} is not aval")
                break
        else:
            print(f"{a} is aval")
    print('\n',20*"**",'\n')