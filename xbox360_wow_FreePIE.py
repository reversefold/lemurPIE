#a, x, y, b
#1, 2, 3, 4
#5, 6, 7, 8
#9, 0, -, =
#Numpad 0, Numpad ., Sh-z, Sh-x

#b, Sh-`, Mouse 4, `

if starting:
    from lemur.controller import XBox360
    from xbox360_wow import WowController

    controller = XBox360(xbox360[0])
    wow_controller = WoWController(controller)

wow_controller.tick()
