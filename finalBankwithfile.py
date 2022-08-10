
import os
import re
import random
no_of_star = 100
path ='AllFiles/UserInfo/UserRegisterationInfo.txt'
#path1 ='AllFiles/UserBanking/UserBanking.txt'


print(" BANK MANAGEMENT SYSTEM ".center(no_of_star, '*'))

class Admin:
    def __init__(self):

        #admin Details
        self.__AdminId = "admin123"
        self.__AdminPassword = "admin123"


        








    def AdminLogin(self,AdminId,AdminPass):

        if AdminId == self.__AdminId:
            if AdminPass == self.__AdminPassword  :
                return True
            else:
                return "Invalid Admin Password"
        else:
            return "Invalid Admin Id"                

       

class User(Admin):
    def __init__(self):

        super().__init__()

        #create directories
        try:
            os.mkdir('AllFiles')
            os.mkdir('AllFiles/UserInfo')
            os.mkdir('AllFiles/UserBanking')
        except:
            pass

        #create user Registeration file

        with open(path,'a') as file:
            pass
        with open('AllFiles/UserBanking/UserBanking.txt','a') as file:
            pass


        #User Admin Flag
        self.UserNameFlag = False
        self.UserEmailIdFlag = False
        self.UserContactFlag = False
        self.UserPassFlag = False
        self.flag = False

    def ReadAllRegisterData(self):
        with open(path,'r') as file:
            data = file.read()
        return data    







    def validateUsername(self,UserName):
        name_length = len(UserName)
        x = re.findall('[a-z]+',UserName)
        
        if len(x[0]) == name_length:
            return True 
        else:
            return False   

    def ValidateEmailId(self,UserEmail) :
        ptr = r"^[a-zA-Z0-9\.]+@[a-z]+\.[a-z]+"
        x = re.findall(ptr,UserEmail )
        if len(x) > 0:
            return True
        else:
            return False           
    


    def validateContact(self, contact):
        ptr = r"[6-9]\d{9}"
        x = re.findall(ptr, contact)
        if len(x) > 0:
            return True
        else:
            return False

    def RegisterUser(self,UserName, UserEmail , UserContact , UserPass1 ,UserPass2 ):
        #name validation
        self.UserNameFlag = self.validateUsername(UserName)
        
        if self.UserNameFlag != True:
            return "User is not Valid ,try with alphabets"


        self.UserEmailIdFlag = self.ValidateEmailId(UserEmail)  

        if self.UserEmailIdFlag != True:
            return "Invalid Email ID"  

        self.UserContactFlag = self.validateContact(UserContact)  

        if self.UserContactFlag != True:
            return "Invalid Contact No contact"

        if UserPass1 == UserPass2:
            self.UserPassFlag = True
        else:
            return "Password Mis match"  

        #generate user id
        UserId = UserName +str(random.randint(100,9999)) 


        #read all data
        alldata = self.ReadAllRegisterData()  

        #check Email Username and contact Already exist or not
        if UserEmail not in alldata:
            if UserId not in alldata:
                if UserContact not in alldata:
                    self.flag = True
                else:
                    return "USer Contact already exist"    

                
            else:
                return "User id already exit"       
        else:
            return "USer Email Id is already Exist"


        #insert user data into file   
        if self.UserNameFlag == True and self.UserEmailIdFlag == True and self.UserContactFlag==True and self.UserPassFlag == True and self.flag == True:
            data = f"{UserName},{UserId},{UserEmail},{UserContact},{UserPass1},\n"
            with open(path,'a') as file:
                file.write(data)


            with open('AllFiles/UserBanking/UserBanking.txt','a') as file1:
                bankingdata =f"{UserId},{UserEmail},0,\n"
                file1.write(bankingdata)
            return f" Successfully Register USer {UserName} with User Id as : {UserId} "
        
        

    #Remove user Section

    def RemoveUser(self,Useremail,Userid,AdminPass):
        
        if AdminPass == 'admin123':
            with open(path,'r') as f:
                readdata=f.readlines()
          
            #read all data
            alldata = self.ReadAllRegisterData()  

        #check Email Already exist or not
            if Useremail not in alldata:
                
                return "User Does not exist"

            for i in range(len(readdata)):
                if Useremail in readdata[i]:
                    print(readdata[i])
                    readdata.remove(readdata[i])
                    break
    


            with open(path,'w') as f:
                f.write(''.join(readdata))
                
            return f"User {Userid} Removed Successfully"


          
        else:
            return "Admin Password is incorrect"
    
    #This method is used to login user
    def userLogin(self,userId ,userPass):
        userId = userId.strip()
        userPass = userPass.strip()

        flag = False
        with open(path,"r") as file:
            alldata = file.readlines()

            for line in alldata:
                line = line.split(",")
                #print(line)

                if(line[1] == userId) and (line[4] == userPass):
                    flag = True
        return flag

    #this method is used to return Available balance
    def CheckBalance(self , UserId):
        with open('AllFiles/UserBanking/UserBanking.txt','r') as file1:
            readBankingData = file1.readlines()

            for line in readBankingData:
                #print(type(line))

                line1 = line.split(",")
                if UserId in line1:
                    balance = line1[2]
        #print(type(balance))
        balance = int(balance)
        return balance

    #this method for deposite balance
    def depositeBalance(self,amount,userId):
        oldamount = self.CheckBalance(userId)
        newamount = oldamount + amount

        with open('AllFiles/UserBanking/UserBanking.txt','r+') as file1:
            readBankingData = file1.readlines()

            for line in readBankingData:
                #print(type(line))
                line1 = line.split(",")
                if userId in line1:
                    pos = readBankingData.index(line)

                    line1[2] = str(newamount)
                    line1 = ",".join(line1)
                    readBankingData[pos] = line1

            print()
            data = "".join(readBankingData)
            print(data)

            file1.seek(0)
            file1.write(data)

            return f"SuccessFully deposite amount {amount}"

    #this method is used for widraw balance
    def widrawBalance(self,amount,userId):
        oldamount =  self.CheckBalance(userId)
        if amount > oldamount:
            return "Invalid Amount"
        
        else:
            newamount = oldamount - amount

            with open('AllFiles/UserBanking/UserBanking.txt','r+') as file1:
                readBankingData = file1.readlines()

            
                for line in readBankingData:
                    #print(type(line))
                    line1 = line.split(",")
                    if userId in line1:
                        pos = readBankingData.index(line)

                        line1[2] = str(newamount)
                        line1 = ",".join(line1)
                        readBankingData[pos] = line1

                print()
                data ="".join(readBankingData)
                #print(data)

                file1.seek(0)
                file1.write(data)

            return f"SuccessFully widraw amount {amount}"



            




           
        
                      




        


















