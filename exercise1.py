myage = None
myname=input("what is your name? ")

while myage is None:
    inputmyage=input("what is your age? ")
    try:
        myage=int(inputmyage)
    except ValueError:
        print(inputmyage,"is not a digit, please enter digits only")

gender = None
while gender not in {"male", "female" ,"non binary"}:
    gender = input ("Do you identify as male,female or non binary? ").lower()

for i in range(150):
    # print(i)
    if i==myage:
        print(f"Your name is {myname}, your age is {i} and you identify as {gender}.")
