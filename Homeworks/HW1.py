










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


  







