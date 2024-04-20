# variables for strings
#print("yaseen") # or print('yaseen')
#a='Islam'# or a="Mohamed"
#b='Mohamed'
#c=a+' '+b # or c='' # to add a space a+''+b
#print("yaseen "+c) #2
#print(a) #3
#print(b) #4
#print(c) #5
#print(type(a))
#import math
#import random

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
#ages=["yaseen","18","yahia","16","dan",'10',"daleen","10"]
#random.shuffle(ages)
#print(ages)
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
#a="yaseen islam"


#first_name=a[0:6].capitalize()
#last_name=a[7:12].capitalize()
#last_char=a[-1]
#print("first name is "+ first_name)
#print("last name is "+ last_name)
#print("last character  is "+ last_char)
#FUNCTIONS
#def #FUNCTION Name #():
# بيتم استخدام ال Fn عندما يتم استدعائها فقط ولا لازم اللي هبعته يكون ليه حاجه يتخزن
#def Yaseen():
 #   print("Hi Yaseen")
#for x in range(0,10):
 #   Yaseen()
#def YAS(Name,age,university):
   # print("# Your name is "+Name)
   # print("# Your AGE is " + str(age))
   # print("# Your university is " + university)
#YAS("Yaseen",18,"Alexu")
#def as():
  #  print("Your name is Yaseen")
#as("21") # bc the argument has no parameter in the header of the fn ملهاش حاجه اخزنها فيه
# RETURN STATEMENT used to return a value or an object to the caller
#def diff(Num_1,Num_2):
 #   return abs(Num_1-Num_2)

#print("the sum of 5 and 6 is "+str(diff(5,6)))
#def Nam(first_Name,Last_Name):
  #  print("Your first is "+first_Name)
   # print("Your second is "+Last_Name)
#Nam(first_Name="Yaseen",Last_Name="Islam")
#o/p :
#Your first is Yaseen
#Your second is Islam
# so keywords reduces the error percentage
#but
#def Nam(first_Name,Last_Name):
   # print("Your first NAME is "+first_Name)
   # print("Your last NAME  is "+Last_Name)
#Nam("Islam","Yaseen") # O/P:
#Your first NAME is Islam
#Your last NAME  is Yaseen
# so it is better to use the keywords
#nested function calls

#print("Your age is "+str(round(abs(float(input("What is your age?!"))))))

# هدخله -18.6 بس متنساش ان اي حاجه بترجع string فيحوله ل float هيخليه قيمه موجبه ب abs و بعد كده هيحوله اذا أمكن ب round و يطبعه ب print
 #SCOPE(LOCAL SCOPE(VARIABLE) VS GLOBAL SCOPE(VARIABLE))
#name="Yaseen" # Global variable
#def namee():
   # name="ISLAM" # local scope name will equal ISLAM inside the fn when we use it
  #  print(name)
#print(name) # Global scope o/p : Yaseen
#namee() # local scope  o/p :"ISLAM
# *args (method to return more than one argument )
#def name(*args):
  #  sum=0
   # for i in args :
  #      sum+=i
  #  return sum
#print((name(1,2,6,4,5))) o/p: 18
# same as tuple un changable
 # انا عاوز اغير العنصر في المكان الرابع
 # عشان تغير لازم تعمل casting لل tuple الي list و ال list يمكن تغيرها
#def summ(*sumee):
    #sum=0
    #sumee=list(sumee)
    #sumee[4]=7
    #for i in sumee:
      #  sum+=i
   # return sum
#print(summ(1,2,6,4,5)) #o/p=20
#def name(**kwargs): # first method
 #   print("Hello "+kwargs["first_name"]+" "+kwargs["last_name"]+" and your age is "+str(kwargs['age']))
#name(first_name="Yaseen",last_name="Islam",age=21)
#def dit(**kwargs):
   # print("HELLO ",end="")
  #  for value in kwargs.items():
  #      print(value)


