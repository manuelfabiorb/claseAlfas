class Car:

    color = None
    motor = True
    wheels = 4
    gasoline = 10
    seats = 5
    brand = "Chevrolette"
    moving = False


    def _init_(self):
        print("A car has been created")
        
    def move(self):
        if(self.wheels==4 and self.gasoline>0 and self.motor == True):
             print("I'm moving")
             self.moving = True
             self.gasoline -=1
        else:
            print("I don't have wheels or gas or motor to move")

    def back(self):
        if(self.moving == False and self.gasoline > 0 and self.motor):
            print("I'm backing")
        else:
            print("I don't have wheels or gas or motor or I'm moving")

    def stop(self):
        if(self.moving == True):
            print("I stop")
        else:
            print("I'm not moving")

vocho = Car()
tsuru = Car()

print("Soy vocho")
vocho.stop()
vocho.move()
vocho.back()
vocho.stop()