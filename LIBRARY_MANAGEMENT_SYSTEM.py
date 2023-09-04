import time
from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ROOT",database="CBS")
mycur=mydb.cursor()


#FUNCTIONS

def addbook():
    tab=input("Add Books to which data ? \n --->")
    while tab!="dystopia" and tab!="non fiction" and tab!="young adult":
        print("ERROR (Last Try) Enter a valid response.")
        time.sleep(1)
        
        c=input("Which genre data ? \n --->")
        break
    if tab=="dystopia":
        n=int(input("How many entries to insert ? "))
        for j in range(n):
            ids=int(input("Enter Book ID --> "))
            g=input("Enter Book name ")
            h=input("Enter Author name ")
            i=input("Enter Publisher ")
            mycur.execute("insert into dystopia values({},'{}','{}','{}')".format(ids,g,h,i))
            mydb.commit()

    elif tab=="non fiction":
        n=int(input("How many entries to insert ? "))
        for j in range(n):
            ids=int(input("Enter Book ID --> "))
            g=input("Enter Book name ")
            h=input("Enter Author name ")
            i=input("Enter Publisher ")
            mycur.execute("insert into non_fiction values({},'{}','{}','{}')".format(ids,g,h,i))
            mydb.commit()
    elif tab=="young adult":
        n=int(input("How many entries to insert ? "))
        for j in range(n):
            ids=int(input("Enter Book ID --> "))
            g=input("Enter Book name ")
            h=input("Enter Author name ")
            i=input("Enter Publisher ")
            mycur.execute("insert into young_adult values({},'{}','{}','{}')".format(ids,g,h,i))
            mydb.commit()
            time.sleep(0.5)
    print("Success")

def delete():
    n=input("Enter Book Name -->")
    mycur.execute("select * from dystopia")
    myrecords=mycur.fetchall()
    for r in myrecords:
        if n in r:
            mycur.execute("delete from dystopia where book_name='"+n+"'")
            print("Success")
        else:
            time.sleep(0.1)
    mydb.commit()
    mycur.execute("select * from non_fiction")
    myrecords2=mycur.fetchall()
    for s in myrecords2:
        if n in s:
            mycur.execute("delete from non_fiction where book_name='"+n+"'")
            print("Success")
        else:
            time.sleep(0.1)
    mydb.commit()
    mycur.execute("select * from young_adult")
    myrecords3=mycur.fetchall()
    for t in myrecords3:
        if n in t:
            mycur.execute("delete from young_adult where book_name='"+n+"'")
            print("----Success----")
        else:
            time.sleep(0.2)
    mydb.commit()

def showall():
    mycur.execute("select * from Dystopia union select * from Young_Adult union select * from Non_Fiction order by book_id")
    result = mycur.fetchall()
    mydata=[[[result]]]
    head=["BOOK ID","BOOK NAME","AUTHOR","PUBLISHER"]
    print(tabulate(result,headers=head,tablefmt="fancy_grid"))

def showissue():
    mycur.execute("select * from customer_entry order by book_id")
    result = mycur.fetchall()
    mydata=[[[result]]]
    head=["BOOK ID","BOOK NAME","ISSUED BY","ISSUED DATE","SUBMISSION DATE"]
    print(tabulate(result,headers=head,tablefmt="fancy_grid"))
    
def addissue():
    n=int(input("How many entries to insert ? "))
    for j in range(n):
        a1=int(input("Enter Book ID --> "))
        b1=input("Enter Book name ")
        c1=input("Enter Issuer's Name ")
        d1=input("Enter Issued Date (Format : YYYY-MM-DD)  ")
        e1=input("Enter Submission Date (Format : YYYY-MM-DD) ")
        mycur.execute("insert into customer_entry values({},'{}','{}','{}','{}')".format(a1,b1,c1,d1,e1))
        time.sleep(0.5)
        print("Success")
        mydb.commit()
        
def updatedata():
    mycur=mydb.cursor()
    print("Available Genres : \n 1.) dystopia \n 2.) non fiction \n 3.) young adult")
    an=input("Select Genre \n --->")
    while an!="dystopia" and an!="non fiction" and an!="young adult":
        print("ERROR (Last Try) Enter a valid response.")
        time.sleep(1)
        break
    if an=="dystopia":
        n=input("Which Book would you like to Update ? (Enter Book Name) \n ---> ")
        r=int(input("Enter New Book ID ---> "))
        s=input("Enter New Book Name ---> ")
        t=input("Enter New Author Name ---> ")
        u=input("Enter New Publisher Name ---> ")
        sql="UPDATE non_fiction SET book_id=%s, book_name=%s, author = %s, publisher=%s WHERE book_name = %s"
        val=(r,s,t,u,n)
        mycur.execute(sql,val)
        mydb.commit()
    elif an=="non fiction":
        n=input("Which Book would you like to Update ? (Enter Book Name) \n ---> ")
        r=int(input("Enter New Book ID ---> "))
        s=input("Enter New Book Name ---> ")
        t=input("Enter New Author Name ---> ")
        u=input("Enter New Publisher Name ---> ")
        sql="UPDATE non_fiction SET book_id=%s, book_name=%s, author = %s, publisher=%s WHERE book_name = %s"
        val=(r,s,t,u,n)
        mycur.execute(sql,val)
        mydb.commit()
    elif an=="young adult":
        n=input("Which Book would you like to Update ? (Enter Book Name) \n ---> ")
        r=int(input("Enter New Book ID ---> "))
        s=input("Enter New Book Name ---> ")
        t=input("Enter New Author Name ---> ")
        u=input("Enter New Publisher Name ---> ")
        sql="UPDATE non_fiction SET book_id=%s, book_name=%s, author = %s, publisher=%s WHERE book_name = %s"
        val=(r,s,t,u,n)
        mycur.execute(sql,val)
        mydb.commit()
    time.sleep(0.5)
    print("----Success----")

