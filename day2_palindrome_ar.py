# Not my creation. Copy and paste internet
# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]


# Driver code
while True:
    s = input("Enter the string")
    if s.__eq__("end"):
        break
    ans = isPalindrome(s)
    if ans:
        print("Yes")
    else:
        print("No")
