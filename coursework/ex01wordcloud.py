import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

print(os.getcwd())
text = open("/workspaces/greends-avcad-2026/coursework/cvhannahnathanson.txt").read()
print(text)

stopwords = set(STOPWORDS)
stopwords.update(["currently", "students", "Whitemore", "Trap", "site", "coordinated", "Operation", "Wallacea", "student", "students" "Feb", "April", "August", "de", "Dec", "fostering", "SUMMARY", "Harrow", "sep", "conduct", "conducted", "Hannah", "Nathanson", "coordinating", "June", "July", "S", "Doñana", "gmail", "nathanson23", "assistant"])

wordcloud = WordCloud(stopwords=stopwords).generate(text)

''' # making in a square
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off")
plt.show()

wordcloud = WordCloud(
    stopwords=stopwords, # - stopwords=stopwords → removes unwanted words
    max_font_size=70, # - max_font_size=70 → limits the size of the largest word
    background_color="white", # - background_color="white" → sets the background color
    width=600, 
    height=400, # - width=600, height=400 → defines image dimensions (in pixels)
).generate(text) # - .generate(text) → builds the word cloud from the provided text string

plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")

plt.show()

wordcloud.to_file("wordcloud_PS8.png")
'''


'''
There are two types of variables in the wordcloud produced, words (str) and their frequency (int)

'''

#in a shape

from PIL import Image
my_mask = np.array(Image.open("/workspaces/greends-avcad-2026/coursework/wordcloudshapedog.png"))

my_mask = np.array(Image.open("/workspaces/greends-avcad-2026/coursework/wordcloudshapedog.png"))
print(my_mask.min(), my_mask.max())

plt.imshow(my_mask)

# Remove axis ticks and frame (not needed for image visualization)
plt.axis("off")

plt.show()

wc = WordCloud(
    background_color="white",   # Set the background color of the image
    max_words=1000,             # Maximum number of words to display
    mask=my_mask,           # Use the turtle image as a shape mask
    stopwords=stopwords,        # Remove predefined and custom stopwords
    contour_width=2,            # Thickness of the outline around the mask shape
    repeat=True,                # Allow words to repeat to better fill the mask shape
    max_font_size=50,           # Maximum size for the largest word
    contour_color='grey'        # Color of the contour (outline) around the mask
)

# Generate the word cloud from the text data
wc.generate(text)

# Save the generated WordCloud image to a file in the working directory
wc.to_file("dog_wordcloud.png") 

# Create a matplotlib figure with custom size (width=10, height=5 inches)
plt.figure(figsize=[10,5])

# Display the generated WordCloud image
# interpolation='bilinear' smooths the visual appearance
plt.imshow(wc, interpolation='bilinear')

# Remove axes (not needed for image display)
plt.axis("off")

plt.show()