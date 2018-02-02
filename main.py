print 'Welcome!'

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
                spy_online = True

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