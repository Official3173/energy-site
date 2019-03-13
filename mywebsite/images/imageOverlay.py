from PIL import Image, ImageDraw, ImageFont
import uuid

class ImageOverlay():
    
    def __init__(self, star_rating, model_num, kwh, primary, secondary):
        self.star_rating = star_rating
        self.model_num = model_num
        self.kwh = kwh
        self.final_img_id = None
        self.primary = primary
        self.secondary = secondary + ' water'

    def generate_image(self):
        '''
        Opens the correct blank template image.
        ''' 
        # TODO
        # - Add new 7+ energy label images
        # - Create logic for new labels

        if self.primary == 'Hot':
            primary_text_position_val = 342
        else:
            primary_text_position_val = 330

        # Creates a variable holding the filename of the correct image template,
        # based on user input. 
        # Make sure form doesn't add a space anywhere, or this will not work!
        self.image_template_id = self.star_rating + ' Stars Final Template'

        # Opens the image from the correct directory
        template_img = Image.open('images/static/images/Dishwasher/' + self.image_template_id + '.png')

        # Changed from full path to windows path - shortened version should work on Ubuntu as well
        model_num_font = ImageFont.truetype('images/OpenSans-Regular.ttf', 42)
        kWh_font = ImageFont.truetype('images/OpenSans-Regular.ttf', 105)
        kWh_font_small = ImageFont.truetype('images/OpenSans-SemiBold.ttf', 34)
        primary_font = ImageFont.truetype('images/OpenSans-Regular.ttf', 30)
        secondary_font = ImageFont.truetype('images/OpenSans-SemiBold.ttf', 34)

        # Initializes all the layers we're overlaying
        model_num = ImageDraw.Draw(template_img) #previously d1
        kWh = ImageDraw.Draw(template_img)       #previously d2
        kWh_small = ImageDraw.Draw(template_img) #previously d3...
        primary = ImageDraw.Draw(template_img)
        secondary = ImageDraw.Draw(template_img)
        program = ImageDraw.Draw(template_img)

        # Finds the midpoint of each piece of input text, by finding
        # the total width and dividing by 2. This allows the image to be
        # easily centered.

        kWh_small_text_size = kWh_small.textsize(self.kwh, font=kWh_font)
        kWh_small_text_midpoint = kWh_small_text_size[0] / 2

        d1_text_size = model_num.textsize(self.model_num, font=model_num_font)
        model_num_text_midpoint = d1_text_size[0] / 2

        # Overlays Model Number, with orange text.
        model_num.text((538 - model_num_text_midpoint , 980), self.model_num, font = model_num_font, fill=(241, 92, 48))
        # Overlays KWH in center of image, with white color text.
        kWh.text((538 - kWh_small_text_midpoint, 1120), self.kwh, font = kWh_font, fill=(255, 255, 255))
        
        kWh_small.text((505, 1557), self.kwh, font = kWh_font_small, fill=(241, 92, 48))

        primary.text((primary_text_position_val, 1318), self.primary, font = primary_font, fill=(241, 92, 48))

        secondary.text((672, 1517), self.secondary, font = secondary_font, fill=(241, 92, 48))

        program.text((274, 1354), 'normal', font=primary_font, fill=(241, 92, 48))

        

        # Generates unique ID for each image, so they don't save over each other.
        uniq_id = str(uuid.uuid4())

        # Generates a unique id that is 8 digits long.
        self.final_img_id = uniq_id[0:8]    

        # Saves image to filepath, with unique id as image name
        template_img.save('images/static/images/temp/' + self.final_img_id + '.png')


    def get_unique_img_id(self):
        '''
        Returns the unique image id..
        '''
        return self.final_img_id

        
'''
Initializes the object, and generates an image with input from parameters
'''
