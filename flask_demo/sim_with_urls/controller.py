# https://github.com/hplgit/web4sciapps/blob/master/doc/src/web4sa/src-web4sa/apps/flask_apps/vib1/controller.py

from model import InputForm
from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)

@app.route('/A=<int:user_input_A>+w=<int:user_input_w>', methods=['GET', 'POST'])
def uservar(user_input_A,user_input_w):
    result = compute(user_input_A,user_input_w)

    return render_template('compute_from_URL.html', form=None, result=result)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, 
                         form.w.data)
    else:
        result = None

    return render_template('form_input_view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)

