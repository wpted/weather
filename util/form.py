from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import input_required, data_required


class WeatherForm(FlaskForm):
    weather = StringField(validators=[data_required()], render_kw={"placeholder": "Enter a city"})
    search = SubmitField()


