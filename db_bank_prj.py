
import mysql.connector as db
import re
import random


class bank:
    def __init__(self):
        self.__adminid = 'admin'
        self.__adminpasswd = 'admin'

        # create Database

        # create table
        mydb = db.connect(host = 'localhost', user = 'dbuser' , passwd = 'dbuser', database = 'dbuser')
        cur = mydb.cursor()
        query = '''create table if not exists Holder_info(id int primary key auto_increment,name varchar(100) not null,dob date not null,acc_type varchar(100) not null,acc_no bigint not null,email varchar(100) unique not null,contact bigint unique not null,amount bigint not null,password varchar(100));'''
        cur.execute(query)
        mydb.close()


    def AdminLogin(self,adminid,adminpasswd):
        if self.__adminid == adminid:
            if self.__adminpasswd == adminpasswd:
                print("\n**********Login Successfully ***********")
                return True
            else:
                print("\n*********invalid password ***********")
        else:
            print("\n********** Invalid Id *****************")

    def connection(self):
        self.mydb = db.connect(host = 'localhost', user = 'dbuser' , passwd = 'dbuser', database = 'dbuser')
        self.cur = self.mydb.cursor()

    def RegisterUser(self,name,dob,acc_no,acc_type,email,contact):
        
        acc_no = int(acc_no)
        contact = int(contact)

        self.connection()

        try:
            data = (name,dob,acc_no,acc_type,email,contact)
            query = '''insert into Holder_info(name,dob,acc_type,acc_no,email,contact,amount,password) values(%s,%s,%s,%s,%s,%s,0,null);'''

            self.cur.execute(query,data)

            self.cur.execute("commit;")
            self.mydb.close()
        except:
            self.mydb.close()
            return 'Email or contact Already Exists....'

        else:
            return True


        
    def generatepassword(self,pass1,email):
        self.connection()
        data = (email,)
        query = '''select password from Holder_info where email = %s;'''

        self.cur.execute(query,data)
        d= self.cur.fetchone()

        self.mydb.close()

        if d[0] == None:
            self.connection()
            try:
                data = (pass1,email)
                query = '''update Holder_info set password = %s where email = %s;'''
                self.cur.execute(query,data)
                self.cur.execute("commit;")
                self.mydb.close()

            except:
                self.mydb.close()
                return "password failed to generate"

            else:
                return True

        else:
            return "password Already Generated"

    def DeleteAccount(self,email,acc_no):
        self.connection()
        data = (email,acc_no)
        query = '''select acc_no from Holder_info where email = %s && acc_no = %s;'''
        self.cur.execute(query,data)
        d = self.cur.fetchone()
        print(d)
        self.mydb.close()

        if d == None:
            return "Account Does Not Exists"

        elif d[0] == None:
            return "Account Does Not Exists"

        else:
            self.connection()
            data = (email,acc_no)
            query = ''' delete from Holder_info where email = %s && acc_no = %s;'''
            self.cur.execute(query,data)
            self.cur.execute("commit;")
            self.mydb.close()
            return True







    def UserLogin(self,email,pass1):  
        self.connection()
        data=(email,pass1)
        query='''select email,password from Holder_info where email=%s && password=%s;'''
        self.cur.execute(query,data)
        value=self.cur.fetchone()
        #print(value)
        self.mydb.close()
        try:
            if value[0]==email:
                if value[1]==pass1:
                    return True
        except:
            return "User Email id or password is incorrect"     



    def check_balance(self,email,pass1):    
        self.connection()
        data=(email,pass1)
        query='''select name,acc_type,acc_no,email,amount from Holder_info where email=%s && password=%s;'''
        self.cur.execute(query,data)
        value=self.cur.fetchone()
         #print(value)
        self.mydb.close()
        return value



    def Depositeawamount(self ,amount,email,pass1):
        info=self.check_balance(email,pass1)
        balance=int(info[4])
        new_amount=balance+int(amount)

        self.connection()
        query='''update Holder_info set amount=%s where email=%s && password=%s;''' 
        data=(new_amount,email,pass1)
        self.cur.execute(query,data)     
        self.cur.execute("commit;")
        self.mydb.close()
        return f"Previous Balance:{balance} Deposite Balance:{new_amount}"





    def Withdrawamount(self ,amount1,email,pass1):
        info=self.check_balance(email,pass1)
        balance=int(info[4])

        if int(amount1) > balance:
            return "Insufficient amount"
        else:
            new_amount=balance-int(amount1)

        
        self.connection()
        query='''update Holder_info set amount=%s where email=%s && password=%s;''' 
        data=(new_amount,email,pass1)
        self.cur.execute(query,data)     
        self.cur.execute("commit;")
        self.mydb.close()
        return f"Previous Balance:{balance}:Withdraw Balance:{new_amount}"        
        


    # application start 

app = bank()
print("\n**************** Bank Application **************\n")

