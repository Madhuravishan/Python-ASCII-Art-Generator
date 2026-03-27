import time
from PIL import Image
import os
import sys

# Your image path
IMAGE_PATH = "D:/Programming Languages/Ascii art/input.jpg"

if not os.path.exists(IMAGE_PATH):
    print(f"Image not found: {IMAGE_PATH}")
    sys.exit()

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    # Adjusted ratio from 1.65 to 2.2 to fix the vertical stretch
    ratio = height / width / 2.2  
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def image_to_ascii(image):
    image = image.convert("RGB")
    width, height = image.size
    ascii_data = []

    for y in range(height):
        line = ""
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray = int((r + g + b) / 3)
            char = ASCII_CHARS[gray * len(ASCII_CHARS) // 256]
            color_char = f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            line += color_char
        ascii_data.append(line)
    return ascii_data

img = Image.open(IMAGE_PATH)
# Increased the default width from 100 to 130 to make it wider overall
img = resize_image(img, new_width=130)
ascii_lines = image_to_ascii(img)

for line in ascii_lines:
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0) 
    print()

print("\n✅ Image fully revealed!")