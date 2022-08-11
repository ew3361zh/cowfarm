class Pen():
    def __init__(self, breed, number_of_cows, feed_type, amount_of_feed_per_cow, milk_yield):
        self.breed = breed  # if breed feed/milk yield is more standard could create sub class objects
        self.number_of_cows = number_of_cows
        self.feed_type = feed_type
        self.amount_of_feed_per_cow = amount_of_feed_per_cow
        self.milk_yield = milk_yield

    def __str__(self):
        return f'This pen contains {self.number_of_cows} {self.breed}s that consume {self.feed_type}'
        
        
        