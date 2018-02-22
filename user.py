import csv
class user :
    def __init__(self, spy_name, spy_password, spy_age, spy_rating):
        self.name = spy_name
        self.password = spy_password
        self.age = spy_age
        self.rating = spy_rating
        self.status = 'None'
        with open('spy.csv','a') as spy:
            writer = csv.writer(spy)
            writer.writerow([self.name,self.password,self.age,self.rating,self.status])