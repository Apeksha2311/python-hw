#Library management system

import re
print("\nKeys to the past… Gateway to the future. My library, my lifeline. Open your world. Opening the door to knowledge.\n")
print("\n******************************* LIBRARY MANAGEMENT SYSTEM *******************")



class library_management:
    def __init__(self):
        self.__admin_id = "admin"
        self.__admin_pass ="admin123"

        #book Section
        self.books = ["rich dad poor dad","the secret","harry poter"]
        self.authors = ["ankit","apeksha","pooja"]

        # User Section 
        
        self.user_name = []
        self.localUserId = []
        self.userContact = []
        self.userIdProf = []
        self.userPass = []

        # flags for user registration 

        self.userName_flag = False
        self.localUserId_flag = False
        self.userContact_flag = False
        self.userIdProf_flag = False
        self.userPass_flag = False

        # User Login Section
        self.UserLogin_flag = False




    def admin_login(self, adminId , adminPass ):
        if adminId == self.__admin_id:
            if adminPass == self.__admin_pass:
                return True
            else:
                return "Admin Password Incorrect"

    def ShowAllBooks(self):
        return zip(self.books,self.authors)

    def addBooks(self,bookName ,authorName):
        self.books.append(bookName)
        self.authors.append(authorName)
        return "Succefully Book added"

    def RemoveBook(self,bookAuthor):
        bookAuthor = bookAuthor.strip()
        
        if bookAuthor.lower() in self.books:
            position =self.books.index(bookAuthor.lower())
            self.books.pop(position)
            self.authors.pop(position)
            return "Book Successfully Remove from Library"
        else:
            return "Please Check Book Name again"

    # this method is used to remove the user
    def removeUser(self , uid):
        self.localUserId
        uid = uid.strip()
    
        if uid.lower() in self.localUserId:
            upos = self.localUserId.index(uid.lower())
            self.localUserId.pop(upos)

            self.user_name.pop(upos) 
            
            self.userContact.pop(upos)
            self.userIdProf.pop(upos)
            self.userPass.pop(upos)

            return f"User {uid} Successfully Removed "
        else:
            return f"User {uid} Not present In Database check Again"


    # this method is used to register new user 
    def userRegistration(self , name , uid , contact , id_prof , pass1 , pass2):
        
        
        # HW 21 /07 /2022
        # validate User name # only alphabets digit or spacial charact not included
        
        
        ptr = r"\A[a-zA-Z]+$"
        
        
        if re.match(ptr , name) :
            self.userName_flag = True
        else:
            return f"User name {name} is Invalid, Please Enter once again username"
        
        # add user id 
        if uid not in self.localUserId:
            self.localUserId_flag = True

        else:
            return f"User Id {uid} already Exists Try different Uid "

        # contact validation # HW 21/07/2022
        ptr1=r"[7-9]{9}"
        #ptr1=r"(0|91)?[7-9][0-9]{9}"
        Ucontact=re.findall(ptr1,contact)
        if Ucontact:
            self.userContact_flag = True
        else:
            return f"Please enter valid contact Number"

        # Id Proof 

        if id_prof not in self.userIdProf:
            self.userIdProf_flag = True
        else:
            return f"Id Proof Number {id_prof} already Exists Try Different "

        # password Validation 

        if pass1 == pass2:
            self.userPass_flag = True

        else:
            return "Entered Password Mismatch "


        # add User value 
        if self.userName_flag == True and self.localUserId_flag == True and self.userContact_flag == True and self.userIdProf_flag == True and self.userPass_flag == True:
            
            self.user_name.append(name)
            self.localUserId.append(uid)
            self.userContact.append(contact)
            self.userIdProf.append(id_prof)
            self.userPass.append(pass1)

            return f"User {uid} Successfully Registered"

    #user login section
    def localUserLogin(self,userId1,userPass):
        if userId1 in self.localUserId :
            if userPass in self.userPass:
                self.UserLogin_flag = True
                return self.UserLogin_flag
            
            else :
                return "Invalid Password"

        else :
            return "Invalid User Id"
    
    def bookallocation(self,bookname):
        if bookname in self.books:
            return f"Books Is {bookname} Allocated"

        else:
            return f"Book Name Is {bookname} Not Found"


#Application start from here        

app = library_management()     #instance

