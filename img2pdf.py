from PIL import Image
import os
file = 'koti.jpg'
img = Image.open(file)

# if img.mode == 'RGBA':
# 	img = img.convert('RGB')
new_file = 'koti.pdf'
img.save(new_file,'PDF',resolution=100.0)

#If image is not RGB Use the following code

from PIL import Image
import os
file = 'koti.jpg'
img = Image.open(file)
if img.mode == 'RGBA':
	img = img.convert('RGB')
new_file = 'koti.pdf'
img.save(new_file,'PDF',resolution=100.0)
