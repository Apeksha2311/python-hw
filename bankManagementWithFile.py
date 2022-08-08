from importlib.resources import path
import os
import re
import random
no_of_star = 100
path ='AllFiles/UserInfo/UserRegisterationInfo.txt'


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
        except:
            pass

        #create user Registeration file

        with open(path,'a') as file:
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
                
                return "USer Does not exist"

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
                    Userid = input("Enter USer Id:")
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
        pass
    elif ch == 3:
        print(" THANK YOU FOR VISTING ".center(no_of_star,"*"))
        break
    else:
        print(" INVALID CHOICE".center(no_of_star,"*"))