#dit(first_Name="Yaseen",last_Name="Islam",age="18")
#a={"eg":"alex","eng":"lond"}
#for i,t in a.items():
   # print(i)
# Format  in only for strings
#{} place holder
#first format method
#print("the {} jumped over the {}".format("cow","moon"))
#second format method
#animal,item="cow","moon"
#print("the {} jumped over the {}".format(animal,item))
#Third format method (positional argument)
#print("The {0} jumped over the {1}".format("cow","moon"))#==print("The {0} jumped over the {1}".format(animal,item))
#Forth format method(keyword argyment)
#print("The {an} jumped over the {it}".format(an="cow",it="moon"))
#fifth format method (aleganta)
#item="the {} jumped over the {}"
#print(item.format("cow","moon"))
#print("My name is{:<10},nice to meet you".format("Yaseen")) # left a lined and make a space my name took 10 places
#print("My name is{:>10},nice to meet you".format("Yaseen")) #right a lined
#print("My name is{:^10},nice to meet you".format("Yaseen")) #centered a lined
#number_1=3.14567
#number_2=5000
##print("{:.2f}".format(number_1)) #o/p=3.15
#print("{:.3f}".format(number_1)) #o/p=3.146
#print("{:,}".format(5000)) # same as format(number_2)
#print("{:b}".format(number_2))
#print("{:x}".format(number_2))
#print("{:o}".format(number_2))
#print("{:e}".format(number_2))
# IMPORT RANDOM  انا عاوزه يطلعلي حاجه عشوائيه
#import random # lazeem
#print(random.randint(0,3))# randint require 2 arguments # generate integer numbers
#print(random.random()) # generate float numbers no arguments required
#my_list=["Yaseen","Dan",'Daleen','Yahia']
#print(random.choice(my_list)) # choose randomly (بيختار عشوائي مش بالترتيب )
#random.shuffle(my_list)
#print(my_list) # o/p : ['Daleen', 'Yaseen', 'Yahia', 'Dan']
#EXPECTIONS
#try:
#   num_1=int(input("num1= "))
#   num_2=int(input("num2= "))
 #  result=num_1/num_2
#except ZeroDivisionError as e:
 #   print(e)
  #  print("something went wrong ")
#except ValueError  as d:
  #  print(d)
  #  print("something went wrong ")
#else :
 #   print(result)
#finally:
   # print("Thank you !! ")
# file or folder ditection
#import os
#path="C:\\Users\\yi340\\OneDrive\\Desktop\\Ka"
#if os.path.exists(path):
  #  print("Found !!")
  #  if os.path.isfile(path):
    #    print("that is a file")
  #  elif os.path.isdir(path):
  #      print("that is a folder")
#else :
   # print("not exist !!")
#import os
#if os.path.exists("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"):
   #  print("Found!!",end="")
   #  if os.path.isfile("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"):
       #  print(" and a file  ")
    # if os.path.isdir("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"):
       #  print(" and a folder  ")
#else:
  #  print("Not Found!!")
# OPEN A FILE
#with open("dan.txt") as file:  # with open (fn) ("file name or location") as VAriable name :
                              # print(variable.read())   # to open a file
  #  print(file.read())
#print(file.closed) # to check if the file is closed or open \
#import os
#file="C:\\Users\\yi340\\OneDrive\\Desktop\\dan.tt"
#if os.path.exists(file) :
   #  print("FOUND",end="")
   #  if os.path.isfile(file):
        # print(", it is a file and it contains : ")
         #try:
            # with open("C:\\Users\\yi340\\OneDrive\\Desktop\\dan.txt") as file:
             #   print(file.read())
      #   except FileNotFoundError:
            #    print("file is not found ")
    # elif os.path.isdir(file):
         #print("and it is a folder ! ", end="")
#else:
  #  print("NOT FOUND :( !! ", end="")
#import os
#if os.path.exists("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"):
   # if os.path.isfile("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"):
       # print("Found and it is a file !!")
        #file="C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"
     #   with open (file) as file:
     #       print(file.read())
  #  elif os.path.isdir("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt"): # بص انا كده عملت ملف جديد
     #   print("Found and it is a folder !!")
