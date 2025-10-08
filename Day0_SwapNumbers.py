# Swap numbers using temporary variable
a = 10
b = 20
print("Value of a is ", a)
print("Value of b is ", b)

c = a
a = b
b = c
print("Value of a is ", a)
print("Value of b is ", b)

# Swap numbers without using temporary variable( Multiplication and Division)
a = 20
b = 40
print("Value of a is ", a)
print("Value of b is ", b)

a = a*b
b = a/b
a = a/b
print("Value of a is ", a)
print("Value of b is ", b)

# Swap numbers without using temporary variable( Addition and Subtraction)
a = 300
b = 400
print("Value of a is ", a)
print("Value of b is ", b)

a = a+b
b = a-b
a = a-b
print("Value of a is ", a)
print("Value of b is ", b)

