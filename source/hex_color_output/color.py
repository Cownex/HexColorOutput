from HexOutput import Color, Formatting, text, back, both

print(text("#b71c1c") + "Red Text! \033[2J")
print(back("#b71c1c", ) + "Red Background! \033[2J")
print(both("#b71c1c", "#000000") + "Red Text with Black Background! \033[2J")

print(text(Color.RED) + "Red Text! \033[2J")
print(back(Color.RED) + "Red Background! \033[2J ")
print(both(Color.RED, Color.BLACK) + "Red Text with Black Background! \033[2J" + Formatting.END)