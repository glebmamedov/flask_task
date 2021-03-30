from flask import Flask
from flask import render_template, request, redirect, url_for
from numbers_gen import main_func
import os
from werkzeug.utils import secure_filename

path = os.getcwd()
path += '\Downloads'
try:
    os.mkdir(path)
except FileExistsError:
    pass
download_folder = path
allowed_formats = set(['txt', 'jpg', 'png', 'jpeg'])

main_fl = Flask(__name__)
main_fl.config['download_folder'] = download_folder


@main_fl.route('/time')
def cac():
    cont = main_func(4545)
    dict_t = {"cont": cont}
    return render_template("upload_page.html", content=dict_t)


def allowed_format(filename):
    return "." in filename and filename.rsplit('.', 1)[1] in allowed_formats


@main_fl.route('/download', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_format(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(main_fl.config['download_folder'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('upload_page.html')


if __name__ == "__main__":
    main_fl.run()
