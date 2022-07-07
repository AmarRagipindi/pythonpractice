x = input('Enter the text or number:')
ln = len(x)
var = (ln - 1) / 2
c = 0
oob=0
while c <= var:
  # print('x[c] :',x[c])
  #  print('x[(ln-1)-c]:' ,x[(ln-1)-c])
   if x[c] == x[(ln-1)-c]:
    oob=oob+0
    c = c + 1
   else:
    oob=oob+1
    # print('oob',oob)
    c=c+1
if oob==0:
    print('Input is a Polyndrome')
else:
    print('Input is not a Polyndrome')
