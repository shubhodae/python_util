from abc import ABC, abstractmethod


class ElectricAppliance(ABC):

    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass


class LightBulb(ElectricAppliance):

    def switch_on(self):
        print("Bulb swithced on ....")

    def switch_off(slef):
        print("Bulb switched off ....")


class Fan(ElectricAppliance):

    def switch_on(self):
        print("Fan swithced on ....")

    def switch_off(slef):
        print("Fan switched off ....")


class ElectricSwtich:
    on = False

    def __init__(self, appliance: ElectricAppliance) -> None:
        self.appliance = appliance

    def press(self):
        print("\n\nSWICH PRESSED")
        if False == self.on:
            self.on = True
            self.appliance.switch_on()
        else:
            self.on = False
            self.appliance.switch_off()



lb = LightBulb()

e = ElectricSwtich(lb)
e.press()
e.press()
e.press()
e.press()


f = Fan()

e = ElectricSwtich(f)
e.press()
e.press()
e.press()
e.press()