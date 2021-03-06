# Python Hex-Color-Output 

This package can use hex codes to change text and background color for the Python console.
## Installation

Install Hex-Color-Output via pip

```bash
  pip install hex-color-output
```






## How to


Normal usage with hex codes:
```python
from hex_color_output import Color, Formatting, text, back, both

print(text("#b71c1c") + "Red Text!")
print(back("#b71c1c") + "Red Background!")
print(both("#b71c1c", "#000000") + "Red Text with Black Background!")

```

Using our Color Class:
```python
print(text(Color.RED) + "Red Text!")
print(back(Color.RED) + "Red Background!")
print(both(Color.RED, Color.BLACK) + "Red Text with Black Background!")
```

With Text-Formatting:
```python 
print(Formatting.Bold + " Bold Text")
print(Formatting.UNDERLINE + " Underline Text")
print(Formatting.END + " Reset Formatting (Color and Formatting)")

```
## Formatting Classes


Formatting
| Name | Description |  
| :-------- | :------- | 
| `BOLD` | Bold Text | 
| `UNDERLINE` | Underline Text | 
| `END` | Reset Text Formatting |

Color
## Color Reference
```py
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
```

## Support

For support and feedback contact me via E-Mail: contact@cownex.de.


## Thanks to

- [@marl0nx](https://www.github.com/marl0nx)


## License

[MIT](https://choosealicense.com/licenses/mit/)

