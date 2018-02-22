import spydetail
from steganography.steganography import Steganography
from datetime import datetime
from colorama import Fore, Back, Style
import csv
from user import user
import pandas as pd

print 'Welcome to SpyChat'

global count_friend
count_friend = 0
spy_friend_name = []
spy_friend_age = []
spy_friend_rating = []
spy_friend_online = []
friend_count = [0]

def read_chat(friend_num) :
    selected_friend = int(friend_num) - 1
    print'Chats Done by you with ' + Fore.RED + spy_friend_name[selected_friend]
    for chats in spydetail.spy_user['chats'] :
        if chats['friend_id'] == friend_num :
            print Fore.BLACK + str(chats['message'])
            print Fore.BLUE  + str(chats['time'])
            print Fore.BLACK + str(chats['sent_by_me'])
            print '\n'

def read_msg(friend_num):
    #Reading a Message
    friend_choosen = int(friend_num)
    image_name = raw_input("Enter the name of the image :")
    message = Steganography.decode(image_name)
    new_chat = {
        'friend_id' : friend_num,
        'message': message,
        'time': datetime.now(),
        'sent_by_me': False
    }
    spydetail.spy_user['chats'].append(new_chat)
    print 'Your secret text is : ' + message
    if message== 'SAVE ME' or message == 'SOS' or message =='HELP ME!':
        print 'Spy Need your Help ' + spydetail.spy_user['spy_name']

def send_msg(friend_num):
    # Sending Message
    friend_choosen = int(friend_num)
    message = raw_input("Enter the message you want to send : ")
    original_image = raw_input("What is the name of your image : ")
    output_path = "output.jpg"
    Steganography.encode(original_image, output_path, message)
    chat = {
        'friend_id' : friend_num,
        'message' : message,
        'time' : datetime.now(),
        'sent_by_me' : True
    }
    spydetail.spy_user['chats'].append(chat)
    print 'Message has been encrypted and sent'

#validation function
def selection_validation(validation):
    validation_asci = ord(validation)
    if (validation_asci >= 32 and validation_asci <= 47) or (validation_asci >= 58 and validation_asci <= 126 ) :
        print "Wrong input try again."
        return 0
    else :
        return 1

#Selecting friend
def select_friend():
    k = 0
    i = 1
    success = 0
    while k < friend_count[0]:
        print i
        print "Friend Name : " + spy_friend_name[k]
        print "Friend Age : " + spy_friend_age[k]
        print "Friend Rating : " + spy_friend_rating[k]
        k = k + 1
        i = i + 1
    friend_num = raw_input("Which friend you want to communicate with ? ")
    success = selection_validation(friend_num)

    #Validation of friend's selection
    if success == 0 :
        select_friend()
    else :
        friend_num_int = int(friend_num)
        if friend_num_int > friend_count[0] :
            print "Your selection is exceeding the number of friends. Try Again. "
            select_friend()
        else :
            return friend_num

#Adding a Friend
def add_friend():
    i = 0
    j = 1
    count = 0
    friend_name = raw_input("Please Enter your friend's name :")
    # Validation on Name
    if len(friend_name) > 0:
        friend_salut = raw_input("What should I call him/her Mr. or Mrs.? :")

        # Validation on Salutation
        if friend_salut == 'Mr.' or friend_salut == 'Mrs.' or friend_salut == 'mr.' or friend_salut == 'mrs.':
            # Declaration of New variables
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
                    spy_friend_name.append(friend_name)
                    spy_friend_age.append(friend_age)
                    spy_friend_rating.append(friend_rating)
                    friend_count[0] = friend_count[0] + 1
                    count = friend_count[0]
                    print 'Here are the Informations provided by you as below:'

                    #Printing Friend
                    print "Name : " + friend_name
                    print "Age : " + str(friend_age)
                    print "Rating: " + str(friend_rating)
                    print 'Total Number of friends you have : ' + str(count)
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
def status(logged_in_user,id_counter):
    j = 1
    l = 0
    #Displaying Current Status
    print 'your current status is : ' +  logged_in_user[4]
    with open('spy.csv','a') as spy:
        writer = csv.writer(spy)
        stat_op = input("Do you want to choose Custom Stat or create new ? /n 1.Custom Status 2.Create New\n")

        #Printing and asking the custom status that user want to set
        if stat_op == 1:
            print 'Please select a Status from the given list :\n'
            for  i in spydetail.custom_stat :
                print str(j) + ' ' + i
                j = j + 1
            stat_choice = input() - 1

            #Updating Custom Status
            if stat_choice >= 0 and stat_choice < j - 1 :
                logged_in_user[4] = spydetail.custom_stat[stat_choice]
                return 1
            else :
                print 'You have entered a wrong choice'
                success = status(logged_in_user,id_counter)
                return success

        #Setting new status
        elif stat_op == 2:
            new_status = raw_input('Please Enter your new status :')
            logged_in_user[4] = new_status
            writer.writecolumn(logged_in_user)
            return 1
        else :
            return 0

