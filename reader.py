import csv
import os
from PIL import Image
from numpy import array

name = 'OMA.csv'


def convert_picture(pictures, folder):
    for el in pictures:
        path = os.path.abspath(el.split('/')[-1])
        try:
            picture = Image.open(path)
            palette_image = picture.convert('P')
            if palette_image.mode != 'RGB':
                palette_image = palette_image.convert('RGB')
            palette_image.save(folder + '/' + el.split('/')[-1])
        except:
            pass


def name_folder(name):
    with open(name, 'r') as f:
        csv_data = csv.reader(f)
        my_list = []
        for line in csv_data:
            urls = "".join(line)
            if urls != '':
                my_list.append(urls)
        folder = my_list[0].split('/')[2]
        if not os.path.exists(folder):
            os.makedirs(folder)
        convert_picture(my_list, folder)


name_folder(name)
