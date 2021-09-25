# import cv2
# import math
# print("hello python")       # comments not allowed here run thr code after removing comments. //  hello python 
# print(9-0)                           #9              # is single line comment 
# print("9-0")                            #9-0
# print("yes")                  # can also make comment by pressing control+/ and vice versa
''' this is multiline comment   '''
# print(math.gcd(7,14))

# a=10
# b="anju"
# c=89.7
# print(b)         # output: anju
# print(a+10)       # output: 20
# print(a+c)
# arithmetic operators
# print(a+c)
# print(a-c)
# print(a*c)
# print(a/c)
# print(a%c)
#increment operator  not available here
# print(a+1)
# print(a)
#variable: variable is an simply a container which is used to store the data and its value always gets changed during the execution of the program.
# mera variable=45      gives invalid syntax
''' rules for declaring valid syntax variable  
1. a variable should start from letter or underscore.
2. variable can't be start from a number.
3. it can only contain alphanumeric character(A,a to z,Z and 0-9)
4. variable names are case sensitive means Harry and harry are two different variables.
5. variable's value can overwrite also.

'''
# typeA=type(a)  #its an function that tells the type of the variable.
# print(typeA)
# typeB=type(b)  #its an function that tells the type of the variable.
# print(typeB)
# r=56
# print(r)   # 56 is as integer value
# r="56"
# print(r)         # here 56 is as string value
''' here not any problem both are printing the 56 without any problem 
    but problem comes when we add the number in  r which is string type
    then it will gives an error to us. '''

# print (r+2)       provide error a string cannot be add with the integer value
# c=int(r)                    #typecasting
# print(c+2) 
# e=int("45")              #typecasting can from string to integer
# f=float(45)              #typecasting can from integer to float
# g=str(45)                #typecasting can also be from integer to string
# print("the value of e is:", e )
# print("the value of f is:", f )
# print("the value of g is:", g )
# print(type(e))
# print(type(f))
# print(type(g))

#STRINGS

# name="Anju"
#print(name)            #prints Anju
# name = 'Anju'
# print(name)             #prints Anju no difference
# name = "anju is a good girl"                # it is single line string
# print(name)                            #prints anju is a good girl

# name= '''ANJU 
# IS A GOOD GIRL'''             #it is multiline string  
# print(name)                     #prints   '''ANJU 
#                                        #       IS A GOOD GIRL''' 

# name ="anju
# is a good girl"
# print (name)                #provides error
# name="Anju"
# print(name[0])                 #gives A
# print(name[0:2])                #gives An      last wala character count nhi krta
# name="       anju                 "             
# print(name)                                   its gives        anju                  the output
# name ="         anju                           "
# print (name.strip())                      stip is a function which simply neglect the spaces from the string.
# name ="hello      anju"
# # print(name)              #prints same as we have given 
# # print(name.strip())            '''this will print by without any space no wrong it willl print the same 
# # it can only work in one word string. '''
# print(len(name))                #  gives the length of the string 15
# var="ANJU"
# print(var.lower())             #converts the string into the lower case
# print(var.upper())             #converts the string into  the upper case
# print(var.replace("A","G"))          #prints the GNJU


# namesvar="ANJU, ADITYA, SRISHTI"
# print(namesvar.replace(","," "))         # prints ANJU  ADITYA  SRISHTI
# print(namesvar.replace(",","|"))          #prints ANJU| ADITYA| SRISHTI
# print(namesvar.replace(",", "\n"))         
# '''prints ANJU
#            ADITYA
#            SRISHTI'''
# print(namesvar.replace(", ", "\n"))         
# '''prints ANJU
#           ADITYA
#           SRISHTI'''
# namesvar= "ANJU IS ALSO "
# namesvar2= "ADITI"
# # print(namesvar+namesvar2)           # prints ANJU IS ALSO ADITI
# print(namesvar + namesvar2)           # prints ANJU IS ALSO ADITI

# var1="anju"
# var2="aditya"
# # # print("this is {} and she is elder sister of {}".format(var1,var2))     same work 
# # temp= "this is {} and she is elder sister of {}".format(var1,var2)         
# # print(temp)            # same work  output:  this is anju and she is elder sister of aditya
# # temp=("this is {} and he is younger brother of {}".format(var2,var1))
# # print (temp)                        #this is aditya and he is younger brother of anju
# # temp= "this is {0} and she is elder sister of {1}".format(var1,var2)        #bydefault value and print linewise
# # temp= "this is {1} and she is elder sister of {0}".format(var1,var2)        #this will reverse the names
# # print(temp)                #prints this is aditya and she is elder sister of anju
# temp= f"this is {var2} and this is {var1}"         #it also do the same thing
# print(temp)                                    #  prints this is aditya and this is anju

