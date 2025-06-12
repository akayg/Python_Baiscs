class Vehicle :
    def start(self):
        print("Vehicle is Starting...")
    
class Car(Vehicle):
    def start(self):
        print("Car is Starting...")
    def fuel(self):
        print ('Car is Petrol Powered.')


c1= Car()
c1.start()
c1.fuel()