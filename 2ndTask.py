class Device:
    def change_channel(self, channel):
        pass

class TV(Device):
    def change_channel(self, channel):
        print(f"TV channel changed to {channel}")

class Radio(Device):
    def change_channel(self, channel):
        print(f"Radio frequency set to {channel}")

class RemoteControl:
    def __init__(self, device):
        self.device = device

    def change_channel(self, channel):
        self.device.change_channel(channel)

tv = TV()
remote = RemoteControl(tv)
remote.change_channel(5)  # Output: TV channel changed to 5

radio = Radio()
remote = RemoteControl(radio)
remote.change_channel("FM 98.5")  # Output: Radio frequency set to FM 98.5
