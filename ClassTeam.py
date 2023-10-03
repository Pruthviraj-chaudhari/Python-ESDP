class Team:
    def __init__(self,country,name,matches,age,battingAvg, ballingAvg):
        self.country = country
        self.name = name
        self.matches = matches
        self.age = age
        self.battingAvg = battingAvg
        self.ballingAvg = ballingAvg


t1 = Team("India", "Sachin", 295, 30, 45.51, 53.00)
t2 = Team("Australia", "Ricky", 160, 28, 41.00, 67.00)
t3 = Team("India", "Saurav", 230, 31, 40.95, 30.00)

team = [t1, t2, t3]

for i in team:
    print(i.country + " " + i.name + " " + str(i.matches) + " " + str(i.age) + " " + str(i.battingAvg) + " " + str(i.ballingAvg))

        