#Application Start From here
app=User()

while True:
    print("\n1 -Admin Login\n2 -User Login\n3 -Exit\n")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        #Admin Login Start from here 
        print("Admin Login Section".center(no_of_star,"*"))

        AdminId = input("Enter Admin id :")
        AdminPass = input("Enter Admin Password:")

        adminFlag =app.AdminLogin(AdminId , AdminPass)
        
        if adminFlag != True:
            print(f"\n******* {adminFlag} ************\n")
        else:
            print("Admin Logged In Successfully".center(no_of_star,"*"))

            #After Admin Loged in Section
            while True:
                print("\n1 -Create User\n2 -Remove User\n3 -Admin logout\n")

                Adminch =int(input("Enter Admin choice:") ) 

                if Adminch == 1:
                    print("Create USer Section".center(no_of_star,"*"))

                    UserName = input("Enter User Name:")
                    UserEmail = input("Enter User Email:")
                    UserContact = input("Enter user contact:")
                    UserPass1 = input("Enter Password")  
                    UserPass2 = input("Confirm Password:")

                    userCreation = app.RegisterUser(UserName , UserEmail ,UserContact ,UserPass1 ,UserPass2)
                    print(f"{userCreation}".center(no_of_star,"*"))
                
                elif Adminch == 2:
                    
                    print("Remove User section".center(no_of_star,"*"))
                    Useremail = input("Enter USer EmailId:")
                    Userid = input("Enter User Id:")
                    AdminPass= input("Enter Admin Password:")

                    confirm = input(f" Are you sure you want to dalete user {Userid} (Y/N):").lower()
                    
                    if confirm == 'y':

                        removeFlag =app.RemoveUser(Useremail,Userid,AdminPass)
                        print(f"{removeFlag}".center(no_of_star,"*"))
                    else:
                        print(f" Process terminated to delete user {Userid} ".center(no_of_star,"*"))   
                             









                elif Adminch == 3:
                    print("Successfully Admin Logged Out".center(no_of_star,"*"))
                    break
                else:
                    print("Invalid Choice".center(no_of_star,"*"))
                   


                      
                    
                    


         
       

    elif ch == 2:
        print("User login section".center(no_of_star,"*"))
        userId = input("Enter user id:")
        userPass = input("Enter user password:")

        userLoginFlag = app.userLogin(userId ,userPass)
        if userLoginFlag != True:
            print(" Invalid id or password ".center(no_of_star,"*"))
        else:
            print("Successfully logged in".center(no_of_star,"*"))

            #After user login section
            while True:
                print("1 -Check Balance\n2 -Deposite Amount\n3 -Widraw amount\n4 -Logout\n")

                userch = int(input("Enter user choice:")) 
                if userch == 1:
                    print(" Current Available Balance ".center(no_of_star,"*"))

                    data = app.CheckBalance(userId)
                    print(f" Available Balance is :{data} ".center(no_of_star,"*"))

                elif userch == 2:
                    print("Deposite Amount".center(no_of_star,"*"))

                    amount = int(input("enter Amount:"))

                    data = app.depositeBalance(amount,userId)
                    print(f"{data}".center(no_of_star,"*"))



                elif userch == 3:
                    print("Widraw Amount".center(no_of_star,"*"))

                    amount =int(input("Enter widraw Amount:"))

                    data = app.widrawBalance(amount,userId)

                    print(f"{data}".center(no_of_star,"*"))

                elif userch == 4:
                    print(" User logged out Successfully ".center(no_of_star,"*"))
                    break
                else:
                    print("Invalid User choice".center(no_of_star,"*"))



















    elif ch == 3:
        print(" THANK YOU FOR VISTING ".center(no_of_star,"*"))
        break
    else:
        print(" INVALID CHOICE".center(no_of_star,"*"))
