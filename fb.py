import time
import datetime
Database={}
class Data(object):
    def __init__(self):
        self.username="default"
        self.password="1234567890"
        self.t=0
    def get_Details(self,username,password):
        if username in Database:
            print "\t\t\tSorry the Username already Exists\n"
            return
        flag = 0
        flag1 = 0
        for i in password:
            if(i>='A' and i<='Z'):
                flag=1
            elif(i>='0' and i<='9'):
                flag1=1
        if((not flag) or (not flag1)):
            raise Exception("\t\tInvalid Password")
        self.username=username
        self.password=password
        self.t=0
while(1):
    n = int(raw_input("\t1.Create new account\n\t2.Login\n\t3.Log Out\n\t4.Authenticate\n\t5.Exit\n\tEnter Your choice :" ))
    if(n==1):
        user = raw_input("\t\tEnter Username : ")
        passw = raw_input("\t\tEnter Password : ")
        s1 = Data()
        try:
            s1.get_Details(user,passw)
        except Exception as e:
            print e
        else:
            Database[user]=s1
    elif(n==2):
        user = raw_input("\t\tEnter Username : ")
        passw = raw_input("\t\tEnter Password : ")
        if user in Database:
            if passw == Database[user].password:
                if(Database[user].t!=0):
                    print "\t\t\tYou are already Logged In!!!"
                else:
                    print "\t\t\tYou are Logged In successfully!!!"
                    t = datetime.datetime.now()
                    k = (t.hour*3600) + (t.minute*60) + (t.second)
                    Database[user].t=k
            else:
                print "\t\t\tSorry Incorrect Details Try again!!!"
        else:
            print "\t\t\tSorry Incorrect Details Try again!!!"
    elif(n==3):
        user = raw_input("\t\t\tEnter Username : ")
        passw = raw_input("\t\t\tEnter Password : ")
        if user in Database:
            if passw == Database[user].password:
                if(Database[user].t==0):
                    print "\t\t\tYou are not Logged in"
                    continue
                print "\t\t\tYou are Logged Out successfully!!!"
                Database[user].t=0
            else:
                print "\t\t\tSorry Incorrect Details Try again!!!"
        else:
            print "\t\t\tSorry Incorrect Details Try again"
    elif(n==5):
        break
    elif(n==4):
        user = raw_input("\t\tEnter Username : ")
        l = datetime.datetime.now()
        j = (l.hour*3600) + (l.minute*60) + l.second
        if user in Database:
            if(j-Database[user].t>30 and Database[user].t):
                print "\t\t\tYour session is expired "
                print "\t\t\tYou are Logged Out successfully"
                Database[user].t=0
            else:
                print "\t\t\tYou are Logged In!!!"
        else:
            print "\t\t\tSorry Incorrect Details try again!!!"