#else:
  #  print("not Found")
#MAKE AND WRITE AND APPEAND ON A FILE
#with open  ("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt","a") as file :
 #   file.write("\nHI i am Dan thx ")
 # copying file by shutile
 # by COPY      # copyfile()+permisssion mode + dst can be a directory
 #    copyfile() # copy the contents of a file
 #    copy2()    # copy()+metadate(creation and modification time)
#import shutil
#shutil.copy("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt","C:\\Users\yi340\\OneDrive\\Desktop\\Android") #2 parameters srs,dst
# error عشان copy file بتعمل كوبي لالي جوه ال  ال file بس
#shutil.copy("C:\\Users\yi340\\OneDrive\\Desktop\\dan.txt","D:\\AUTOCAD")
#with open ("dan.txt","a")as file:
   # file.write("\nhii Yaseen")
#  MOVING  FILES import os and os.replace(srs,dst)
# import os
#destination="C:\\Users\\yi340\\OneDrive\\Desktop"
#source="C:\\Users\\yi340\\OneDrive\\Desktop\\Courses\\Cs50x"
#os.replace(source,destination)
#os.remove(file location) to remove a file
# خلي بالك ان موضوع ال folder بيحتاج access زي النقل بيبقي محتاج access
#import os
#try:
  #  os.remove("C:\\Users\yi340\\OneDrive\\Desktop\\ys.txt")
#except FileNotFoundError:
 #   print("FileNotFoundError")
#import os
#try:
 #   os.remove("C:\\Users\yi340\\OneDrive\\Desktop\\Sopranos")
#except OSError as e: o/p: Access is denied ( remove مينفعش امسح ملف مليان او اي ملف عموما ب )
  #  print(e)
# remove directory (empty only )
#import os
#try :
 #   os.rmdir("C:\\Users\yi340\\OneDrive\\Desktop\\Sopranos")
#except WindowsError as e: # The directory is not empty
  #  print(e)

#import os
#try :
 #   os.rmdir("C:\\Users\yi340\\OneDrive\\Desktop\\folder") # folder is an empty directory
#except WindowsError as e:
 #   print(e)
#import shutil
#import os
#try:
 #   os.remove("C:\\Users\yi340\\OneDrive\\Desktop\\test.txt")
  #  shutil.copy("C:\\Users\yi340\\OneDrive\\Desktop\\folder", "C:\\Users\yi340\\OneDrive\\Desktop\\Sopranos\\folder")

#except PermissionError as e:
   # print(e)
#except FileNotFoundError as e:
   # print(e)
# DELete an empty folder by rmdir
#try:
  #  os.rmdir("C:\\Users\yi340\\OneDrive\\Desktop\\folder")
#except OSError as e:
  # print("you are not supposed to use this function !!")
   # Remove a no empty file by shutile.rmtree
#try:
 #   shutil.rmtree("lab 5")
#except PermissionError as e :
    #print(e)

#try :
  #  shutil.copy("C:\\Users\yi340\\OneDrive\\Desktop\\Android\\Lab","C:\\Users\yi340\\OneDrive\\Desktop\\Lab")
#except PermissionError as e:
  #  print(e)  # Permission denied
#os.remove(path)  for files
#os.rmdir(path)   for empty folders
#os.rmtree(path)  for not empty folders
#modules : file comtain python code or functions or classess
#import python as py
#print(py.diff(5,6))
#import python
#print(python.plus(5,6))
#from python import diff,plus
#print(diff(6,8))
#from python import *
#print(plus(9,1))
#help("modules")  يطلع كل الfns الموجوده
#from game import *
#game()

