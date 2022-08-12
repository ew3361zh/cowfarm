class Pen():
    def __init__(self, 
                breed, 
                number_of_cows, 
                feed_type, 
                amount_of_feed_per_cow, 
                feed_cost_per_pound, 
                q1_milk_yield,
                q2_milk_yield,
                q3_milk_yield,
                q4_milk_yield):
        self.breed = breed  # if breed feed/milk yield is more standard could create sub class objects
        self.number_of_cows = number_of_cows
        self.feed_type = feed_type
        self.amount_of_feed_per_cow = amount_of_feed_per_cow
        self.feed_cost_per_pound = feed_cost_per_pound
        self.q1_milk_yield = q1_milk_yield
        self.q2_milk_yield = q2_milk_yield
        self.q3_milk_yield = q3_milk_yield
        self.q4_milk_yield = q4_milk_yield

    def __str__(self):
        return f'This pen contains {self.number_of_cows} {self.breed}s that consume {self.feed_type}'
        
        
        