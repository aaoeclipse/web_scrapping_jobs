import re

class Card:
    
    def __init__(self, title, location, ammount, description):
        self.title = title
        self.location = location
        self.ammount = ammount
        self.getMinMax(ammount)
        self.description = description

    def getMinMax(self, ammount):
        if ammount is 'unknown':
            self.minimum = 0
            self.maximum = 0
            return

        separated_ammount = ammount.split('-')
        if len(separated_ammount) == 1:
            self.minimum = re.sub("\D", "", separated_ammount[0])
            self.maximum = re.sub("\D", "", separated_ammount[0])
            return 

        self.minimum=re.sub("\D", "", separated_ammount[0])
        self.maximum=re.sub("\D", "", separated_ammount[1])
    
    def __str__(self):
        return '{}\n{}\n{}\n{}\n'.format(self.title,self.location,self.ammount,self.description)