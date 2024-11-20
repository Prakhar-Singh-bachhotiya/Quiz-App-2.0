from random import *
logged=False
log_user=''

def attempt():
    total=0

    with open("question.txt","r") as quiz:
        ques = quiz.readlines()
        
        for i in ques:
            i=i.replace('\n','')
            li=i.split(",")
            print(li[0])
            for ops in range(1,5):
                print(li[ops])
            ans=input("Enter Answer (A-D) :").upper()
            if ans == li[5]:
                total+=10
    with open("score.txt","a") as result:
        result.write(f"{log_user},{total}\n")


def result():
    with open ("score.txt","r") as score:
        scr=score.readlines()
        marks=0
        for i in scr:
            i=i.replace('\n','')
            li=i.split(',')
            if li[0]==log_user:
                marks=li[1]
        print(f"{log_user} has scored {li[1]} percent")
            



def register():
    with open ('register.txt','a') as reg:
        name=input("Enter Username:")
        pwd=input("Enter password:")
        roll=input("Enter Enrollment Number:")
        clg=input("Enter College Name:")
        reg.write(f"{roll},{name},{pwd},{clg}\n")
    with open('logindetails.txt','a') as log:
        log.write(f"{roll},{pwd}\n")

def login():
    global logged
    global log_user
    user=input("Enter Enrollment Number: ")
    
    with open('logindetails.txt','r') as log:
        us=log.readlines()
        for i in us:
            i=i.replace('\n','')
            li=i.split(',')

            if li[0]==user:
               count =3
               while (True):
                    
                    password=input("Enter Password: ")
                    if li[1]==password:
                        print('Login Successful!!!')
                        logged=True
                        log_user=user
                        break
                    else:
                        print(f"Incorrect Password!!! \n  {count} attempt left ")
                        
                        if count==0:
                            print("You have exceeded maximum number of attempts... Try again Next Time!")
                            break
                        count-=1    
                        print("Enter correct Password:")
            else:
                print("Incorrect Username!!!")   
                print("Please Try Again") 
                login()

def login_page():
    loop=True
    while(loop):
        print("1.Attempt quiz")
        print('2.Show Result')
        print("3.Exit")
        ch1=int(input("Enter your choice (1-3): "))
        if ch1==1:
            print()
            attempt()
            loop=bool(input('Do you want to continue True or False : '))
            if loop == False:
                break
        elif ch1==2:
            print()
            result()
            break
            
        elif ch1==3:
            print("....Thanking You For Using Quiz Master....")
            exit()
        else:
            print("Please choose a valid option!!!")

loop=True
while(loop==True):
    print("1.Register")
    print("2.Login")
    print('3.Exit')
    ch=int(input("Enter your choice (1-3): ")) 

    if ch==1:
        print()
        register()
        print()
        loop=bool(input('Do you want to continue True or False'))
        if loop== False:
            break
    elif ch==2:
        print()
        login()
        print()
        login_page()
        print()
        break
        
    elif ch==3:
        print("....Thanking You For Using Quiz Master....")
        exit()
    else:
        print("Please choose a valid option!!!")
    