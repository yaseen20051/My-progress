# variables for strings
#print("yaseen") # or print('yaseen') #1
#a='Islam'# or a="Mohamed"
#b='Mohamed'
#c=a+' '+b # or c='' # to add a space a+''+b
#print("yaseen "+c) #2
#print(a) #3
#print(b) #4
#print(c) #5
#print(type(a))
#import math

# variables for a string
#a=2005
#print(a)
#a+=5   increment and decrement as the c language
#print(a)
#c=b+10
#print(b)
#print(c)
#print(type(a))
# if a is a string like
#a="21"   it is a string
#print(a)  o/p:21
#print(type(a))  o/p:string type
#a="21"
#b=a+2  it will produce a error bc we cannot add astring to a integer
#a='18'
#print('Your age is '+a) # produce a error print statement should be the same type
#print('Your age is '+a) # or if a is a integer
#a=17
#print('Your age is '+str(a))# casting because donot forget that print statement must be the same type
 # float date type
#a=250.4
#print(a)
#print("Your height is : "+str(a)+"M"+" "+"yaseen islam")
# boolean date type  is a true or false date type
#a= True # it should be capital
#b= False # Capital letters
#print(b)
#print(type(a))
#print("I am Yaseen : "+str(a))
#multiple assigment
#a=21
#b="Yaseen"
#c=True
# we can use multiple assigment
#a,b,c=21,"Yaseen",True
#print(a)
#print(b)
#print(c)
# assigment multiple variables  at the same line
#a="Yaseen Islam"
#print(len(a)) # length of a character (just for a character )
#print(a.find('m'))
#a,n="yaseen yslam","2005"
#b,c="yaseenislam","YASEEN ISLAM"
#print(len(a)) # length of a character
#print(b.find('n')) #place of a character
#print(b.capitalize()) # capitalization only for the first character
#print(a.upper()) #o/p:YASEEN YSLAM capitalization for all the character
#print(c.lower()) #o/p:yaseen islam to small all the character
#print(a.isdigit()) # to check if the string contains letter (all the string should be numbers )
#print(b.isalpha()) # to check if all the sting places contain only charcters without spaces  o/p:true
#print(a.isalpha()) # o/p:False
#print(n.isdigit()) # o/p: True
#print(b.count("a")) # to count number of a specific character
#print(a.replace("e","r")) #to replace "e" with a "r"
#print(a*2) # to make multiple prints of one string
#a=2.5
#b='4'
#c=3

