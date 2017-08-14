import glob
import os

from wtforms import Form, BooleanField, StringField, SelectField, validators

pybites_logos = glob.glob(os.path.join('assets', 'pybites', '*png'))


class ImageForm(Form):
    image_url1 = SelectField(
        'Image URL 1',
        choices=[(img, os.path.splitext(os.path.basename(img))[0])
                 for img in pybites_logos]
    )
    image_url2 = StringField('Image URL 2', [validators.DataRequired()])
    text = StringField('Banner text', [validators.DataRequired()])
    background = BooleanField('Image 2 as background?',
                              [validators.DataRequired()])