'''QUIZ:
TRY SOME OPERATORS ARE:
1. ** Exponentiation operator
2. // floor value division
3. modulo operator
'''
# num1=2
# num2=3
# print(num1**num2)          # it will put the 3 to the top of 2 so that after open it will become the 8.
# print(num2//num1)         #1
# print(num2%num1)            #1


#note:alt+arrow keys is helpful to move the line
'''
python collection : 1. list
 2. tuple
 3. set
 4. dictionary

'''
#list : 

#list and [array in other languages] are ordered and changable.
# list=['amrud','onion','burger','maggy','namkeen','biscuit']
# print(list)             #prints ['amrud', 'onion', 'burger', 'maggy', 'namkeen', 'biscuit']
# print(type(list))          #prints <class 'list'>
# print(list[1])            #prints onion this is called slicing
# print(list[3])              #maggy
# print(list[1:5])            # ['onion', 'burger', 'maggy', 'namkeen']
# list[1]='pau bhajhi'
# print(list[1])                 #it can changable also
# print(list)                          #['amrud', 'pau bhajhi', 'burger', 'maggy', 'namkeen', 'biscuit']
# print(len(list))                      #6
# listy=['','','allu']
# print(listy)                    #  ['', '', 'allu']

# print(list+listy)              #['amrud', 'onion', 'burger', 'maggy', 'namkeen', 'biscuit', '', '', 'allu']
# listy=['','','allu','amrud','onion','biscuit']
# print(list-listy)               #minus is not allowed here
# listy.append('kurkure','chips')           # it says append takes only one argument, only add at the end of the list
#listy.append('kurkure')                
#print(listy)                               #['', '', 'allu', 'amrud', 'onion', 'biscuit', 'kurkure']

#to add the new element at the specific position in the list
# listy.insert(1,'sabji')
# listy.insert(2,'pakode')
# print(listy)             # ['', 'sabji', 'pakode', '', 'allu', 'amrud', 'onion', 'biscuit', 'kurkure']
# listy.remove('allu')          #we need to give name here that we want to delete/remove.
# print(listy)                  #['', '', 'amrud', 'onion', 'biscuit']
# listy.pop()
# print(listy)                #['', '', 'amrud', 'onion']  this will remove the last element from the list.
# del listy[0]                   #deletes the specific element
# print(listy)                     #['', 'amrud', 'onion']  
# del listy                    #  this will delete the list and nothing will be print if we want.
# listy.clear()
# print(listy)                   #[] there will no element in the list it become empty clear



#TUPLE: 
 
# these are not changable and it is defined using () symbol
# tup=("1st",6,"anju")      
# print(tup)                  #('1st', 6, 'anju')
# tup1=('1st',6,'anju')     
# print(tup1)                   #('1st', 6, 'anju')
# print(type(tup))              #<class 'tuple'>
# tup[0]="2nd"             #this will not allowed we can't change the values of tuple directly
# print(tup)
# print(len(tup))               #3
# tup2=("2nd",5,"aditya")
# print(tup+tup2)                  #('1st', 6, 'anju', '2nd', 5, 'aditya')
# tup.clear()
# print(tup)                          #'tuple' object has no attribute 'clear'
# tup=tup.append("near rania road")
# print(tup)                              #'tuple' object has no attribute 'append'
#we can do this operation after typecasting the tuple into the list


#SET:

'''set is same as in mathematics that it is collection of well defined objects and order
and repeation not matters.'''
# setty={1,3,4,5,6}          #declaration of numerical set

#setty={'hye','anju','tum','hye','anju','tum'}             #declartion of string valued set
# print(setty)                     #{'tum', 'hye', 'anju'}
# setty.add(34555)                #used for adding only one elemnt in set
# print(setty)                     #{1, 3, 4, 5, 6, 34555}
#to add multiple numbers in set we can use update function
# setty.update([23,45,67,78,99,00,450,356,35,323,2456,89])
# print(setty)               #{0, 1, 450, 3, 4, 5, 6, 67, 99, 356, 35, 323, 45, 78, 23, 2456, 89}
# print(len(setty))             #5
# print(setty.remove(2))        #2 is invalid
# print(setty.remove(1))  
# print(setty)               #{3, 4, 5, 6}
'''if we write the number which is in tuple and want to delete it then
 it will easily delete that particular element but if write the element which is not in the tuple
  and we are writing for delete it then it will directly gives error to us. 
  so to overcome this problem we use discard means if it present in set then delete otherwise 
  discard that particular and print as same as set not giving any error but remove 
  is so strict in this error throwing matter'''
