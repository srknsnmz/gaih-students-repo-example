#QUESTION1

NumList = []
 
Number = int(input("How many elements in list :- "))
 

while ( Number%2 != 0 ):
   print("This program will not accept odd number.")
   Number = int(input("How many elements in list :- "))
   break
 
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element :- " %i))
    NumList.append(value)
 
num = int(Number/2)
 
list1 = NumList[:num]

list2 = NumList[num:]
 
swapList = list2 + list1


print(num)
print("list : ",NumList)
print("list1: ",list1)
print("list2: ",list2)
print(swapList)


#QUESTION2
 
Number = int(input("Please enter a single digit integer: "))
 

while ( Number < 0 or 10 <= Number ):
   print("please enter a single digit integer between 0 and 9 ")
   Number = int(input("Please enter a single digit integer: "))
   exit()

MyList = list(range(Number + 1))
print(MyList)
 

evenList = []

for i in range(Number+1):
  if MyList[i] % 2  == 0:
    evenList.append(MyList[i])
  exit()

print(evenList)


  







