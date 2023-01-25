from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
import random

inky_display = InkyWHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("./fonts/NotoSansJP-Medium.otf", 72)

flashcards = {}

flashcards['a'] = "あ"
flashcards['i'] = "い"
flashcards['u'] = "う"
flashcards['e'] = "え"
flashcards['o'] = "お"

keys = list(flashcards.keys())

currentCard = flashcards[keys[random.randrange(len(keys))]]

w, h = font.getsize(currentCard)

x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), currentCard, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()