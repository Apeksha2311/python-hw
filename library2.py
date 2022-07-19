#Library management system



print("\n******************************* LIBRARY MANAGEMENT SYSTEM *******************")



class library_management:
    def __init__(self):
        self.__admin_id = "admin"
        self.__admin_pass ="admin123"

        #book Section
        self.books = ["rich dad poor dad","the secret","harry poter"]
        self.authors = ["ankit","apeksha","pooja"]

        # User Section 
        self.localUserId = []

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

            return f"User {uid} Successfully Removed "
        else:

            return f"User {uid} Not present In Database check Again"




        
        

#Application start from here        

app = library_management()     #instance

while True:
    print("1- Admin section\n2 - Local User \n3 - Exit\n")


    ch = input("Enter u r choice:")

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
            print("1 - show All books \n2 - Add book \n3 - Remove Book  \n4 - Remove User \n5 - Logout \n")

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

    elif ch == "2":
        pass
    elif ch == "3":
        print("\n********************* thank you for visitng **************\n")
        break
    else:
        print("\n***************************** Invalid Option ************************\n")
