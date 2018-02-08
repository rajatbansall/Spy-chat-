import spydetail
print 'Welcome to SpyChat'

#Menu
def menu() :
    spy_choice = input("Welcome to Spy chat\n What tasks you want to do ? \n 1.Add a Frnd\n 2.Send Message \n 3. Status Update\n 4. Log Out")
    return spy_choice

def task(choice) :
    if choice == 1:
        # Add a Friend
        print 'Friend has been added'
    elif choice == 2:
        # Send a Message
        print 'Message has been sent'
    elif choice == 3:
        # Status Update
        print 'Status has been set'
    elif choice == 4:
        return 4
    else:
        print 'Maybe you have entered an invalid choice please try again'
        return 0

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
    if spy_name == spydetail.spy_name and spy_password == spydetail.spy_password :
        print 'You are Authenticated'
        return 1
    else :
        print 'Your Provided Informations are not found in our database please sign Up.'
        return 0

#Introduction
while True :
    spy_op = 0
    success = 0
    choice = 0
    #Asking to Log in or Sign up
    spy_op =  input('Please Log In or Sign Up to Continue \n 1. Log In \n 2. Sign Up\n 3.Exit \n')
    if spy_op == 1:
        success = login()
        if success == 1:
            while True :
                choice = menu()
                choice = task(choice)
                if choice == 4 :
                    break
    elif spy_op == 2:
        signup()
    elif spy_op == 3:
        print 'Thanx for using Spychat '
        break
    else:
        print 'You Have Entered a wrong choice try again!'