#print(b*3)#o/p:444
#print(int(b)*3)#o/p:12 # type one of casting (temporary)
#b=int(b)
#print(b*2)
#print(a*2) #o/p: 5.0
#print(int(a)*2) #bc 2.5 will be just 2# o/p: 4 temporary casting
#print(a) #o/p: 2.5
#print("my age is : "+str(a)) o/p:my age is : 2.5 it willnot be just
#a='Islam'+' '+"Mohamed"
#print(a) # we can use two varibles with the same name but here we took the last assigment
#like if we had acode consist of a=20 then a=70 and we did that print(a*2) the o/p will be 140
#ACCEPT USER INPUT
#a=input("What is your name : ") # # input take anything as a string even numbers
#b=int(input("What is your age : ")) # we made a casting process so we cannot accept float or a string it will produce a syntax error
#c=float(input("What is yor tall : "))
#b=b+1 # we cannot add str to int
# casting needed bc input take only strings
#print("Your name is : "+a)
#print("Your age is : "+str(b))
#print("Your tall is : "+str(c))
# I/P :What is your name : Yaseen Islam Mohamed
# I/P :What is your age : 18
#O/P
#Your name is : Yaseen Islam Mohamed
#Your age is : 18
#a=input("First Name : ")
#b=input("Last Name : ")
#c=int(input("Age :"))
#d=float(input("Tall : "))
#print("First Name : "+a)
#print("Last Name : "+b)
#print("Age : "+str(c)+" "+"years old")
#print("Tall :"+str(d)+"cm")
#MATH FUNCTIONS
#import math #be math contain all the mathematic fns
#a=2.6
#b=3.2
#c=4
#d=-2
#f=19
#print(round(a)) # i/p=2.6 o/p:3
#print(round(b)) # i/p=3.2 o/p:3
#print(math.sqrt(c)) # floor and ceil and sqrt inside the math file
#print(max(a,d,b)) # it can contain integers and floats together
#print(math.ceil(b))
#print(math.floor(b))
#print(abs(d))
#SLICING A STRING
#a="Yaseen Islam"  #12
# by using indexing[] method
# start
#name=a[0] #o/p: Y
#print(name)
# stop
#name=a[0:2]
#print(name) # o/p : Ya
#name=a[0:3]
#print(name) # o/p : Yas
#name=a[] #o/p: syntax error
#print(name)
# stop
#name=a[:2]
#print(name) # o/p : Ya it considerd index is zero
#name=a[0:]
#print(name) # o/p : Yaseen Islam it considerd stop  is 12
# step
#name=a[0:12:2]
#print(name) # o/p (Yse sa) it takes all the charcters in place 2
#name=a[0:6:]
#print(name) # o/p Yaseen
#name=a[0:6:1]
#print(name) # o/p Yaseen
#name=a[0:12:1]
#print(name) # o/p Yaseen Islam
#reversing a string
#name=a[::-1]
#print(name)  #o/p:malsI neesaY revercing should be without start and stop numbers
#name=a[::-1]
#print(name)  #o/p:nothing
#silcing method 2
#b="https://www.youtube.com"
#slice=slice(12,-4)
#slice=slice(0,-6)
#print(b[slice]) #o/p : youtube
#a="Yaseen Islam"

#print(a[slice]) #we cannot use two slice objects
#age=int(input("Please enter your age : "))
#if age==100 :
   # print("OLD")
#elif age>=18 :
    #print("adult")
#else :
   # print("kid")
#a=input("what is your name ? ")
#print(a)
#print(len(a))
#print(a.isdigit())
#print(a.isalpha())
#print(a.capitalize())
#print(a.upper())
#a=input("what is your name ? ")
#print(a.lower())
#a=input("what is your name ? ")
#print(a.replace('e','a'))
#print(a.count("e"))
#b=a[0]
#if b=="y":
 #   print('Yes')
#b=a[1]
#if b=="a":
 #   print("No")
#b=a[2]
#if b=="M":
 #   print("Yes")
#elif b=="N":
 #   print("No")
#else :
 #   print("Nothing")
#a=input("What is your name ? ")
#b=int(input("How old are you ? "))
#c=float(input("How tall are you ? "))
#print("Name : "+a)
#print("Age : "+str(b)+" "+"years old. ")
#print("Tall : "+str(c))
#a="https://www.google.com"
#slice=slice(12,-4)
#print(a[slice])
#a=int(input("first number : "))
#b=int(input("second number : "))
#c=a+b
#d=a*b
#e=a/b
#print("a*b= "+str(d))
#print("a+b= "+str(c))
#print("a/b= "+str(e))
#print(abs(-3))
#print(math.sqrt(4))
#print(math.floor(3.2))
#print(math.ceil(4.2))
#print(round(3.7))
#print(min(2,1,-4))
#a="yaseen islam"
#b=a[0:12:2]
#print(b)
#a="Yaseen"
#print(a*2)
#a="2"
#print(int(a)*3)
#a=int(input("Enter your age : "))
#if a>=18 and a<=50:
 #   print("you are allowed")
  #  print("you can enter the movie")
#elif not(a<18 and a >50):
 #   print("you are not allowed to join the movie")
  #  print("you cannot enter the movie")
#a=""
#while len(a)==0:
 #   a=input("Enter your name : ")

 #print("Hello "+a) # syntax error not the same line
#a = ""
#while len(a) == 0:
 #   a = input("Enter your name : ")

#print("Hello " + a)   # it will enter an infinite loop untill the name not equal "" then it will print if the input was a thing
#a = None
#while not (a):
 #   a = input("Enter your name : ")
