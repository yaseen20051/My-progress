counter_0=0
counter_1=0
counter_z=0
counter_e=0
counter_r=0
counter_o=0
counter_n=0
ones=[]
zeros=[]
check=1
char='w'
characters=[]
characters_nums=0
while characters_nums <= 2:
 try:
    characters_nums= int(input())
 except ValueError :
    characters_nums = int(input())

while(check):
 char=input("")
 for counter in range(characters_nums)  :
         if (char[counter]=="z"):
             counter_z=counter_z+1
             counter=counter+1
         elif (char[counter]=="e"):
             counter_e=counter_e+1
             counter=counter+1
         elif (char[counter]=="r"):
             counter_r=counter_r+1
             counter=counter+1
         elif (char[counter]=="o"):
             counter_o=counter_o+1
             counter=counter+1
         elif (char[counter]=="n"):
             counter_n=counter_n+1
             counter=counter+1

 if ((counter_z!=0) and (counter_e >= counter_z) and (counter_r >= counter_z) and (counter_o >= counter_z)):
       counter_0 =  counter_z
       counter_e = counter_e - counter_z
       counter_r = counter_r - counter_z
       counter_o = counter_o - counter_z
       counter_z=counter_z-counter_0
 if ((counter_n!=0) and (counter_o >= counter_n) and (counter_e >= counter_z)) :
         counter_1 = counter_1 + counter_n
         counter_o = counter_o - counter_n
         counter_e = counter_e - counter_n
         counter_n = counter_n - counter_1
 if (counter_z==0) and (counter_e==0) and (counter_r==0) and (counter_o==0) and (counter_n==0):
     check=0
 else:
     counter=0
     counter_0 = 0
     counter_1 = 0
     counter_z = 0
     counter_e = 0
     counter_r = 0
     counter_o = 0
     counter_n = 0

for counter_2 in range(counter_0):
    zeros.append(0)
counter_2=0
for counter_2 in range(counter_1):
   ones.append(1)

for counter_3 in ones:
    print(counter_3,end=' ')
counter_3=0
for counter_3 in zeros:
    print(counter_3,end=' ')