while True:
    print("1- Admin section\n2 - Local User \n3 - Exit\n")


    ch = input("Enter Your Choice :")

    if ch == "1":
        print("\n************* welcome to the admin section **********************\n")

        adminId = input("Enter admin id :")
        adminPass = input("Enter admin password:")

        adminId = adminId.strip()
        adminPass = adminPass.strip()


        admin_flag = app.admin_login(adminId , adminPass)
        if admin_flag == True:
            print("\n************** successfully admin Login ****************\n")

        while admin_flag == True:
            print("1 - show All books \n2 - Add book \n3 - Remove book  \n4 - Remove User \n5 - Logout \n")

            admin_ch = input("enter Admin choice:")


            if admin_ch == "1":
                print("\n************ show all Book and Authors *****************")

                all_books = app.ShowAllBooks()

                print("\tBooks \t Authors\n")

                for book,author in all_books:
                    print(f"\t{book.capitalize()}\t{author.capitalize()}\t")

                print("\n*********************************************************\n")
            
            elif admin_ch == "2":
                print("\n***************** Add Books **********************\n")
                bookName = input("Enter bookname :")
                authorName = input("Enter author name :")

                bookName = bookName.strip()
                authorName = authorName.strip()

                if bookName != " ":
                    if authorName != "":
                        feedback = app.addBooks(bookName ,authorName)

                        print(f"\n******************* { feedback } **************************\n")
                    else:
                        print("\n************** Author Name is Empty**************************\n")

                else :
                    print("\n************** book name is empty ****************\n")

            elif admin_ch == "3":
                print("\n*********** Delete Book *************************\n")



                bookAuthor = input("enter Book Name :")
                rflag = app.RemoveBook(bookAuthor)
                print(f"\n**************{rflag}******************\n")
                

                

            elif admin_ch == "4":
                print(f"\n********************* Remove User Section ***************\n")

                uid = input("Enter User Id:")
                remov_flag = app.removeUser(uid)
                print(f"\n*******************{remov_flag}******************\n")
            

            elif admin_ch == "5":
                print("\n**************** Logout Successfully ******************************\n")
                break

            else :
                print("\n************** Invalid Admin Option  *********************\n")
        else :
            print(f"\n****************** {admin_flag} **************************\n")



    # Local User Section
    elif ch == "2":

        print("\n*********** Welcome To User Section *******************\n ")
        while True:
            print("1 - Local User Login\n2 - Local User Registration\n3 - Exit From User Section\n")

            u_ch = input("Enter User Choice :")

            if u_ch == "1":
                print("\n********** local User Login ******************\n")

                userId1 = input("Enter user id:")
                userPass = input("Enter user pwd:")

                userId1 =userId1.strip()
                userPass = userPass.strip()

                UserFlag = app.localUserLogin(userId1,userPass)

                if UserFlag != True :
                    print(f"\n*********** {UserFlag} *************\n")

                else :
                    print("User Successfully Login")

                    while True :  
                        print("1-assign books\n2-logout users\n")
                        loginuser_ch=input("enter ur login choice:")
                        if loginuser_ch == "1":
                            print("**********book allocation***********")
                            allbooks=app.ShowAllBooks()
                            print("\tBOOKS\t\tAUTHORS\n")
                            for book,author in allbooks:
                                print(f"\t{book.capitalize()}\t\t{author.capitalize()}\n")



                            bookname=input("enter book name:")
                            bookname=bookname.lower()
                            app.bookallocation(bookname)


                        elif loginuser_ch =="2":
                            print("*****logout successfully******")
                            break
                        else:
                            print("invalid option")

                





            elif u_ch == "2":
                print("\n*********** Welcome to User Registration Form ***********\n")
                name = input("Enter User Name :")
                uid = input("Enter User Id :")
                contact = input("Enter Contact Number :")
                id_prof = input("Enter Id Prof Number :")
                pass1 = input("Enter Password :")
                pass2 = input("Confirm Password :")

                # remove Extra spaces from str data 

                name = name.strip()
                name = name.lower()

                uid = uid.strip()
                uid = uid.lower()

                contact = contact.strip()
                
                id_prof = id_prof.strip()
                id_prof = id_prof.lower()

                pass1 = pass1.strip()
                pass2 = pass2.strip()


                u_feedBack = app.userRegistration(name , uid , contact , id_prof , pass1 , pass2)

                print(f"\n****** {u_feedBack} *********\n")

            
                

            elif u_ch == "3":
                print("\n************** Exiting from User Section ***********\n")
                break

            else:
                print("\n************ Invalid User Choice *****************\n")







    elif ch == "3":
        print("\n********************* thank you for visitng **************\n")
        break
    else:
        print("\n***************************** Invalid Option ************************\n")
