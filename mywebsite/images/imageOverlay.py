from PIL import Image, ImageDraw, ImageFont
import uuid


class ImageOverlay():
    
    def __init__(self, star_rating, model_num, kwh):
        self.star_rating = star_rating
        self.model_num = model_num
        self.kwh = kwh
        self.final_img_id = None

    def generate_image(self):
        '''
        Opens the correct blank template image.
        '''

        if self.star_rating == '0.5':
            self.image_template_id = '0.5 Stars Final Template'
        
        elif self.star_rating == '1':
            self.image_template_id = '1 Stars Final Template'
        
        elif self.star_rating == '1.5':
            self.image_template_id = '1.5 Stars Final Template'

        elif self.star_rating == '2':
            self.image_template_id = '2 Stars Final Template'
        
        elif self.star_rating == '2.5':
            self.image_template_id = '2.5 Stars Final Template'
        
        elif self.star_rating == '3':
            self.image_template_id = '3 Stars Final Template'
        
        elif self.star_rating == '3.5':
            self.image_template_id = '3.5 Stars Final Template'
        
        elif self.star_rating == '4':
            self.image_template_id = '4 Stars Final Template'

        elif self.star_rating == '4.5':
            self.image_template_id = '4.5 Stars Final Template'

        elif self.star_rating == '5':
            self.image_template_id = '5 Stars Final Template'

        # Opens the image from the correct directory
        img = Image.open('images/static/images/Dishwasher/' + self.image_template_id + '.png')

        # Changed from full path to windows path - shortened version should work on Ubuntu as well


        fnt1 = ImageFont.truetype('images/OpenSans-Regular.ttf', 42)

        
        fnt3 = ImageFont.truetype('images/OpenSans-Regular.ttf', 105)

        #replaces "<program name> used once per week"
        fnt4 = ImageFont.truetype('images/OpenSans-Regular.ttf', 18)

        d1 = ImageDraw.Draw(img)
        d2 = ImageDraw.Draw(img)
        d3 = ImageDraw.Draw(img)
        d4 = ImageDraw.Draw(img)

        d3_text_size = d3.textsize(self.kwh, font=fnt3)
        d3_text_midpoint = d3_text_size[0] / 2

        d1_text_size = d1.textsize(self.model_num, font=fnt1 )
        d1_text_midpoint = d1_text_size[0] / 2


        # Overlays Model
        d1.text((538 - d1_text_midpoint , 1340), self.model_num,        font = fnt1, fill=(241, 92, 48))
        
        # Overlays KWH in center of image, with white color text.
        d3.text((538 - d3_text_midpoint, 1120), self.kwh,               font = fnt3, fill=(255, 255, 255))

        uniq_id = str(uuid.uuid4())
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