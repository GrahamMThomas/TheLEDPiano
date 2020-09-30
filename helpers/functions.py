def hex_to_rgb(hex_code):
    stripped_hex = hex_code.lstrip("#")
    return tuple(int(stripped_hex[i : i + 2], 16) for i in (0, 2, 4))