import os
import requests

from flask import Flask, abort, render_template, request, send_file

from forms import ImageForm
from banner.banner import generate_banner
from banner.banner import DEFAULT_OUTPUT_FILE as outfile

IN_FILE = 'input.png'

app = Flask(__name__)


def download_url(url, in_file=IN_FILE, chunk_size=2000):
    print('Downloading {}'.format(url))
    r = requests.get(url, stream=True)
    print('Saving as {}'.format(in_file))

    with open(in_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)

    return in_file


@app.route('/', methods=['GET', 'POST'])
def image_inputs():
    form = ImageForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form)
        args = [form.image_url1.data]
        args.append(form.image_url2.data)
        args.append(form.text.data)
        if form.background.data:
            args.append(1)

        generate_banner(args)

        if os.path.isfile(outfile):
            return send_file(outfile, mimetype='image/png')
        else:
            abort(400)

    return render_template('imageform.html', form=form)


if __name__ == "__main__":
    app.run()
