#Assignment 1

class FootballPlayer:
    def __init__(self, name, position, club):
        self.name = name
        self.position = position
        self.club = club
    
    def introduce(self):
        return f"My name is {self.name}, I play as a {self.position} for {self.club}."
    
    def train(self):
        return f"{self.name} is training hard on the pitch!"


class Goalkeeper(FootballPlayer):
    def __init__(self, name, club, clean_sheets):

      
        super().__init__(name, "Goalkeeper", club)
        self.clean_sheets = clean_sheets
    
    def _secret_training(self):
        return f"{self.name} is secretly practicing penalty saves!"
    
 
    def train(self):
        return f"{self.name} is practicing diving and shot-stopping!"


player1 = FootballPlayer("Kevin De Bruyne", "Midfielder", "Manchester City")
player2 = Goalkeeper("Alisson Becker", "Liverpool", 15)

print(player1.introduce())
print(player1.train())
print(player2.introduce())
print(player2.train())


#Assignment 2


class Vehicle:
    def move(self):
        return "Moving in some way..."

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Bike(Vehicle):
    def move(self):
        return "Riding on two wheels 🚴"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

vehicles = [Car(), Bike(), Plane()]

for v in vehicles:
    print(v.move())
