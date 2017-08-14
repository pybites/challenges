import os
import requests

from flask import Flask, abort, render_template, request, send_file

from forms import ImageForm
from banner.banner import generate_banner
from banner.banner import DEFAULT_OUTPUT_FILE as outfile

IMAGES = 'images'

app = Flask(__name__)


def _download_image(from_url, to_file, chunk_size=2000):
    r = requests.get(from_url, stream=True)

    with open(to_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


def get_image(image_url):
    basename = os.path.basename(image_url)
    local_image = os.path.join(IMAGES, basename)

    if not os.path.isfile(local_image):
        _download_image(image_url, local_image)

    return local_image


@app.route('/', methods=['GET', 'POST'])
def image_inputs():
    form = ImageForm(request.form)

    if request.method == 'POST' and form.validate():
        image1 = form.image_url1.data
        image2 = get_image(form.image_url2.data)
        text = form.text.data
        print(text)
        background = form.background.data

        args = [image1, image2, text, background]

        generate_banner(args)

        if os.path.isfile(outfile):
            return send_file(outfile, mimetype='image/png')
        else:
            abort(400)

    return render_template('imageform.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
