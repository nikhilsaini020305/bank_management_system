import json
import random
import string
from pathlib import Path
class Bank :
    database = 'data1.json'
    data=[]
    try:
        if Path(database).exists(): 
            with open(database)as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an execption occured as {err}") 
    @classmethod
    def __update(cls):
        with open (cls.database,'w')as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return"".join(id)



    def createaccount(self):
        info={
            "name":input("Tell your name :- "),
            "age":int(input("tell your age :- ")),
            "email":input("tell your email :- "),
            "pin":int(input("Tell your 4 nimber pin :- ")),
            "accountNo": Bank.__accountgenerate(),
            "balance":0
        }
        if info['age']<18 and len(str(info['pin']))==4:
            print("sorry you cannot create your account")
        else: 
            print("account has been created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please note down your account number ")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        account=input("please tell your account number ")
        pin=int(input("please tell your pin aswell "))
        userdata=[i for i in Bank.data if i['accountNo']==account and i['pin']==pin]
        print(userdata)
        if userdata==False:
            print("sorry no data Found")
        else:
            amount=int(input('how much you want to depoit '))
            if amount>10000 or amount<0:
                print("Sorry the amount is too much you can deposit below 10000 and above the 0")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print("Bank Deposit successfully")

    def withdrawing(self):
            account=input("please tell your account number ")
            pin=int(input("please tell your pin aswell "))
            userdata=[i for i in Bank.data if i['accountNo']==account and i['pin']==pin]
            print(userdata)
            if userdata==False:
                print("sorry no data Found")
            else:
                amount=int(input('how much you want to withdraw '))
                if userdata[0]['balance']>10000 or amount<0:
                    print("Sorry you dont have that much money")
                else:
                    userdata[0]['balance']-=amount
                    Bank.__update()
                    print("Amount withdraw successfully")
    def details(self):
            account=input("please tell your account number ")
            pin=int(input("please tell your pin aswell "))
            userdata=[i for i in Bank.data if i['accountNo']==account and i['pin']==pin]
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")
    def updating(self):
            account=input("please tell your account number ")
            pin=int(input("please tell your pin aswell "))
            userdata=[i for i in Bank.data if i['accountNo']==account and i['pin']==pin]
            if userdata==False:
                print("no such user found ")
            else:
                print("you cannot the age ,account number ,balance")
                print("Fill the details for change or leave it empty if no change")
                newdata={
                    "name":input("please tell new name or press enter : "),
                    "email":input("please tell your new email or press enter to skip : "),
                    "pin":input("enter new Pin or press enter to skip : ")
                }
                if newdata["name"]=="":
                    newdata["name"]=userdata[0]['name']
                if newdata["email"]=="":
                    newdata["email"]=userdata[0]['email']
                if newdata["pin"]=="":
                    newdata["pin"]=userdata[0]['pin']        
                newdata['age']=userdata[0]['age']
                newdata['accountNo']=userdata[0]['accountNo']
                newdata['balance']=userdata[0]['balance']
                if type(newdata['pin'])==str:
                    newdata['pin']=int(newdata['pin'])
                for i in newdata:
                    if newdata[i]==userdata[0][i]:
                        continue
                    else:
                        userdata[0][i]=newdata[i]
                Bank.__update()
                print("details update successfully")

    def deleting(self):
        account=input("please tell your account number ")
        pin=int(input("please tell your pin aswell "))
        userdata=[i for i in Bank.data if i['accountNo']==account and i['pin']==pin]
        if userdata==False:
            print("sorry no such data exist")
        else:
            check=input("press y if you actually want to delet the account or press n : ")
            if check=='n' or check=="N":
                print("bypassed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted succefully ")
                Bank.__update()

user= Bank()    
print("Press 1 forcasting an account")
print("Press 1 for Depositing the money in the bank ")
print("Press 1 for withdrawing the money ")
print("Press 1 for details")
print("Press 1 for updating the details")
print("Press 1 for deleting your account")
check=int(input("Tell your response :- "))
if check ==1:
    user.createaccount()
if check==2:
    user.depositmoney()
if check==3:
    user.withdrawing()
if check==4:
    user.details()
if check ==5:
    user.updating()
if check==6:
    user.deleting()