#Menu
def menu(logged_in_user, id_counter) :
    spy_choice = input("Welcome to Spy chat\n What tasks you want to do ? \n 1.Add a Frnd\n 2.Send a Secret Message\n 3.Read a Secret Message \n 4 Status Update\n 5. Read Chat From a User \n 6. Log Out \n")
    success = task(spy_choice, logged_in_user, id_counter)
    if success == 0 :
        return

def task(choice, logged_in_user, id_counter) :
    success = 0
    if choice == 1:
        # Add a Friend
        add_friend()
        menu()

    elif choice == 2:
        # Send a Message
        num = select_friend()
        send_msg(num)
        menu()

    elif choice == 3:
        #Read a Message
        num = select_friend()
        read_msg(num)

    elif choice == 4:
        # Status Update
        success = status(logged_in_user, id_counter)
        if success == 1 :
            print 'Status has been set'
            print 'Your current status has been set to : ' + logged_in_user[4]
            menu(logged_in_user,id_counter)
        elif success == 0 :
            print 'There was some error in updating your status please try again !'
            menu(logged_in_user)

    elif choice == 5:
        # Read Chats
        num = select_friend()
        read_chat(num)
        menu()


    elif choice == 6:
        #Logout
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
                    spy = user(spy_name, spy_password, spy_age, spy_rating)
                    print 'Great!' + ' ' + spy_salute + spy.name  + ' ' + 'You have successfully registered to SpyChat.'
                    print 'Here are the Informations provided by you as below:'
                    print 'Name :' + ' ' + spy_salute + spy.name
                    print 'Age :' + ' ' + str(spy.age)
                    print 'Rating :' + ' ' + str(spy.rating)

                    return 1
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
    found = False
    id_counter = 0
    print 'Log In'
    with open('spy.csv', 'rb') as spy_user:
        reader = csv.reader(spy_user)
        spy_name = raw_input("Please enter your Name:")
        spy_password = raw_input("Please enter your password:")
        for row in reader:
            id_counter = id_counter + 1
            if spy_name == row[0] and spy_password == row[1] :
                found = True
                logged_in_user = row
                break
        if found == True:
            print 'You are Authenticated'
            menu(logged_in_user, id_counter)
        else :
            print 'Your Provided Informations are not found in our database please sign Up.'
            return 0

#Introduction
while True :
    success = 0
    #Asking fro being a default user or new
    spy_op =  raw_input('Are You an Existing User or New User? \n 1. Existing User  \n 2. New User\n 3.Exit \n')
    success = selection_validation(spy_op)
    if success == 0:
        print 'wrong selection try again'
    else :
        if spy_op == '1':
            print 'We have your information stored.'
            success = login()
            if success == 1 :
                while True :
                    menu()
                    break
        elif spy_op == '2':
            success = signup()
            if success == 1 :
                login()
        elif spy_op == '3':
            print 'Thanx for using Spychat '
            break
        else:
            print 'You Have Entered a wrong choice try again!'