#from QUIZ import *
#Quiz()
#from CLASS import Chips
#chip_1=Chips("chipse",1999,"cheese",10,"Medium")
#print(chip_1.make)# self.make=make (self == object name)
#print(chip_1.price)
#chip_2=Chips("Lion",1998,"LEMON",10,"Large")
#print(chip_2.volume)
#print(chip_2.flavor)
#chip_2.eat()
#chip_1.salary()
#chip_1.eat()
# Class variable Vs Instance variable
#Class variable found out of the construction  (variable shared between all objects from this Class)
# Instance variable (Variable inside the construction unique variable for one object )
#print(chip_1.paper) # Plastic
#print(chip_2.paper)   #palstic
#print(Chips.paper)   # plastic
#chip_2.paper="Glass" # يبقا بتاعت ال شيبسي التانيه بس اللي هتتغير
#print(chip_2.paper) # o/p: Glass
#print(chip_1.paper) # o/p: plastic
#print(Chips.paper) # o/p: plastic
#Chips.paper="ALUMINUIM"
#print(chip_2.paper) #ALUMINUIM
#print(chip_1.paper) #ALUMINUIM
#print(Chips.paper)  #ALUMINUIM
#chip_2.paper="Glass"
#Chips.paper="ALUMINUIM"
#chip_2  will not change if it changed already
#print(chip_2.paper) #Glass
##print(chip_1.paper) #ALUMINUIM
#print(Chips.paper)  #ALUMINUIM
#chip_2.eat()
#class Chips : # object name must be Capital
  #paper="Plastic"
  # FIRST attributes
  #def __init__(self,make,year,flavor,price,volume):
   # self.make=make
   # self.year=year    # Instance variable
   # self.flavor=flavor
   # self.price=price
   # self.volume=volume
  #SECOND methods(actions)
 # def eat(self):
   #   print(" taste Good!! :)")
  #def salary(self):
   #   print(str(self.price)+" Good Salary!!")
 # def furance(self):
   #   print("Can not be baked again !!")
# inheritance (Father and Son)
# class Animal :
 #   alive=True
 #   def eat(self):
    #    print("The Animal is eating")
  #  def sleep(self):
 #       print("The Animal is sleeping")


#class Lion(Animal):
 #  def people(self):
  #     print("The lion not eat people ")
#class Cat(Animal):
   # def meaw(self):
   #  print("the cat is meawooing")


#cat=Cat()

#cat.eat()
#lion=Lion()
#print(cat.alive)
#print(lion.alive)
#lion.sleep()
#lion.people()
#cat.eat()
#cat.meaw()
# multi-level inheritance
#class Organism :
#    alive=True
#class Human(Organism):
  #  def eat(self):
  #      print("He is eating !!")
#class Yaseen(Human):
 #   def  sex(self):
      #  print("He is a Male !!")
#Yaseen=yaseen=Yaseen()
#print(Yaseen.alive)
#yaseen.sex()
#yaseen.eat()
#Multiple inheritance
#class Prey:
  #      def flee(self):
 #           print("The animal is running !!")
#class Predator:
  #      def hunt(self):
 #           print("The animal is hunting !!")
#class Hawk(Predator):
  #      def fly(self):
 #           print("The Hawk is flying !!")
#class Fish(Predator,Prey):
  #      def swim(self):
 #           print("The Fish is swimming !!")
#class Rabit(Prey):
  #      def jump(self):
 #           print("The Rabit is jumping !!")
#rabit=Rabit()
#hawk=Hawk()
#fish=Fish()
#fish.hunt()
#fish.flee()
##fish.swim()
#hawk.hunt()
#hawk.fly()
#rabit.jump()
#rabit.flee()
# over WRITE method
#class Animal:
 #   def eat(self):
  #      print("this animal is eating!!")
#class Cat(Animal):
 #   def eat(self):
  #      print("Play!!")
#Animal=Animal()
#Animal.eat()
#Cat=Cat()
#Cat.eat()
#Method chaining
#class Car():
   # def turn_on(self):
   #     print("You turned on the engine!!")
   # def drive(self):
  #      print("You drive the car !!")
   # def brake(self):
  #      print("you are stopping the Car !!")
  #  def turn_off(self):
     #   print("You turned off the engine!!")

