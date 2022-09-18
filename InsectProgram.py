import InsectClass as c


# The main function.
def main():
       # Create an object from the Insect  class
    #    housefly = c.Insect()  
    #    mosquito=c.Insect()  
        housefly = c.Insect(3,4)  
        mosquito=c.Insect(2,4)  
        l1=housefly.length_of_flight()
        l2=mosquito.length_of_flight()

       # print(housefly.wings)

        print("length of miles covered by housefly",housefly.get_length())  
        print("length of miles covered by mosquito",mosquito.get_length())  

# Call the main function.

main()     