# print(setty.discard(345))
# print(setty)            #{1, 3, 4, 5, 6}
# print(setty.pop())                 #1
# print(setty.clear())               #None means empty now
# print(del setty)              #nothing will be print beacuse it is deleted now

# setty2={5,6,78,8,4,2,11,3}
# print(setty and setty2)       # intersection  
# print(setty2 or setty)         # union
# ''' output is {2, 3, 4, 5, 6, 8, 11, 78}
# {2, 3, 4, 5, 6, 8, 11, 78}
# '''



# '''DICTIONARY:
# dictionary is a collection of huge amount of data '''

# anjudict={
#   "Name" : "Anju",
#   "Class" : "10th",
#   "Roll No" : "4"


# }
# print(anjudict)         #output {'Name': 'Anju', 'Class': '10th', 'Roll No': '4'}
# print(anjudict["Class"])         #10th
# anjudict["Roll No"]="6"
# print(anjudict)               #{'Name': 'Anju', 'Class': '10th', 'Roll No': '6'}
# print(len(anjudict))           #3
# print(anjudict.replace("Roll No", "student Id"))          #'dict' object has no attribute 'replace'

# anjudict.pop("Roll No")          
# print(anjudict)               #{'Name': 'Anju', 'Class': '10th'}
# anjudict.clear()
# print(anjudict)                   #{}

'''IF,IF ELSE, IF ELSE IF STATEMENTS '''

# age=input("enter ur age:")    
# age=int(age) 
# '''input function is always work with string means it consider integer
# age is also the string so we need to typecasting it.'''
# print(age)
# print(type(age))
# if(age<18):
#   print("u can't vote")  
# elif(age==18):
#   print("can also")          
# else:
#   print("congrats u can")
'''enter ur age:1
1
<class 'int'>
u can't vote'''   

''' LOOPS :
1. for loop
2. while loop
3. dowhile loop'''


# for i in range (0, 1000):
#   # print(i)            #prints 0 to 999
#  print(i+1)            #prints 0 to 1000

# list=['dosa','register','aalo','rice']            
# for i in list:
#   print(i)        #dosa     iteration of a list
#                   #register
#                   # aalo
#                   # rice

# tup=("anju","4th",67)
# for i in tup:
#   print(i) 
#   '''output: iterate an tuple
# anju
# 4th
# 67'''

# set={1,3,5,6,7}
# for i in set:           
#   print(i)           #iterate a set

# dict={
#   "Heat":"garam",
#   "Shadow":"chanya",
#   "cold" : "thandi"

# }
# for i in dict:
#  print(i)               #Heat Shadow cold           
#  print(dict)           #{'Heat': 'garam', 'Shadow': 'chanya', 'cold': 'thandi'} (3 times after each term of above line.)

# i=0
# while(i<5):
#  print("hello")
#  i=i+1             # prints hello 5 times

#BREAK AND CONTINUE STATEMENT
# i=0
# while(i<10):
#  print(i+1)          #prints 1 to 10 no's
#  i=i+1


# i=1
# while(i<10):
  
#   if(i==3):
#      break
#          #prints 1 to 10 no's
#   print(i)    #only 1 and 2 print because when the value of i reach till 3 then it will break and come out of loop.
#   i=i+1


# i=1
# while(i<10):
  
#   i=i+1
   
#   if(i==3):
#      continue
#   print(i)         #only prints 2 to 10 except 3

# def greet():
#   print("good morning anju")
# greet()              #good morning anju


# def add():
#   print(4+5)       #9
# add()

# def runadd():
#   num1=input("enter the first no.")
#   num1=int(num1)
#   num2=input("enter the second no.")
#   num2=int(num2)
#   c=num1+num2
#   print(c)        #output:
#                    # enter the first no.54
#                    # enter the second no.3
#                    # 57
# runadd()              #with no argument

# def runadd(num1,num2):
  
#   c=num1+num2
#   return c     #output:
#                    #35
# d=runadd(10,25)     
# print(d)


class employee:
  def __init__(self,gname,gsalary):
    self.name=gname
    self.salary=gsalary
harry=employee("harry", 56)
print(harry.name)           #harry
print(harry.salary)         #56