#car=Car()
#car.turn_on().drive().brake().turn_off() #o/p:AttributeError: 'NoneType' object has no attribute 'drive'
#we should return self

#class Car():
 #   def turn_on(self):
    #    print("You turned on the engine!!")
     #   return self
 #   def drive(self):
 #       print("You drive the car !!")
   #     return self
   # def brake(self):
   #     print("you are stopping the Car !!")
   #     return self
   # def turn_off(self):
    #    print("You turned off the engine!!")
    #    return self

#car=Car()
#method chainning
#car.turn_on().drive().brake().turn_off()

#O/p:
#You turned on the engine!!
#You drive the car !!
#you are stopping the Car !!
#You turned off the engine!!
#class Rectangle :
 #   pass
#class Square (Rectangle):
    #def __init__(self,width,length):
     #   self.width=width
  # #     self.length= length
   # def area(self):
    #    return self.width*self.length
#class Cube(Rectangle):
  #  def __init__(self,width,length,height):
   #     self.length=length
  ##      self.height=height
  #  def volume(self):
 #       return self.width*self.length*self.height

#rectangle=Rectangle()
#square=Square(3,3)
#cube=Cube(3,3,3)
#print(square.area())
#print(cube.volume())
# بدل التكرار في الكود هستخدم ال super method

#class Shapes:
 #   def __init__(self, length, width):
   #     self.width = width
  #      self.length = length


#class Square(Shapes):
   #   def __init__(self,length,width):
     #     super().__init__(length, width)
    #  def circumfrence(self):
      #    return self.length+self.width


#class Cube(Shapes):
   #   def __init__(self,length,height,width):
    #      super().__init__(length,width)
     #     self.height=height
     # def circumfrence_3d(self):
     #     return self.length+self.width+self.height
# Abstract classes
#class Vechile :
   # def go(self):
   #     pass


#class Car(Vechile):
#    def go(self):
  #      print("you drive the car ")


#class Motorcycle(Vechile):
  #  def go(self):
   #     print("you drive the car ")


#vechile=Vechile()
#car=Car()
#motorcycle=Motorcycle()
#vechile.go()  # ملهاش لازمه و مش عاوز المستخدم يستخدمها
#car.go()
#motorcycle.go()

# Abstract classes
#from abc import ABC,abstractmethod
#class Vechile(ABC) :
  #  @abstractmethod
  #  def go(self):
  #      pass
   # @abstractmethod
   # def stop(self):
   #     pass


#class Car(Vechile):
   #def go(self):
     #   print("you drive the car ")

  # def stop(self):
    #   pass
#class Motorcycle(Vechile):
  #  def go(self):
  #      print("you drive the car ")
  #  def stop(self):
  #      pass


#vechile=Vechile() #o/p :Can't instantiate abstract class Vechile with abstract method go
#car=Car()
#motorcycle=Motorcycle()
#vechile.go()  # ملهاش لازمه و مش عاوز المستخدم يستخدمها
#car.go()
#motorcycle.go()
# كده منعني اني اعمل object من ال vechile لانه ملهوش لازم
# passing objects as arguments
#from CLASS import Car,Motorcycle
#def change_color(vechile,color):
#    vechile.color=color
#car_1=Car()
#print(car_1.color)  #o/p: None
#change_color(car_1,"Red")
#print(car_1.color)  #o/p: Red
#bike=Motorcycle()
#print(bike.color)
#change_color(bike,"blue")
#print(bike.color)
#Warlus operator :=
#happy=True
#print(happy)
#print(happy:=True) #o/p=Ture
#print(happy) # كأني بعمل اسيمنت للحاجه و اطبعها فنفس الوقت
#foods=list()
#while True:
 #   food=input()
 #   if food=="quit":
 #       break
  #  foods.append(food)
#foods=list()
#while food:=input("What is your fav food ??!! ") != "quit":
 #   foods.append(food)
 # High order function that return a function
 #Ex_1
