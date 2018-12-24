import sys
import conf
import random
import tweepy

from holy_shiit_bot_module import average_size_by_char
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# WORD
# Open the file and lines
fo = open("nounlist.txt", "r+")
lines = fo.read().splitlines()

little_char = ['l', 'i', ]
big_char = ['w', 'm']

while True:
    # Get random word
    word =random.choice(lines)
    # Go to the file begening
    fo.seek(0)
    # rewrite the file without the word
    for line in lines:
        if line != word:
            fo.write(line + "\n")

    # Cut the end file
    fo.truncate()

    # If the word fit in the bubble space, end loop
    if len(word) < 12:
        break

# Close the file
fo.close()

# IMAGE
# Make the midle sentence
sentence = "my " + word
# Center the midle sentence's position
center = 1250 - (len(sentence) - 3) * average_size_by_char(sentence)
# Open the base image
im = Image.open("image_base.png")
draw = ImageDraw.Draw(im)
# Get the font
font = ImageFont.truetype("Cees Hand Regular.ttf", 70)
# Draw the sentences over the image
draw.text((1170, 15),"Holy shit,",(0,0,0),font=font)
draw.text((center, 80),sentence,(0,0,0),font=font)
draw.text((1170, 135),"is on fire",(0,0,0),font=font)
# Save the new image
im.save("image_out.png")

# TWEET
# Tweet authentification
auth = tweepy.OAuthHandler(conf.API_key, conf.API_secret_key)
auth.set_access_token(conf.Access_token, conf.Access_token_secret)
api = tweepy.API(auth)
# Tweet the fun
api.update_with_media("image_out.png", status="Holy shit, " + sentence + " is on fire")