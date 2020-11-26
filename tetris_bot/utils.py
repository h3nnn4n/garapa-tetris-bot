import garapa


def is_ingame():
    current_screen_id = garapa.peek(0xffe1)

    return current_screen_id == 0x00


def is_credits():
    current_screen_id = garapa.peek(0xffe1)

    return current_screen_id not in [0x24, 0x25]