#def pri():
   # def prii():
  #      print("dwdweqdwq")
 #   return prii

#say=pri()
#say()  #o/p: dwdweqdwq
#Ex_2
#def divident(A):
    #def divisor(B):
   #    qoutient=A/B
  #     return qoutient
 #   return divisor


#divide=divident(10) # A=10 AND divide == divisor (assign function to a variable)
#print(int(divide(5)))


#def loud(text):

   # return text.upper()

#def quiet(text):

 #   return text.lower()


#def hello(fn):
  #  text=fn("YaseeN") # fn will do the same jon a s the loud function
 #   return text

#print(hello(loud))   # o/p:  YASEEN
#Lambda function  (Fn that has one expression and many arguments in one line )
#lambda arguments:expression
#def tas(x): # x is the argument

 #   return x*2 # expression in lambda


#print(str(tas(5))+"\n")

#tasc=lambda x:x*2
#print(tasc(6))

#add=lambda x,y:x+y
#multiply=lambda x,y:x*y
#qoutient=str(lambda x,y:x/y) # ERROR LAMBDA CANNOT BE CASTED
##qoutient=lambda x,y:x/y
#sub=lambda x,y:abs(x-y)
#print(add(4,5))
#print(multiply(4,5))
#print(str(int(qoutient(10,5))))
#print(sub(4,5))
#age_check=lambda age:True if age>=18 else False
#print(age_check(10))
#yaseen_check=lambda color:"this is Yaseen" if color=="Brown" else 'This is not Yaseen'
#print(yaseen_check("Brown")) # O/P: this is Yaseen
# sort method (lists only)
# sorted() function (iterables = (list or tuple) )
#list=["Ahmed","EZZ","Zyad","Yaseen"]
#list.sort()
#print(list)# o/p : ['Ahmed', 'EZZ', 'Yaseen', 'Zyad']

#for i in list:
#    print(i)
#tup=("EZZ","Ahmed","Zyad","Yaseen")

#tup_2=sorted(tup) # tup_2 is a list of tup bc sorted change tup to list

#for i in tup_2:
  #  print(i)

#list.sort(reverse=True)
#print(list)

#tup_2=sorted(tup,reverse=True)
#print(tup_2) # o/p : reversed as a list
 # list of tuples or tuples
#FAMILY=[('Yaseen',18,"Y"),('Islam',45,'P'),('Dan',10.5,'D'),("Ghada",42,"A")]
#age=lambda ages:ages[1]
#FAMILY.sort(key=age,reverse=True)

#for i in FAMILY:
 #   print(i)
#print("\n-------------------------\n")
#NAME=lambda name:name[0]
#FAMILY.sort(key=NAME) # كأني بقولك خد الحاجات اللي فالمكان زيرو لل tuples

#for i in FAMILY:
 #   print(i)

#last=lambda l:l[2]
#FAMILY.sort(key=last)
#print("\n-------------------------\n")
#for i in FAMILY:
 #   print(i)


# لو كلها tuple خلاص يبقي بال sorted


#students=(('AMR',"B",19),('omar',"A",20),('YASEEN',"A",18))
#students=("zx","aq",'ys')
#grade=lambda Grade:Grade[1]

#students_2=sorted(students,key=grade)
#students_2=sorted(students)
#print("\n-------------------------\n")

#for i in students_2:
 #  print(i)

#print("\n-------------------------\n")

#age=lambda age_2:age_2[2]

#students_3=sorted(students,key=age,reverse=True)

#for i in students_3:
 #   print(i)

#print("\n-------------------------\n")
#alpha=lambda a:a[0]
#students_3.sort(key=alpha)  # because students_3 already changed to a list in line 1159
#for i in students_3:
  #  print(i)

#map() applies a function to each item of an iterable
#map(function,iterable)


