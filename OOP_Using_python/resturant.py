class Restaurant: # parent class
    """A class representing a standard
    restaurant establishment.
    """

    def __init__(self, restaurant_name:str, cuisine_type:str)->None:
        """Initialize the restaurant with a name,
        cuisine type, and tracker for customers served.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.__total_profit = 0  # private
        self._loss = 0    #protected
        

    def describe_restaurant(self) -> None:
        """Print a summary message displaying
        the restaurant's name and cuisine type
        """
        print(f"Welcome to: {self.restaurant_name} ")
        print(f"Here we serve {self.cuisine_type}  ")

    def open_restaurant(self):
        """Print a message indicating that the
        restaurant is open for business.
        """
        print("Restaurant Open")

    def set_number_served(self, num :int) -> int:
        """Set the total number of customers served 
        to a specific value and return it.
        """
        self.number_served = num
        return self.number_served

    def increment_number_served(self, inc:int)->int:
        """Add a specified amount to the total 
        number of customers served and return it.
        """
        self.number_served += inc
        return self.number_served
    
    def set_profit (self,p) :
        self.__total_profit = p
        
    def get_profit (self) :
        return self.__total_profit
                

class IceCream_Stand(Restaurant): # class inherited (Child class)
    """A specialized subclass of 
    Restaurant representing an ice cream stand.
    """

    def __init__(self, restaurant_name : str, cuisine_type:str):
        """Initialize the ice cream stand, 
        calling the parent constructor and defining flavors.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanila','chocolate','polka','tuity fruity','pistachio','strawberry']

    def display_flavors(self):
        """Loop through and print the
        list of available ice cream flavors.
        """
        print("FALVORS AVAILABLE")
        for i in range(0, len(self.flavors)-1):
            print(self.flavors[i])

    def open_restaurant(self):
        """Override the parent method to
        show that this specific stand is currently closed.
        """
        print("Restaurant closed .")

    def loss_cal(self,l) :
        print(l._loss)
        # --- Execution Code ---
if __name__ == "__main__" :        
    res = Restaurant("Italian Pizza" , "Junk food")
    
    res2 = Restaurant("Chai resort" , "kashmiri chai")
   
    res3 = Restaurant("Lala G Shinwari" , "Desi foods")
   
    print(res.restaurant_name)
    print("="* 50)
    print(res.cuisine_type)
    print("="* 50)
    res.describe_restaurant()
    print("="* 50)
    res2.describe_restaurant()
    print("="* 50)
    res3.describe_restaurant()
    print("="* 50)
    res.open_restaurant()
    print("="* 50)
    print("At 8 am : " ,res.number_served)
    print("="* 50)
    res.number_served = 2
    print("At 10 am : " ,res.number_served)
    print("="* 50)
    print("At 12 am : " ,res.set_number_served(40))
    print("="* 50)
    print("TOTAL customers in a day : " ,res.increment_number_served(80))
    print("="* 50)
    ice = IceCream_Stand("Chaman Icecream" , "Icecream")
    print("="* 50)
    ice.describe_restaurant()
    print("="* 50)
    ice.display_flavors()
    print("="* 50)
    ice.open_restaurant()
    
    res.set_profit(500_000)
    print(f"Total profit is : {res.get_profit()}")
    # print(res.__total_profit)
    print(res._Restaurant__total_profit)
    ice.loss_cal(res)
    
    
