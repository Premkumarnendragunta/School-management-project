#importing mysql module
import mysql.connector
#importing date library
from datetime import date
#defining a function to dispaly all admissions
def total():
conn=mysql.connector.connect(host="localhost",user="root",password="hariom123",database="mcv")
cursor=conn.cursor()
cursor.execute("select * from new_admission")
 data=cursor.fetchall()
 count=cursor.rowcount
 print("Total number of admissions are :")
 for i in data:
 print(i)
 return()
#defining a function bus_fee for entering the bus fee of the student

def bus_fee():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")
 cursor=conn.cursor()
 adm_no=int(input("Enter your admission number : "))
 name=input("Enter your name : ")
 Class=input("Enter your class : ")
 location=input("Enter your location : ")
 bus_fee=input("Enter your bus_fee : ")
 route=input("Enter your route number : ")
 sql="insert into
bus_fee(adm_no,name,class,location,bus_fee,route_no)
values('%d','%s','%s','%s','%s','%s')" %
(adm_no,name,Class,location,bus_fee,route)
 cursor.execute(sql)
 conn.commit()
 conn.close()
 return("bus fees added successfull..........")
#defining a function bus_fee for bus fees payment
def bus_payment():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")

 cursor=conn.cursor()
 name=input("Enter your name : ")
 Class=input("Enter your class :")
 bus_fee=input("Enter your bus_fee : ")
 today=date.today()
 sql="insert into
bus_payment(name,class,bus_fee,date_of_payment)
values('%s','%s','%s','%s')"%(name,Class,bus_fee,today)
 cursor.execute(sql)
 conn.commit()
 conn.close()
 return("Payment is successfull..........")
#defining a function books_payment for payment of the books
puechased by the student
def books_payment():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")
 cursor=conn.cursor()
 name=input("Enter your name : ")
 Class=input("Enter your class :")
 books_fee=input("Enter your books fee :")
 today=date.today()

 sql="insert into
books_payment(name,class,books_fee,date_of_payment)
values('%s','%s','%s','%s')"%(name,Class,books_fee,today)
 cursor.execute(sql)
 conn.commit()
 conn.close()
 return("Payment is successfull..........")
#defining a function books_fee for manually entering the books fee
of the student
def books_fee():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")
 cursor=conn.cursor()
 ad_no=int(input("enter admission number:"))
 name=input("Enter your name : ")
 Class=input("Enter your class : ")
 books_fee=input("Enter your books fee : ")
 sql="insert into books_fee(adm_no,name,class,books_fee)
values('%d','%s','%s','%s')"%(ad_no,name,Class,books_fee)
 cursor.execute(sql)
 conn.commit()

 conn.close()
 return("Books fee added successfull..........")
#defining a function school_fee for manually entering the school fee
of the student
def school_fee():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")
 cursor=conn.cursor()
 adm_no=int(input("Enter your admission number : "))
 name=input("Enter your name : ")
 Class =input("Enter your class : ")
 term_1=input("Enter your term 1 fee : ")
 term_2=input("Enter your term 2 fee : ")
 term_3=input("Enter your term 3 fee : ")
 sql="insert into
school_fee(adm_no,name,class,term_1,term_2,term_3)
values('%d','%s','%s','%s','%s','%s')"%(adm_no,name,Class,term_1,ter
m_2,term_3)
 cursor.execute(sql)
 conn.commit()
 conn.close()
 return("School fees added successfull..........")

#defining a function school_payment for payment of the school term
feeses
def school_payment():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")
 cursor=conn.cursor()
 name=input("Enter your name : ")
 Class=input("Enter your class : ")
 term=input("Enter your term : ")
 amount=input("Enter amount : ")
 today=date.today()
 sql="insert into
school_payment(name,class,term,amount,date_of_payment)
values('%s','%s','%s','%s','%s')"%(name,Class,term,amount,today)
 cursor.execute(sql)
 conn.commit()
 conn.close()
 return("Payment is successfull..........")