#Prieces = [("Jacket",25,33123),('shoes',36,232),('shirts',28,.233),('fliplop',15,2332)]
#to_SAR=lambda l:(l[0],l[1]*0.12) # l[0] tuple عشان ياخد اللي فالمكان زيرو بالنسبه بكل
#Prieces_SAR=map(to_SAR,Prieces) # now i saved changes in  a memory
#Prieces_SAR=list(map(to_SAR,Prieces))# now i saved changes to a memorye

#y=to_EGP(Prieces_SAR)


#print(Prieces_SAR)

#for i in Prieces_SAR:#o/p :('Jacket', 3.0)
  #  print(i)          #('shoes', 4.32)
                     #('shirts', 3.36)
                     #('fliplop', 1.7999999999999998) print(i)
#to_SAR2 = lambda l: ( l[1] ) # l[0] tuple عشان ياخد اللي فالمكان زيرو بالنسبه بكل
#Prieces_SAR = list(map(to_SAR2, Prieces))
#for i in Prieces_SAR:  # o/p :('Jacket', 3.0)
      #  print(i)  #O/P: 3.0
                  #4.32
                  #3.36
                  #1.7999999999999998
# IF L[2]    O/P: 33123
                # 232
                # 0.233
                # 2332


#Prieces=[("chips",5),("pricles",25),("us_chips",50)]
#priece=lambda p:p[1]
#Prieces.sort(key=priece)
#Prieces_SALARY=Prieces.sort(key=priece)  غلط عشان ان بعمل تعديل علي ال PRIECES
#Prieces_SALARY=Prieces
#for i in Prieces_SALARY:
#    print(i)
#def to_USD(l):
 #  return (l[0],l[1]*30)
#Y=to_USD(Prieces_SALARY)
#p_s=lambda i:(i[0],i[1]*30)
#priece_USD=list(map(to_USD,Prieces_SALARY))

#for c in  priece_USD:
#    print(c)
#print(priece_USD)
#nums=[5,2,9,8,4,8,7,6]
#def even(i):
 #   if i%2==1:
  #      return i+1
  #  else :
  #      return

#y=list(map(even,nums))

# filter fn
# filter(fn,iterable)

# Sort method one
#list_1=["Ya","AD",'pp',"kms"]

#list_1.sort()

#print(list_1) # o/p:  ['AD', 'Ya', 'kms', 'pp']

#list_1=["Ya","AD",'pp',"kms"]

#list_1_1=sorted(list_1)

#print(list_1_1)

# Sort method two

#list_2=("ks","ys","pp","ops")

# list_2.sort () wrong because .sort is for lists only

#list_2_2=sorted(list_2)

#print(list_2_2) # o/p: ['ks', 'ops', 'pp', 'ys']

# sort for iterable (list of tuples and tuple of tuples )

#list_3=[("Yaseen",18),('Islam',48),("Ghada",42)]

#name=lambda i:i[0]

#list_3.sort(key=name)

#print(list_3)

#def multiply(x):
#    return x*2

#nums=[5,4,16,9,16,19,20]

#nums=list(map(multiply,nums))

#print(nums)

#prieces=[("chips",20),("bake rolls",17),("doretos",63)]

#to_SAR=lambda i:i[1]*0.12

#prieces_SAR=list(map(to_SAR,prieces))

#print(prieces_SAR)

#def to_EGY(x):
  #  return (x[0],x[1]/0.12)

#prieces_EGY=list(map(to_EGY,prieces_SAR))

#print(prieces_EGY)


# filter function make a list from objects that aquire the conditions

#friends=[("Yaseen",18),("Islam",48),("Yahia",15),('dan',10),("daleen",10),('Ghada',42)]
#def friends_play(x):
# if x[1]>=18:
#    return True
#friends_play2=lambda i:True if i[1]>=18 else False

#friends_play_list=list(filter(friends_play2,friends))

#print(friends_play_list)


#reduce function it rquire to import functools
#import functools

#nums=[7,6,5,4,3,2,1]
#factorial=functools.reduce(lambda x,y:x*y,nums)
#print(factorial)


