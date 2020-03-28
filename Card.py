import re

class Card:
    
    def __init__(self, title, location, ammount, description):
        ''' Initilazies the class with the given values, it also adds the minmum and maximum of the salary '''
        self.title = title
        self.location = location
        self.ammount = ammount
        self.getMinMax(ammount)
        self.description = description

    def getMinMax(self, ammount):
        ''' transform the ammount in integers'''
        # if it's unknown then we set them to 0
        if ammount is 'unknown':
            self.minimum = 0
            self.maximum = 0
            return

        # we separate into two by using the -, examlpe $40 - $200 is going to be [0] = $40, [1] = $200
        separated_ammount = ammount.split('-')
        # if it didn't manage to separate it means ther is only one value ex. $15
        if len(separated_ammount) == 1:
            self.minimum = int(re.sub("\D", "", separated_ammount[0]))
            self.maximum = int(re.sub("\D", "", separated_ammount[0]))
            return 

        # we then remove the dollar sign and every other string that is not a number
        self.minimum=int(re.sub("\D", "", separated_ammount[0]))
        self.maximum=int(re.sub("\D", "", separated_ammount[1]))

    
    def __str__(self):
        ''' This is the standard method to return a string representation of the class '''
        return '{}\n{}\n{}\n{}\n'.format(self.title,self.location,self.ammount,self.description)