#print("Hello " + a)  # evey single time it enters the loop it will print hallo + the user input مهما كان المستخدم مدخل ايه
#None == zero
#a=not (0)
#print(a)
#for i in range(10): # دايما بيطبع تنازلي
 #   print(str(i+1)+": yaseen")\
#for x in range(0,5):
  #  print(x)
 # same o/p as   for x in range(0,5,1):
                 #     print(x)
#for x in "YASEEN":
    # print("Y")  # the loop will be done 6 times  # هيطبع ال Y
#for x in "Yaseen Islam":
  #   print(x)  # هيطبع كل حرف لوحده
#import time
#for i in range(10,0,-1):
 #   print(i)
  #  time.sleep(2) # هياخد بين كل لووب و التاني ثانيتين
#print("Done")
 #a=int(input("Rows: "))
 #b=int(input("Cloumns: "))
 #symbol=input("Symbol")
#print("n", end="") # end="" prevent from doing a new line
#print("f")
#a=int(input("Rows: "))
#b=int(input("Columns: "))
#symbol=input("Symbol: ")
#for i in range(a):
 #   for j in range(b):
  #      print(symbol,end="")
   # print("")
#name=""
#while len(name)==0:
   # a=input("Name: ")
   # if a!="":
    #   break
#print(a)
#number="011-43-93-19-49"
#for i in number :
   #  if i=="-":
    #  pass # do nothing   كأني حاطط اوردر فاضي
    # else :
      #   print(i,end="")
# LIST == ARRAY
#a=["B","C","Y","A","G"]
#print(a)
#a.clear() # it will produce an error in the first loop  هو مش لاقي عناصر يمعلم
#a.sort()
#for x in range(0,5): # take care this loop made a logical error
 #   print(a[x]+" ",end="") # pop option will cause an error مفيش هنا حاجه اسمها garabage فيعمل ايرور هو مش لاقي اخر عنصر
#print("")
#for i in  a: # so this loop is preferable
#    print(i+" ",end="")
#2-D LIST
#islam=["YASEEN","YAHIA",'DAN','DALEEN']
#abdo=["GOUDY","KENZY",'LILE']
#shadi=["BELAL","MOHAMED",'GANA']
#mohamed=[islam,abdo,shadi]
#print(mohamed)
#print(mohamed[0]) # it will display list 0
#print(mohamed[0][1]) # list 0 of islam the element in place 1
#TUPLE for related, ordered and un changable date
#student=('Yaseen',18,'male')
#print(student[2])
#print(student.count("18")) # o/p zero bc  "18" is mentioned as a digit not a character
#print(student.count("Yaseen")) # o/p == 1
#print(student.index("Yaseen"))
#if "yaseen" in student:
 #   print("found")
#elif "Yaseen" in student:
   # print("@found")
#A=["DAN","DALEEN"]
#if  "DAN" and "sALEEN"  in A: # take care
#    print("found")
#else:
  #  print("not found")
#for x in student:
  #  if x==18:
  #   print(str(x)+' ',end="")
  #  else:
   #     print(x + ' ', end="")

  #  if x==18:
   # print(str(x)+' ',end="") # error if and print same line
#@#print(" Hello Yahia ;)" ")
#print("ALLAH")
#a=input("enter a name?!")
#print(a)
#a=input("enter your name : ")
#b=int(input("enter your age : "))
#c=float(input("enter your tall :"))
#print("your name is : "+a)
#print("your age is : "+str(b))
#print("your tall is : "+str(c))
#print(type(b))
#print(type(a))
#a="Yaseen Islam"
#b="yaseen"
#c="21"
#d='YASEENISLAM'
#print(b.capitalize())
#print(b.upper())
#print(b.lower())
#print(d.isalpha())
#print(c.isdigit())
#print(a.replace('e',"a"))
#print(b.count("e"))
#print(b.find("e"))
#a="yaseen"
#if a[0]=="y":
 #   print("TRUE")
#if a[1]=='A':
  #  print("false")
#if a[:3]=="yas":
#    print("yes")
#if a[3]=="a":
  #@  print("yes")
#elif a[3]=="e":
 #   print("no")
