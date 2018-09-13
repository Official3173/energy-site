import os

for file in os.listdir('/home/mitchell/Desktop/energy-site-master/mywebsite/images/static/images/temp'):
    if file.endswith('.png'):
        os.remove(file)