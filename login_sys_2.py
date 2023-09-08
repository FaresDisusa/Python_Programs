programme = True 
tst_user = False
age_user = False
sign_up_sys = False
pass_vef=True
data = {
    "FaresDisusa" : "bubulette 1998",
    "bouzma1998" : "1234567890",
}
while programme:
    sign_up_sys=False
    print("WELCOME TO DISUSA LOGIN / SIGNIN INTERFACE ")
    home= input("sign-up or login ? :")
    if home == "sign-up":
        while True:
            print("Sign-up interface : ")
            new_user= input("Enter a username : ")
            if data.get(new_user) :
                print("Username already used")
                new_user = None 
                continue
            else :
                print("Username registered successfully ! ")
                tst_user=True
                break
        while tst_user:
            new_pass=input("Please enter your new password : ")
            if len(new_pass) < 4 :
                print("please choose a password of at least 4 characters")
                continue
            else:
                print("password registered successfully !")
                data[new_user] = new_pass
                age_user = True
                break
        while age_user:
            age = input("please enter your age : ")
            try:
                age = int(age)
                if 11 >= age or age >= 120 :
                    print("Please enter an age between 12 and 120")
                    continue
                else :
                    print("Well done ", new_user, " you have created a new disusa account !")
                    sign_up_sys = True
                    break
            except:
                print("Please enter your age with numbers ")
                continue
    if home == "login":
        print("Login interface :")
        while pass_vef :
            pass_vef=True
            user_login= input("Please enter your username : ")
            if data.get(user_login) :
                print("Username successfully accepted ! ")
                pass_login=input("Please enter your password : ")
                for user, pswrd in data.items():
                    if pswrd == pass_login:
                        print("you are successfully connected to" '{user_login}')
                        sign_up_sys=True
                        pass_vef=False
                        break 
                    else:
                        print("Incorrect password please try again")
                        continue
            else:
                print("Incorrect username please enter an existing username or create a new account")
                sign_up_sys=True
                break
    if home == "exit":
        break
    if home != "login" and home != "sign-up" and home != "exit" :
        print("Command not found...")
        continue
    elif sign_up_sys :
        continue

       
                
        
