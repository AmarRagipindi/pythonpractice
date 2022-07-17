#Reversing the Lists
#Displaying the Lists in reverse Order
#Removing specified items from the List,Removing first and Last Items from the Lost
#Covert a string into list with comma delimiter
list1=["Amar",1.0,"Jyothi",1.1]
list2=[]
print(list1[::-1]) # just displaying in reverse order
list1.reverse() # Reversing takes place in the list
print(list1)
#Funtion to check if the list is empty or not
def empty_check(inlist):
    if len(inlist)==0:
        print('List is empty')
    else:
        print('List Not empty')
empty_check(list1)
empty_check(list2)
#Remove Item from List, Remove First and Last Item from List
list1.remove(1.1)
print(list1)
list1.append("dummy")
print(list1)
list1.pop()
print(list1)
list1.pop(1)
print(list1)
#Convert Comma Separated String to List
input_string=input("Enter the string you want to convert as a list(Use , as delimiter:")
list3=input_string.split(",")
print(list3)