#yaseen=['Y','a','s','e','e','n']

#def name_fn(x,y):
  #  return x+y

#name=functools.reduce(name_fn,yaseen)
#print(name)

#students=[100,90,80,70,60,50,40,30,20,10,0]

#students_passed=list(filter(lambda i: i>60   ,students))

#print(students_passed)

# list comprehension

#students_passed=[i for i in students if i>60]

#print(students_passed)
#nums=[]

#for i in range(0,11) :
#    nums.append(i*i)

#print(nums)


# كأني بعمل ال fn , list في نفس الوقت

#nums_2=[i*i for i in range(0,11)]

#print(nums_2)

#names="yaseen"

#name=[i if i!="e" else "Failed" for i in names]

#print(name)

#unc=lambda i: print("yes") if i!=5 else print("i == 5")

#print(unc(5))
dic={"Alex":"Yaseen","Cairo":'Kareem'}
#value=dic['Cairo']
#print(value)
#for (key,value) in dic.items():
 #  print(key,value)

#cities_f={"NY":46,"Boston":75,"LA":50}
#dictionary={key: expression for (key,value) in iterable}

#cities_c={key:round(((value-32)/5)) for (key,value) in cities_f.items()}
#for (key,value) in cities_c.items():
 #  print(key,value)

#cities_temp_2={key:'Hot' for (key,value) in cities_f.items() if value>=50}

#print(cities_temp_2) # o/p: {'Boston': 'Hot', 'LA': 'Hot'}

#cities_weather={key:"sunny" if value>=50 else "cold" for (key,value) in cities_f.items()}

#print(cities_weather)
# zip function
# zip(*iteration) # aggregate iterables (one to the opposite one in the other program)
#usernames=["yaseen","islam","Ghada"]
#passwords=("yaso1980","taso19802005","Taso19802005@")

#args=zip(usernames,passwords)  o/p: address
#users=list(zip(usernames,passwords) )
#users=dict(zip(usernames,passwords) )
#for key,value in users.items():
# print(key+":"+value)

#import time

#time.sleep(5)
#print("hi")

# epoch الوقت اللي الكمبيوتر بدأ يحسب وقت منه بالثواني

#print(time.ctime(1000000000))  # return the time from epoch time until 1000000000 gone
#print(time.time()) # time from epoch until now in seconds
#print(time.ctime(time.time())) # my now date
#time_object=time.localtime()
#print(time_object) # now date but in detail #time.struct_time(tm_year=2023, tm_mon=9, tm_mday=5, tm_hour=12, tm_min=56, tm_sec=30, tm_wday=1, tm_yday=248, tm_isdst=1)
#local_time=time.strftime("%d:%b:%Y",time_object)
#print(local_time)  #05:Sep:2023

#local_time2=time.strptime(local_time,"%d:%b:%Y")
#print(local_time2)  #time.struct_time(tm_year=2023, tm_mon=9, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=248, tm_isdst=-1)
#time_tuple=(2022,9,5,4,30,0,0,0,0,0)
#time_tuple2=time.asctime(time_tuple)
#print(time_tuple2)

#.awk  tuple to seconds
# threading
#import threading
#import time
# multi threading == many tasks at the same time

#done=False
#def worker():
 #while not done:
  #   counter = 0
  #   time.sleep(1)
  #   counter+=1
  #   print(counter)

#x=threading.Thread(target=worker).start()
#input("what is your name ?!")
#done=True
#num=500
#print(f"{num}")


# to take multiple integres in one line
# map(int,input().split())
# to take multipe strs
#list(input().split())



#with open("file direction","r"or "w") as file # 'r'to read the file and "w' to write on the file  # as file is a nickname to use fn
    #file.write("needed things to be wrote")
    #num=file.read() # to make it allow to read but u should store3 it in a variable to display it
    #num.split # split ur text in a list with spaces  # we used the name of the variable we made not the file nickname


##mails = file.read()
  #  mails = mails.split()

#print(mails)