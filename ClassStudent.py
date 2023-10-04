class Student:
    def __init__(self):
        self.name = ""
        self.rollNo = 0
        self.address = ""
        self.percent = 0

    def getDetails(self):
        self.name = input("Enter Your Name: ")    
        self.rollNo = int(input("Enter Your Roll No: "))   
        self.address = input("Enter Address: ")    
        self.percent = float(input("Enter Percentage: "))

    def displayDetails(self):
        print("\nName:", self.name)
        print("Roll No:", self.rollNo)
        print("Address:", self.address)
        print("Percent:", self.percent)
        self.result = ""
        if(self.percent >= 75):
            self.result = "Distinction"
        elif(self.percent>=60 and self.percent<70):
            self.result = "First Class"
        elif(self.percent>=40 and self.percent<60):
            self.result = "Second Class"
        elif(self.percent<40):
            self.result = "Failed"   

        print("Result:", self.result)     


s1 = Student()        
s1.getDetails()
s1.displayDetails()