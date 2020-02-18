class Headphone_Device:

    powerOn= None
    volume = None
    marca = "Nokia"

    def __init__(self):
        print("A device has been created")

    def start(self):
        if(self.powerOn == True):
            print("Hello")
        else:
            print("No battery, please charge")
    
    def vol(self):
        if(self.volume == "+"):
            print("adding volume")
        elif(self.volume == "-"): 
            print("lowing volume")

            