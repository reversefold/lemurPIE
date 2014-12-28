if starting:
    from lemur.controller import XBox360
    from lemur.xbox360_wow import key_maps, axis_maps, WoWController

    import lemur.action
    lemur.action.keyboard = keyboard
    lemur.action.mouse = mouse

    controller = XBox360(xbox360[0])
    wow_controller = WoWController(controller, key_maps(Key), axis_maps(Key))

wow_controller.tick()