def ifbook():
    mycur.execute("select book_name from Dystopia union select book_name from Young_Adult  union select book_name from Non_Fiction")
    rows = mycur.fetchall()
    xy=input("Which book would like to Find ? \n ---->")
    for row in rows:
        if xy in row:
            time.sleep(0.5)
            print("Yes --",xy,"-- Book is Available")
        elif xy not in rows:
            pass

def ifpublisher():
    mycur.execute("select publisher from Dystopia union select publisher from Young_Adult  union select publisher from Non_Fiction")
    rows = mycur.fetchall()
    xy=input("Which book would like to Find ? \n ---->")
    for row in rows:
        if xy in row:
            time.sleep(0.5)
            print("Yes --",xy,"-- Publications is Available")
        elif xy not in rows:
            pass



#Entrance page

time.sleep(1)
a="-------------+                        WELCOME  TO  DELHI  PUBLIC  LIBRARY                        +-------------"
b="-------------+                        A Govt. of India Organisation , Ministry of Culture                        +-------------"
print(a.center(130),"\n",b.center(100))

time.sleep(1)

print("\n"," ---      For Customer Service , Enter (1)","\n"," ---      For Staff Portal , Enter (2)")
c=int(input(" --->"))                                                                                 
time.sleep(0.5)

while c!=1 and c!=2:
    print("ERROR (Last Try) Enter a valid response.")
    time.sleep(0.5)
    c=int(input(" --->"))
    break

#in customer service , show available books if the person can issue it or not and find books by name or publisher

if c==1:
    d="----------+       WELCOME TO CUSTOMER SERVICE PORTAL        ----------+"
    print(d.center(100))                                                                        #more to work on
    time.sleep(0.5)
    mydata=[["Find Books by Names","(1)"],["Find Books of Publications","(2)"]]
    head=["Features to Do","Code Number"]
    print(tabulate(mydata,headers=head,tablefmt="fancy_grid"))
    print("Please Enter a Code feature to Perform")

    f=int(input("---> "))
    while f!=1 and f!=2:
        print("ERROR (Last Try) Enter a valid response.")
        time.sleep(1)
        f=int(input(" --->"))
        break
    if f==1:
        ifbook()
    elif f==2:
        ifpublisher()

    wh=input("Would you like to continue ? (yes/no) \n --->")
    while wh=="yes":
        print("Please Enter a Code feature to Perform")
        f=int(input("---> "))
        if f==1:
            ifbook()
        elif f==2:
            ifpublisher()
        wh=input("Would you like to continue ? (yes/no) \n --->")
        

#staff can select out books by name or publisher,insert more books,delete discarded books,update any detail

elif c==2:
    e="----------+       WELCOME TO STAFF PORTAL        ----------+" 
    print(e.center(100)) 
    time.sleep(0.5)
    mydata=[["To Show Issued Book History","(1)"],["To Add New Books Issued","(2)"],["To Delete Discarded Books","(3)"],["To Update a Book Detail","(4)"],["To Display All the Books Record","(5)"],["To Add Books To Library Data","(6)"]]
    head=["Features to Do","Code Number"]
    print(tabulate(mydata,headers=head,tablefmt="fancy_grid"))
    print("Please Enter a Code feature to Perform")
    f=int(input("---> "))

    while f!=1 and f!=2 and f!=3 and f!=4 and f!=5 and f!=6:
        print("ERROR (Last Try) Enter a valid response.")
        time.sleep(1)
        f=int(input(" --->"))
        break

    if f==6:
        print("Available Genres : \n 1. dystopia \n 2. non fiction \n 3. young adult")
        addbook()
    elif f==3:
        delete()
    elif f==5:
        showall()
    elif f==1:
        showissue()
    elif f==2:
        addissue()
    elif f==4:
        updatedata()

    wh=input("Would you like to continue ? (yes/no) \n --->")
    while wh=="yes":
        print("Please Enter a Code feature to Perform")
        f=int(input("---> "))
        if f==6:
            print("Available Genres : \n 1. dystopia \n 2. non fiction \n 3. young adult")
            addbook()
        elif f==3:
            delete()
        elif f==5:
            showall()
        elif f==1:
            showissue()
        elif f==2:
            addissue()
        elif f==4:
            updatedata()
        wh=input("Would you like to continue ? (Yes/No) \n --->")

