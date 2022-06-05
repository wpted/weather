import os
from flask import Flask, render_template, redirect, url_for
from util.form import WeatherForm
from util.weather import Weather
from util.location import Location

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
MY_WEATHER_KEY = os.environ["api_key"]


@app.route('/', methods=["POST", "GET"])
def home():
    form = WeatherForm()
    current_weather = Weather(MY_WEATHER_KEY)

    user_location = vars(Location())

    weather = current_weather.get_weather(user_location["city"])
    temperature = weather["main"]["temp"]
    weather_description = weather["weather"][0]["main"].lower()

    if form.validate_on_submit():
        form = WeatherForm()
        city = form.weather.data

        return redirect(url_for('search', city=city))

    return render_template("index.html", form=form, temperature=temperature, weather_description=weather_description,
                           location=user_location)


@app.route('/search/<city>', methods=["POST", "GET"])
def search(city):
    form = WeatherForm()
    search_weather = Weather(MY_WEATHER_KEY).get_weather(city)
    temperature = search_weather["main"]["temp"]
    weather_description = search_weather["weather"][0]["main"].lower()

    if form.validate_on_submit():
        form = WeatherForm()
        city = form.weather.data

        return redirect(url_for('search', city=city))

    return render_template("result.html", form=form, temperature=temperature, weather_description=weather_description,
                           location=city)


if __name__ == '__main__':
    app.run(debug=True)
