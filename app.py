from flask import Flask, render_template, request, jsonify
import requests
from .boil_math import *

app = Flask(__name__)

# start page
@app.route('/')
def home():
    return render_template('index.html')

# route for getting the information from the user's selections and then calculating boiling point and time
@app.route('/boiling-point', methods = ['POST'])
def boiling_point():
    # get info from selections 
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')
    egg_type = data.get('egg_type', 'soft')

    print(f"Received lat: {lat}, lon: {lon}, egg_type: {egg_type}")

    # open elevation API url 
    elevation_api_url = "https://api.open-elevation.com/api/v1/lookup"
    resp = requests.get(elevation_api_url, params={"locations": f"{lat},{lon}"})
    elevation_data = resp.json()

    # store altitude
    altitude = elevation_data["results"][0]["elevation"]

    # calculate boiling point 
    boiling_point_f = altitude_to_boiling_point_F(altitude)

    # base times at sea level 
    base_times = {'soft': 240, 'hard': 540, 'poached': 180}
    base_time_sec = base_times.get(egg_type, 4)

    # new time given elevation 
    adjusted_time = adjusted_egg_time_F(boiling_point_f, base_time_sec, k=0.018)

    # Return JSON response with boiling point
    return jsonify({
        "boiling_point": boiling_point_f,
        "boil_time": round(adjusted_time, 1)
    })

@app.route('/timer')
def timer_page():
    time = request.args.get('time', default=0, type=int)
    city = request.args.get('city', default='Unknown City')
    egg = request.args.get('egg', default='egg')
    temp = request.args.get('temp', default='Unknown')

    # truncate city to first two parts, "Denver, Colorado, USA" -> "Denver, Colorado"
    parts = [p.strip() for p in city.split(',')]

    if len(parts) > 1:
        # avoid duplicates, "Boston, Boston" -> "Boston"
        if parts[0].lower() == parts[1].lower():
            city_display = parts[0]
        else:
            city_display = ", ".join(parts[:2])
    else:
        city_display = city

    # return calculated info
    return render_template('timer.html', time=time, city=city_display, egg=egg, temp=temp)



if __name__ == '__main__':
    app.run(debug=True, port=8000)