import random

class Insect:
  

    # def __init__(self):
    #     self.wings = 2
    #     self.legs=4
    #     self.length=0
    def __init__(self,w,l):
        self.wings = w
        self.legs= l
        self.length=0
    
    def length_of_flight(self):

        self.length = random.randint(1,10) 
            
    def get_length(self):
        return self.length

