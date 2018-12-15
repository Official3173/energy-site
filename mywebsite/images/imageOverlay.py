from PIL import Image, ImageDraw, ImageFont
import uuid


class ImageOverlay():
    
    def __init__(self, star_rating, model_num, kwh, primary, secondary):
        self.star_rating = star_rating
        self.model_num = model_num
        self.kwh = kwh
        self.final_img_id = None

    def generate_image(self):
        '''
        Opens the correct blank template image.
        '''

        # TODO
        # - Add new 7+ energy label images
        # - Create logic for new labels


        # Creates a variable holding the filename of the correct image template,
        # based on user input. 
        # Make sure form doesn't add a space anywhere, or this will not work!
        self.image_template_id = self.star_rating + ' Stars Final Template'

        # Opens the image from the correct directory
        img = Image.open('images/static/images/Dishwasher/' + self.image_template_id + '.png')

        # Changed from full path to windows path - shortened version should work on Ubuntu as well

        fnt1 = ImageFont.truetype('images/OpenSans-Regular.ttf', 42)
        kWh_font = ImageFont.truetype('images/OpenSans-Regular.ttf', 105)
        kwh_font_small = ImageFont.truetype('images/OpenSans-SemiBold.ttf', 34)

        # Initializes all the layers we're overlaying (I think?)
        d1 = ImageDraw.Draw(img)
        d2 = ImageDraw.Draw(img)
        d3 = ImageDraw.Draw(img)
        d4 = ImageDraw.Draw(img)

        # Finds the midpoint of each piece of input text, by finding
        # the total width and dividing by 2. This allows the image to be
        # easily centered.
        d3_text_size = d3.textsize(self.kwh, font=kWh_font)
        d3_text_midpoint = d3_text_size[0] / 2

        d1_text_size = d1.textsize(self.model_num, font=fnt1 )
        d1_text_midpoint = d1_text_size[0] / 2

        # Overlays Model Number, with orange text.
        d1.text((538 - d1_text_midpoint , 980), self.model_num, font = fnt1, fill=(241, 92, 48))
        # Overlays KWH in center of image, with white color text.
        d3.text((538 - d3_text_midpoint, 1120), self.kwh,       font = kWh_font, fill=(255, 255, 255))

        d4.text((505, 1555), self.kwh, font=kwh_font_small, fill=(241, 92, 48))

        # Generates unique ID for each image, so they don't save over each other.
        uniq_id = str(uuid.uuid4())

        # Generates a unique id that is 8 digits long.
        self.final_img_id = uniq_id[0:8]
        

        #saves image to filepath, with unique id as image name
        img.save('images/static/images/temp/' + self.final_img_id + '.png')


    def get_unique_img_id(self):
        '''
        Returns the unique image id.
        '''
        return self.final_img_id

        
'''
Initializes the object, and generates an image with input from parameters
'''
#image = ImageOverlay('1.5', 'Clothes Dryer 3000, for big loads', '366')
#image.generate_image()