while True:
    print("\n1 - Admin login \n2 - user login \n3 - Generate password \n4 - Exit application\n")

    ch = input("Enter Your Choice :")

    if ch == '1':
        print("\n**************** Admin Login Section ****************\n")
        adminid = input("Enter Your Id :")
        adminpasswd = input("Enter Your Password :")

        # cleaning Data

        adminid = adminid.strip()
        adminpasswd = adminpasswd.strip()

        x = app.AdminLogin(adminid,adminpasswd)
        if x != True:
            print("\n***********{x}****************\n")
        else:
            print("\n************ Successfully Admin Login ***************\n")
            while True:
                print("\n1 - Create Account \n2 - Close Account \n3 - Update Account \n4 - Logout Admin\n")

                a_ch = input("Enter Admin Choice :")

                if a_ch == '1':
                    print("\n********** Create New Account *************\n")

                    while True:
                        name = input("Enter Your Name :")

                        nameptr = r'[a-zA-Z]+$'
                        if re.match(nameptr,name):
                            break
                        else:
                            print("\n********* Please Enter Correct Name **************\n")

                    while True:
                        dob = input("Enter Your Date of Birth (yyyy-mm-dd):")
                        dob_ptr = r'\d{4}-\d{2}-\d{2}'
                        if re.match(dob_ptr,dob):
                            break
                        else:
                            print("\n*********Please Enter Correct DOB *************\n")

                    print("\n1 - Saving Account \n2 - Current Account")
                    while True:
                        acc_type =input("Enter Your AccountType :")
                        if acc_type == '1':
                            break
                        elif acc_type == '2':
                            break

                        else:
                            print("\n******* Incorrect AccountType *********\n")
                    
                    acc_no = '100'
                    if acc_no == '1':
                        acc_no = acc_no+'103'
                    elif acc_type == '2':
                        aacc_no = acc_no+'201'

                    

                    acc_no = acc_no+str(random.randint(1000,9999))

                    while True:
                        email = input("Enter Your Email Id :")
                        email_ptr = r'[a-z-0-9\_\.]+@+[a-z]+'
                        if re.match(email_ptr,email):
                            break
                        else:
                            print("\n****** Please Enter Correct Mail Id *********")

                    while True:
                        contact = input("Enter Your Contact NO :")
                        contact_ptr = r'^[6-9]+[0-9]{9}$'
                        if re.match(email_ptr,email):
                            break
                        else:
                            print("\n****** Please Enter Correct No **********")


                    x = app.RegisterUser(name,dob,acc_no,acc_type,email,contact)

                    if x != True:
                        print(f"\n*********{x}********\n")
                    else:
                        print(f"\n********* Successfully Account Create And Account No is {acc_no} ********\n")
                
                elif a_ch == '2':
                    print("\n********** Closing Account Section ***************\n")
                    email = input("Enter Account Holder Email Which U want To Delete :")
                    acc_no = input("Enter Account Holder Account Number Which U Want To Delete :")
                    print("Are You Sure U Want To Delete Account ")
                    ch1 = input("(Y/N) :")
                    if ch1 == 'Y' or ch1 == 'y':
                        y = app.DeleteAccount(email,acc_no)
                        if y != True:
                            print(f"\n************{y} **********\n")

                        else:
                            print("\n********* Account Closed {acc_no}***********\n")
                    
                    else:
                        print("\n********* Account Delete Process Cancelled ***********\n")
                


                elif a_ch == '3':
                    pass
                
                elif a_ch == '4':
                    print("\n***********Successfull admin Logout *********\n")
                    break

                else:
                    print("\n********* Invalid Admin Choice ***********")








                


                
    elif ch == '2':
        print("\n**************** User Login Section *******************\n")
        email=input("enter your email is:")
        pass1=input("enter your pass1:")

        x=app.UserLogin(email,pass1)
        if x!=True:
            print(f"\n*********************{x}**********************\n")
        else:
            print(f"\n************** successfully login***************************\n")


            while True:
                print("1-check Balance\n2-widraw Amount\n3-Deposite Amount\n4-Account History\n5-User logout")

                U_ch=int(input("Enter your choice:"))

                if U_ch==1:
                    print("\n************* check balance section *************\n")

                    z=app.check_balance(email,pass1)
                    #print(z)
                    print(f"Account Holder Name is:{z[0]}")
                    print(f"Account type is:{z[1]}")
                    print(f"Account number is:{z[2]}")
                    print(f"Account Holder email-id is:{z[3]}")
                    print(f"Available balance is:{z[4]}\n")

                elif U_ch==2:
                    print("\n********** withdraw Amount section **********\n")
                    amount1=input("Enter withdraw amount:")
                    am1 =app.Withdrawamount(amount1,email,pass1)
                    print(f"\**********{am1}*************\n")

                    


                elif U_ch==3:
                    print("\n********** Deposite Amount section **********\n")
                    amount=input("Enter Deposite amount:")
                    am =app.Depositeawamount(amount,email,pass1)
                    print(f"\**********{am}*************\n")
                   
                    
                    


                elif U_ch==4:
                    pass


                elif U_ch==5:
                    print("\n************* User Logout ****************\n")
                    break

                else:
                    print("\n********Invalid Chice you Selected*******\n")











    elif ch == '3':
        print("\n****** Generate Password Section *************\n")
        email = input("Enter Your Email Id :")
        pass1 = input("Enter Your Password :")
        pass2 = input("Confirmed Your Password :")
        if pass1 != pass2:
            print("\n*********Password Did Not Match **********\n")

        else:
            x = app.generatepassword(pass1,email)


            print("\***** Successfully Password Generated *********\n")


        

    elif ch == '4':
        print("\n**************** Exited Application ***************\n")

    else:
        print("\n********* Invalid Option ************")
