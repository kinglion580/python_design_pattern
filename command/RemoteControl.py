class Command:
    def execute(self):
        pass


class LightCommand(Command):
    def __init__(self, light):
        self.__light = light

    def execute(self):
        self.__light.on()


class Light:
    def on(self):
        print("light on")


class SimpleRemoteControl:
    def __init__(self):
        self.__command = None

    def set_command(self, command):
        self.__command = command

    def button_was_pressed(self):
        if self.__command is not None:
            self.__command.execute()


def test():
    light = Light()
    command = LightCommand(light)
    remote = SimpleRemoteControl()
    remote.set_command(command)
    remote.button_was_pressed()


