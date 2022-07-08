def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    # return rgb as list
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def generateColorCode(rgb, back=0):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    if back == 0:
        return '\033[{};2;{};{};{}m'.format(38, r, g, b)
    elif back == 1:
        return '\033[{};2;{};{};{}m'.format(48, r, g, b)


def hex_text(hex_code):
    rgb = hex_to_rgb(hex_code)
    return str(generateColorCode(rgb))


def hex_back(hex_code):
    rgb = hex_to_rgb(hex_code)
    return str(generateColorCode(rgb, 1))


def hexs(hex_text, hex_back):
    text_rgb = hex_to_rgb(hex_text)
    back_rgb = hex_to_rgb(hex_back)
    return str(generateColorCode(text_rgb) + generateColorCode(back_rgb, 1))