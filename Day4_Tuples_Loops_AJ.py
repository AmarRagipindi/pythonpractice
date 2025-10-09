#Amara Jyothi
# the input tuple contains the Trading price of the stock on a week
#find out the maximum profit a person can make by buying and selling a stock only one time in a week.
#Currently this is designed only for single digit numbers
#Input example : 34256 Ans: 4 reasom: third day price-5th day price
# this can be enhanced to take input of double digits separated by commas
s=input('Enter the prices of stock for the weekdays in order:')
r1=0
temp=0
buy_day=0
sell_day=0
while r1<len(s):
        c=s[r1]
        r2=r1+1
        while r2<len(s):
          if temp< int(s[r2])-int(c):
             temp=int(s[r2])-int(c)
             buy_day=r1
             sell_day=r2
            # print(s[r2],c,temp)
          r2=r2+1
        r1=r1+1
print(f"Maximum Profit: {temp}")
print(f"Buy on day {buy_day+1} at price {s[buy_day]}")
print(f"Sell on day {sell_day+1} at price {s[sell_day]}")





