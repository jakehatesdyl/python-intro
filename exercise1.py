
def getNumberFromUser(passednumber,question):
    while passednumber is None:
        inputmyage=input(question)
        try:
            passednumber=int(inputmyage)
            return(passednumber)

        except ValueError:
            print(inputmyage,"is not a digit, please enter digits only")

myname=input("what is your name? ")


myage = None
question="What is your age?"
myage=getNumberFromUser(myage,question)

eyes = None
question = "How many eyes do you have?"
eyes=getNumberFromUser(eyes,question)

gender = None
while gender not in {"male", "female" ,"non binary"}:
    gender = input ("Do you identify as male,female or non binary? ").lower()


print("you have",eyes,"eyes")
print("Your age is",myage)