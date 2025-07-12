import sys
import os
from PIL import Image

folder_name = sys.argv[1]
new_folder_name = sys.argv[2]

if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)

for filename in os.listdir(folder_name):
    img = Image.open(f'./{folder_name}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'./{new_folder_name}{clean_name[0]}.png', 'png')
    