#defining a function new_admission for entering data of a new
student
def new_admission():

conn=mysql.connector.connect(host="localhost",user="root",passwo
rd="hariom123",database="mcv")
 cursor=conn.cursor()
 adm_no=int(input("Enter your admission number : "))
 name=input("Enter your name : ")
 Class=input("Enter your class : ")
 address=input("Enter your address : ")
 phone=input("Enter your mobile number :")
 email=input("enter your email : ")
 aadhar=input("Enter your aadhar number : ")
 mname=input("Enter your mother name : ")
 fname=input("Enter your father name : ")
 sql="insert into
new_admission(adm_no,name,class,address,phn_no,email,aadhar,m
other_name,father_name) values
('%d','%s','%s','%s','%s','%s','%s','%s','%s')"%(adm_no,name,Class,add
ress,phone,email,aadhar,mname,fname)
 cursor.execute(sql)
 conn.commit()
 conn.close()
 return("New student added successfully............")

#calling the functions and desiging the interface
while True:
 print()
 print("-"*90)
 print("\t\t\t\t\tHari om!!")
 print("\n\t\t\t\tMarg Chinmaya Vidyalaya")
 print("1.Admission\n")
 print("2.Fees\n")
 print("3.Staff\n")
 print("4.Classes\n")
 print("5.Payment\n")
 print("6.Non-teaching staff \n")
 print("7.Office staff\n")
 print("8.Board of manging directors\n")
 print("9.Lab details \n")
 print("10.Exit\n")
 a=int(input("Enter your choice(1-10)....."))
 print("-"*90)

 if a==1:
 print("\t\t\t\t\t----ADMISSION-----")
 print("1.New admission\n")
 print("2.Total admissions\n")

 x=int(input("enter your choice(1-2).."))
 if x==1:
 print("\t\t\t\tNEW-ADMISSION\n\n")
 print(new_admission())
 else:
 print(total())

 elif a==5:
 print("\t\t\t\t\t----PAYMENT------")
 print("1.School fee payment\n")
 print("2.Bus fee payment\n ")
 print("3.Books fee payment\n")
 z=int(input("Enter your choice(1-3)..."))
 if z==1:
 print("\t\t\t\t\t-----SCHOOL FEE PAYMENT-----")
 print(school_payment())
 elif z==2:
 print("\t\t\t\t\t-----SCHOOL FEE PAYMENT-----")
 print(bus_payment())
 elif z==3:
 print("\t\t\t\t\t-----BOOKS FEE PAYMENT-----")
 print(books_payment())


 elif a==2:
 print("\t\t\t\t\t-----FEEs------")
 print("1.School fee\n")
 print("2.Books fee\n")
 print("3.Bus fee\n")
 w=int(input("Enter your choice(1-3)....."))
 if w==1:
 print("\t\t\t\t\t-----SCHOOL FEE-------")
 print(school_fee())
 elif w==2:
 print("\t\t\t\t\t-----BOOKS FEE-------")
 print(books_fee())
 elif w==3:
 print("\t\t\t\t\t-----BUS FEE-------")
 print(bus_fee())
#retrieving the information stored in text files

 elif a==3:
 print("------------STAFF OF CHINMAYA VIDYALAYA---------")
 x=open("staff.txt","r")
 a=x.read()

 print(a)
 elif a==4:
 print("----------------CLASSES------------------")
 x=open("class.txt","r")
 a=x.read()
 print(a)
 elif a==9:
 print("-----------LAB DETAILS---------")
 x=open("lab.txt","r")
 a=x.read()
 print(a)
 elif a==6:
 print("-------NON TEACHING STAFF--------")
 x=open("non_teach.txt","r")
 a=x.read()
 print(a)
 elif a==7:
 x=open("office.txt","r")
 a=x.read()
 print(a)
 elif a==8:
 x=open("board.txt","r")
 a=x.read()
 print(a)

#coming out of the interface if user entered
 elif a==10:
 break 
