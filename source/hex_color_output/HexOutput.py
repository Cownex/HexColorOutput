class Color:
    RED = "#b71c1c"
    RED_DARK = "#d50000"
    RED_LIGHT = "#e57373"
    PINK = "#e91e63"
    PINK_DARK = "#880e4f"
    PINK_LIGHT = "#f48fb1"
    PURPLE = "#9c27b0"
    PURPLE_DARK = "#4a148c"
    PURPLE_LIGHT = "#ce93d8"
    BLUE = "#1e88e5"
    BLUE_DARK = "#0d47a1"
    BLUE_LIGHT = "#90caf9"
    INDIGO = "#3f51b5"
    INDIGO_DARK = "#1a237e"
    INDIGO_LIGHT = "#9fa8da"
    CYAN = "#00bcd4"
    CYAN_DARK = "#006064"
    CYAN_LIGHT = "#26c6da"
    GREEN = "#4caf50"
    GREEN_DARK = "#1b5e20"
    GREEN_LIGHT = "#a5d6a7"
    YELLOW = "#ffeb3b"
    YELLOW_DARK = "#f57f17"
    YELLOW_LIGHT = "#fff59d"
    ORANGE = "#ff9800"
    ORANGE_DARK = "#e65100"
    ORANGE_LIGHT = "#ffb74d"
    GREY = "#9e9e9e"
    GREY_LIGHT = "#eeeeee"
    GREY_DARK = "#212121"
    BROWN = "#795548"
    BROWN_LIGHT = "#bcaaa4"
    BROWN_DARK = "#3e2723"
    BLACK = "#000000"
    WHITE = "#ffffff"


class Formatting:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def generateColorCode(rgb, back=0):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    if back == 0:
        return '\033[{};2;{};{};{}m'.format(38, r, g, b)
    elif back == 1:
        return '\033[{};2;{};{};{}m'.format(48, r, g, b)


def back(hex_code):
    rgb = hex_to_rgb(hex_code)
    return str(generateColorCode(rgb, 1))


def text(hex_code):
    rgb = hex_to_rgb(hex_code)
    return str(generateColorCode(rgb))


def both(hex_text, hex_back):
    text_rgb = hex_to_rgb(hex_text)
    back_rgb = hex_to_rgb(hex_back)
    return str(generateColorCode(text_rgb) + generateColorCode(back_rgb, 1))



