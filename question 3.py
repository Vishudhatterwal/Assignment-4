import random
count=0
while count<10:
 a=random.randint(1,10)
 b=random.randint(1,10)
 print(a)
 print(b)
 c=a*b
 print('muliply' ,a ,'and', b)
 d=int(input('what is your answer'))
 if d==c:
   print('Right')
 else:
    print('Wrong','the correct answer is',c) 
 count=count+1 