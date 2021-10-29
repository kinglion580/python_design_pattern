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


class StereoWithCDComand(Command):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()


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


class Stereo:
    def on(self):
        print("Stereo on")

    def off(self):
        print("Stereo off")

    def set_cd(self):
        print("set cd")

    def set_volume(self, volume):
        print("set volume " + str(volume))


class SimpleRemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def button_was_pressed(self):
        if self._command is not None:
            self._command.execute()


class MyRemoteControl:
    def __init__(self):
        nocommand = NoCommand()

        self._oncommand = [nocommand] * 7
        self._offcommand = [nocommand] * 7

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
    stereo = Stereo()
    light_command = LightCommand(light)
    light_off_command = LightOffCommand(light)
    gd_command = GarageDoorCommand(garagedoor)
    gd_off_command = GarageDoorOffCommand(garagedoor)
    stereo_command = StereoWithCDComand(stereo)
    stereo_off_command = StereoOffCommand(stereo)
    remote = MyRemoteControl()
    remote.set_command(1, light_command, light_off_command)
    remote.set_command(3, gd_command, gd_off_command)
    remote.set_command(4, stereo_command, stereo_off_command)
    remote.on_button_was_pressed(1)
    remote.off_button_was_pressed(3)
    remote.on_button_was_pressed(2)
    remote.on_button_was_pressed(4)
    remote.off_button_was_pressed(4)
    print(remote)
