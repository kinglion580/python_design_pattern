class Command:
    def execute(self):
        raise NotImplementedError("Command subclass must implement execute()")


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


class GarageDoorOffCommand(Command):
    def __init__(self, garagedoor):
        self.__garagedoor = garagedoor

    def execute(self):
        self.__garagedoor.down()


class NoCommand(Command):
    def execute(self):
        print("no command")


class Light:
    def on(self):
        print("light on")

    def off(self):
        print("light off")


class GarageDoor:
    def up(self):
        print("GarageDoor up")

    def down(self):
        print("GarageDoor down")


class SimpleRemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def button_was_pressed(self):
        if self._command is not None:
            self._command.execute()


class RemoteControl:
    def __init__(self):
        self._oncommand = []
        self._offcommand = []

        for _ in range(7):
            self._oncommand.append(nocommand)
            self._offcommand.append(nocommand)

    def set_command(self, slot: int, oncommand: Command, offcommand: Command):
        self._oncommand[slot] = oncommand
        self._offcommand[slot] = offcommand

    def on_button_was_pressed(self, slot):
        self._oncommand[slot].execute()

    def off_button_was_pressed(self, slot):
        self._offcommand[slot].execute()

    def __str__(self):
        info = "\n--------- Remote Control ---------\n"
        for i in range(len(self._oncommand)):
            info += "[slot " + str(i) + "] " + self._oncommand[i].__class__.__name__ + "   " + \
                    self._offcommand[i].__class__.__name__ + "\n"
        return info


def test():
    light = Light()
    garagedoor = GarageDoor()
    light_command = LightCommand(light)
    light_off_command = LightOffCommand(light)
    gd_command = GarageDoorCommand(garagedoor)
    gd_off_command = GarageDoorOffCommand(garagedoor)
    remote = RemoteControl()
    remote.set_command(1, light_command, light_off_command)
    remote.set_command(3, gd_command, gd_off_command)
    remote.on_button_was_pressed(1)
    remote.off_button_was_pressed(3)
    remote.on_button_was_pressed(2)
    print(remote)
