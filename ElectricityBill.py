class ElectricityBill:
    def __init__(self,name,units):
        self.name = name
        self.units = units 
        temp = 0
        while(units!=0):
            if(units>300):
                temp+=(units-300)*4.25
                units = 300
            elif(units>30):    
                temp+=(units-30)*3
                units = 30
            else:
                temp += units*1.5
                units = 0

        if(temp>500):
            temp += (temp* 0.15)
        self.bill = temp      

    def printBill(self):
        print(self.name,"\t",str(self.units),"\t",str(self.bill))    



user1 = ElectricityBill("Gopal", 30)
user2 = ElectricityBill("Sandip", 50)
user3 = ElectricityBill("Paresh", 300)

arr = [user1, user2, user3]

print("Name\tUnits\tBill")
for user in arr:
    user.printBill()