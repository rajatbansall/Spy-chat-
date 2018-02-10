import spydetail
print 'Welcome to SpyChat'

#Adding a Friend
def add_friend():
    i = 0
    j = 1

    friend_name = raw_input("Please Enter your friend's name :")
    # Validation on Name
    if len(friend_name) > 0:
        friend_salut = raw_input("What should I call him/her Mr. or Mrs.? :")

        # Validation on Salutation
        if friend_salut == 'Mr.' or friend_salut == 'Mrs.' or friend_salut == 'mr.' or friend_salut == 'mrs.':
            # declaration of New variables
            friend_age = 0
            friend_rating = 0.0

            # Input Age
            friend_age = raw_input("What is your friend's age:")

            # Age Validations
            if friend_age >= '12' and friend_age <= '50':
                # input Ratings
                friend_rating = raw_input('Please enter your friend\'s rating(Max 5.0):')

                # Rating Validations
                if friend_rating > '0.0' and friend_rating <= '5.0':
                    # Successful Registration and Printing Entered Informations
                    print 'Great! your friend has been added successfully'
                    friend_name = friend_salut + friend_name
                    spydetail.spy_friend['friend_name'] = friend_name
                    spydetail.spy_friend['friend_age'] = friend_age
                    spydetail.spy_friend['friend_rating'] = friend_rating
                    print 'Here are the Informations provided by you as below:'
                    #printing friend
                    for friend in spydetail.spy_friend.items():
                        print str(j) + " " + friend[0] + ": " + str(friend[1])
                        i = i + 1
                        j = j + 1
                    return
                else:
                    print 'It seems you have entered a wrong rating please try again.'
                # Rating Validations End

            else:
                print 'I am Sorry !' + ' ' + friend_salut + friend_name + ' ' + 'seems not to be eligible.'
            # Age Validation Ends

        elif friend_salut == 'Mr' or friend_salut == 'Mrs' or friend_salut == 'mr' or friend_salut == 'mrs':
            print 'Please enter dot(.) after salutation'

        else:
            print ' Please enter a valid salutation from given options ! '
        # Salutation Validation Ends

    else:
        print 'Please enter a valid name with atleast 3 characters'
    # Name validation Ends


#Status Update
def status():
    j = 1

    #Displaying Current Status
    print 'your current status is : ' +  spydetail.spy_user['spy_status']

    stat_op = input("Do you want to choose old status or create new ? /n 1.Old Status 2.Create New\n")

    #Printing and asking the custom status that user want to set
    if stat_op == 1:
        print 'Please select a Status from the given list :\n'
        for  i in spydetail.custom_stat :
            print str(j) + ' ' + i
            j = j + 1
        stat_choice = input() - 1
        spydetail.spy_user['spy_status'] = spydetail.custom_stat[stat_choice]
        return 1

    #Setting new status
    elif stat_op == 2:
        new_status = raw_input('Please Enter your new status :')
        spydetail.custom_stat.append((new_status))
        spydetail.spy_user['spy_status'] = new_status
        return 1
    else :
        return 0

#Menu
def menu() :
    spy_choice = input("Welcome to Spy chat\n What tasks you want to do ? \n 1.Add a Frnd\n 2.Send Message \n 3. Status Update\n 4. Log Out")
    success = task(spy_choice)
    if success == 0 :
        return

def task(choice) :
    success = 0
    if choice == 1:
        # Add a Friend
        add_friend()
        menu()

    elif choice == 2:
        # Send a Message
        print 'Message has been sent'

    elif choice == 3:
        # Status Update
        success = status()
        if success == 1 :
            print 'Status has been set'
            print 'Your current status has been set to : ' + spydetail.spy_user['spy_status']
            menu()
        else :
            print 'There was some error in updating your status please try again !'
            menu()

    elif choice == 4:
        return 0
    else:
        print 'Maybe you have entered an invalid choice please try again'
        menu()

#signup function
def signup():
    print 'Sign Up'
    #Asking Name of the Spy
    spy_name = raw_input("Please Enter Your Name:")

    #Validation on Name
    if len(spy_name) > 0:
        spy_salute = raw_input("What should I call you Mr. or Mrs.? :")

        #Validation on Salutation
        if spy_salute == 'Mr.' or spy_salute == 'Mrs.' or spy_salute == 'mr.' or spy_salute == 'mrs.':
            print 'Welcome' + ' ' + spy_salute + spy_name + ' ' + 'Please give us some additional information about yourself.'

            # declaration of New variables
            spy_age = 0
            spy_rating = 0.0
            spy_online = False

            #Asking for password
            spy_password = raw_input("Enter your Password:")

            # Input Age
            spy_age = raw_input("What is your age:")

            # Age Validations
            if spy_age >= '12' and spy_age <= '50' :
                print 'Great!' + ' ' + spy_salute + spy_name + ' ' + 'You look perfectly eligible to become a SpyChat user.'

                # input Ratings
                spy_rating = raw_input('Please enter your rating as a spy (Max 5.0):')

                # Rating Validations
                if spy_rating > '0.0' and spy_rating <= '5.0' :
                    if spy_rating >= '3.0' and spy_rating <= '4.5' :
                        print 'Cool ! It seems you are a Good Spy.'
                    elif spy_rating >= '4.5':
                        print 'Wow ! You are brilliant.'
                    else:
                        print 'It seems you need more experience.'

                    # Successful Registration and Printing Entered Informations
                    print 'Great!' + ' ' + spy_salute + spy_name + ' ' + 'You have successfully registered to SpyChat.'
                    print 'Here are the Informations provided by you as below:'
                    print 'Name :' + ' ' + spy_salute + spy_name
                    print 'Age :' + ' ' + str(spy_age)
                    print 'Rating :' + ' ' + str(spy_rating)
                    login()

                else:
                    print 'It seems you have entered a wrong rating please try again.'
                #Rating Validations End

            else:
                print 'I am Sorry !' + ' ' + spy_salute + spy_name + ' ' + 'You seems to be not eligible to become a SpyChat User.'
            # Age Validation Ends

        elif spy_salute == 'Mr' or spy_salute == 'Mrs' or spy_salute == 'mr' or spy_salute == 'mrs' :
            print 'Please enter dot(.) after salutation'

        else:
            print ' Please enter a valid salutation from given options ! '
        #Salutation Validation Ends

    else:
        print 'Please enter a valid name with atleast 3 characters'
    #Name validation Ends

#Login Function
def login():
    print 'Log In'
    spy_name = raw_input("Please enter your Name:")
    spy_password = raw_input("Please enter your password:")
    if spy_name == spydetail.spy_user['spy_name'] and spy_password == spydetail.spy_user['spy_password'] :
        print 'You are Authenticated'
        return 1
    else :
        print 'Your Provided Informations are not found in our database please sign Up.'
        return 0

#Introduction
while True :
    spy_op = 0
    success = 0
    #Asking fro being a default user or new
    spy_op =  input('Are You an Existing User or New User? \n 1. Existing User  \n 2. New User\n 3.Exit \n')
    if spy_op == 1:
        print 'We have your information stored.'
        success = login()
        if success == 1:
            while True :
                menu()
                break
    elif spy_op == 2:
        signup()
    elif spy_op == 3:
        print 'Thanx for using Spychat '
        break
    else:
        print 'You Have Entered a wrong choice try again!'

