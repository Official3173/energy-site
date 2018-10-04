import os

for file in os.listdir('.'):
    if file.endswith('.png'):
        os.remove(file)