myage = None
myname=input("what is your name?")

while myage is None:
    inputmyage=input("what is your age?")
    try:
        myage=int(inputmyage)
    except ValueError:
        print(inputmyage,"is not a digits, please enter digits only")


for i in range(150):
    # print(i)
    if i==myage:
        print("Your name is",myname,"and Your age is",i)
