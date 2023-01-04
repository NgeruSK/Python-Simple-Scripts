print("hello world")

print("*" * 10)


x = input("Enter your name : ")

y = input("Enter your age : ")

if bool(x) and bool(y):
    if int(y) >= 18:
        print("you grown up "+x)
    else:
        print("you kiddo " + x)
else:
    print("all parameters needed")
