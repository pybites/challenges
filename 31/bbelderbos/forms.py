import glob
import os

from wtforms import Form, BooleanField, StringField, SelectField, TextAreaField, validators

pybites_logos = glob.glob(os.path.join('assets', 'pybites', '*png'))

option_field = lambda img: os.path.splitext(os.path.basename(img))[0]


class ImageForm(Form):
    image_url1 = SelectField(
        'PyBites Logo Theme',
        choices=[(img, option_field(img)) for img in pybites_logos]
    )
    image_url2 = StringField('Second Image URL', [validators.DataRequired()])
    text = TextAreaField('Text for Banner', [validators.DataRequired()])
    background = BooleanField('Use Second Image as Background?', default=True)
