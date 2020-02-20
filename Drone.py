"""helices
bateria
color
tanque"""

class Drone:

    helices = 4
    bateria = 50
    color = "Blanco"
    tanque = 70
    despegue = False
    aterrizar = True

    def encender(self):
        if(self.bateria > 15):
            print("Power On")
        elif(self.bateria <= 5):
            print("No battery, please charge")
        else:
            print("Power Off, Goodbye")

    def takeOff(self):
        if(self.)

    def volar(self):
        if(self.despegue == True and self.helices == True and self.bateria > 5 and self.tanque > 10):
            print("I'm flying")
            self.bateria -= 1
            self.tanque -= 1
        else:
            print("I haven't take off yet, or one of my propellers its not working, or battery and/or tank are low")
    
    def cargarGas(self):
        if()

    def apagar(self):

    def aterrizar(self):

    def mostrarGas(self):
