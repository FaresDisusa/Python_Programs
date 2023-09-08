systeme = True 
while systeme:
    acceuil = input("registration or connection ? : ")
    if acceuil == "registration" :
        print("You are in the registration interface")
        user_id2 = input("enter a username : ")
        if user_id2 == "exit":
           break 
        password2 = input("enter a password : ")
        if password2 == "exit":
         break 
        age_utilisateur = input("How old are you ? : ")
        try:
            age_utilisateur = int(age_utilisateur)
            if 11 >= age_utilisateur or age_utilisateur >= 100 :
                print("Please enter an age between 12 and 100")
            else :
                print("Well done ", user_id2, " you have created a new disusa account !")
        except:
            print("Please enter your age with numbers... ")
       
    if acceuil == "connection" :
        print("You are in the login interface")
        user_id = input("enter your username : ")
        password = input("enter your password : ")
        if  user_id2 == user_id and password2 == password :
            print("You are connected to ", user_id2)
        if  user_id != user_id2 and password == password2 :
            print ("Username incorrect or not found")
        if  user_id == user_id2 and password != password2 :
            print ("Password incorrect or not found")
        if  user_id != user_id2 and password != password2:
            print("Password and username incorrect or not found")
        if password == "exit":
            break  
        if user_id == "exit":
            break 
    if acceuil == "exit":
        break
    if acceuil != "connection" and acceuil != "registration" and acceuil != "exit" :
        print("command not found...")
