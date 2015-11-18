# https://github.com/hplgit/web4sciapps/blob/master/doc/src/web4sa/src-web4sa/apps/flask_apps/vib1/model.py

from wtforms import Form, FloatField, validators

class InputForm(Form):
    A = FloatField(
        label='*3', default=1.0,
        validators=[validators.InputRequired()])
    w = FloatField(
        label='+2', default=2,
        validators=[validators.InputRequired()])

