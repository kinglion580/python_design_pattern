class Command:
    def execute(self):
        pass


class LightCommand(Command):
    def __init__(self, light):
        self.__light = light

    def execute(self):
        self.__light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.__light = light

    def execute(self):
        self.__light.off()


class GarageDoorCommand(Command):
    def __init__(self, garagedoor):
        self.__garagedoor = garagedoor

    def execute(self):
        self.__garagedoor.up()


class Light:
    def on(self):
        print("light on")

    def off(self):
        print("light off")


class GarageDoor:
    def up(self):
        print("GarageDoor up")


class SimpleRemoteControl:
    def __init__(self):
        self.__command = None

    def set_command(self, command: Command):
        self.__command = command

    def button_was_pressed(self):
        if self.__command is not None:
            self.__command.execute()


class RemoteControl:
    def __init__(self):
        self.__oncommand = []
        self.__offcommand = []

        nocommand = Command()

        for i in range(len(self.__oncommand)):
            self.__oncommand[i] = nocommand
            self.__offcommand[i] = nocommand

    def set_command(self, slot: int, oncommand: Command, offcommand: Command):
        self.__oncommand[slot] = oncommand
        self.__offcommand[slot] = offcommand

    def on_button_was_pressed(self, slot):
        self.__oncommand[slot].execute()

    def off_button_was_pressed(self, slot):
        self.__offcommand[slot].execute()


def test():
    light = Light()
    garagedoor = GarageDoor()
    light_command = LightCommand(light)
    light_off_command = LightOffCommand(light)
    gd_command = GarageDoorCommand(garagedoor)
    remote = SimpleRemoteControl()
    remote.set_command(light_command)
    remote.button_was_pressed()
    remote.set_command(light_off_command)
    remote.button_was_pressed()
    remote.set_command(gd_command)
    remote.button_was_pressed()

