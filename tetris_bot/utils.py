import garapa


def is_ingame():
    current_screen_id = garapa.peek(0xffe1)

    return current_screen_id == 0x00


def is_credits():
    current_screen_id = garapa.peek(0xffe1)

    return current_screen_id not in [0x24, 0x25]


def init_joystick():
    for key in ['right', 'left', 'up', 'down', 'a', 'b', 'select', 'start']:
        garapa.set_input(key, 0)
