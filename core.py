import os.path
username =input("Enter username")
Password =input("Enter Password")
if os.path.isfile(username + '.txt') :
    file = open(username +'.txt', "r")
    text = file.readlines()
    if Password == text[1] :
        print("Login succesfull")
    else:
        print("Incorrect password")
else :
    print("File doesn't exist")
    print("Creating new user file")
    nf = open(username + ".txt" , "x")
    nf.write(username +"\n")
    nf.write(Password)
    print("File created")
    nf.close()
    nfr = open(username + ".txt" , "r")
    print(nfr.read())
