givenNumber = int(input("Enter a number"))
num1 = 0
num2 = 1
num = 0
while givenNumber > 0:
    print(num)
    num = num1 + num2
    num1 = num2
    num2 = num
    givenNumber = givenNumber - 1