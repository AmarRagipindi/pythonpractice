ln=input('Enter the length of Fibonacci series:')
c=1
prev_1=0
prev_2=1
print(prev_2)
while c < int(ln):
    curr = prev_1 + prev_2
    print(curr)
    prev_1=prev_2
    prev_2=curr
    c=c+1