#a="YASEEN ISLAM"
#b=a[::-1]
#print(b)
#a="https://www.google.com/"
#slice=slice(12,-5)
#print(a[slice])
#import math
#a="Yaseen ISlam "
#t=1
#b=25.5
#c=-5
#d=a+t
#print(a)
#print(abs(c))
#print(round(2.7))
#print(math.sqrt(a))
#print(d)
#print(math.ceil(-2.2))
#print(math.floor(-2.2))
#for i in range (0,12,1):
 #   print(i,end="")
#for i in "Yaseen Islam ":
 #   print(i,end="")
#print("Mohamed")
#for i in range(0,10,2):
 #   print(i)
#a="yaseen"
#b=len(a)
#a=''
#print(len(a))
#while len(a)==0:
#    a=input("Enter your name: ")
#print("your name is : "+str(a))
#import time
#for i in  range (0,10):
# print(i,end="")
 #@     time.sleep(2)
#s=("yaseen",18,"engineer")
#print(s[])
#a=["yaseen","islam","18"]
#b=["mohamed","21"]
#c=[]
#print(c[1][1])#
#set (same as list but not ordered ,duplicate value ,unindexed مش مترتبه  )
#sets={"yaseen","islam","mohamed","islam"}
#a={"abdo","joudy","mohamed"}
#sets.add("21")
#sets.remove("islam")
#b=sets.union(a) # to union the sets together
#sets.update(a) # دخل كل ال a جوه ال sets

#for c in sets:
  # print(c)
#print(sets.difference(a))
#print(a.difference(sets))
#print(sets.intersection(a))
#DICTIONARY = {"KEY":"VALUE"}
ages={"yaseen":"18","yahia":"16","dan":'10',"daleen":"10"}
#a=input(" the person name : ")
#print(a+" age is "+ages[a])
#print(ages.get("islam"))
#o/p is none  اضمن عشان لو مش موجود ميطلعش للمستخدم ايرور
#ages.pop("yaseen")
#ages.update({"islam":"30"})
#print(ages.items())
#for i in ages: # it will print only the keys
   # print (i)
#ages.clear()
#for i in ages.items(): # it will print values and keys
 #  print (i)
#for values,keys in ages.items(): # it will print only the keys
  #  print (values,keys)
#x="racecaz"
#z=x[::-1]
#print(z)
#n=input("En
#a,b,c,f="18",18,False,"yaseen"
#print(f.find("e")) # يجيب اول واحده
#import math
#a=4
#b,c,d=19.5,-12,3.2
#print(math.ceil(d))
#print(math.sqrt(a))
#print(math.floor(d))
#print(abs(c))
#print(round(b))
#print(round(d)) #o/p=3
#print(max(a,b))
#print(min(c,b))
#a="yas"+"e"*2+"n"
#print(a)
#a=2*3
#print(a)
#print("yas"+"e"*2+"n")
#b=a[0:12:2]
#print(b)
#a="Yaseen Islam"
#b="https://www.youtube.com"
#slice=slice(12,-4)
#print(b[slice])
#b=["Dan",'DALEEN']
#c=[a,b]
#print(c[0][2])
#YASEEN=("Gender","age","relationship",'job')
#if "Gender" and "age" and "relationship" and "job"  in YASEEN :
  #  a =input("What is your gender ?!")
   # b = input("What is your age ?!")
   # c = input("What is your relationship statue ?!")
   # d = input("What is your job ?!")
#print("YASEEN is a "+a+" and he is "+b+" years old and "+c+"+"+d)
#a={"Egypt":'Cairo','USE':'RIYAD'}
#a.update({"Germany":"Berlin"})
#for x in a.items():
 #   print(x)
#print(a["Egypt"])
#print(a.get("Egypt"))
#print(a.get("wwdf")) o/p : none
#print(a["wwdf"]) o/p: error
# Index operator[]
a="yaseen islam"


first_name=a[0:6].capitalize()
last_name=a[7:12].capitalize()
last_char=a[-1]
print("first name is "+ first_name)
print("last name is "+ last_name)
print("last character  is "+ last_char)





