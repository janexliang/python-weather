from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve 

### Create our main app
app = Flask('__name__')   ### app is a Flask app server

### @app is an annotion of running web server 
@app.route('/')  ### define this app homepage
@app.route('/index')  # both /, /index or /index.html goest to the same route
def index():
    ##  "Hollo World" for testing only. 
    #return "Hello World: with serve"
    return render_template('index.html')

### add route to weather.html page
@app.route('/weather')
### Call function get_current_weather from import
def get_weather(city="Ottawa"):  
    ### Get a city from args
    city = request.args.get('city')

    ### check if enter empty value for city
    ### strip() to remove empty whitespace string
    if not bool(city.strip()):
        city = "Ottawa" 
    
    ### please note weather_data is an object in json format
    weather_data = get_current_weather(city)

    
    ### Check response cod returned:
    ### 200 - Successful proceed 
    ### 3xx - Redirect
    ### 404 - Not found
    ### 5xx - server error
    ### request timeout
    if not weather_data["cod"]==200:
        return render_template("city-not-found.html")
        
    return render_template(
        "weather.html",
        ### title, status, temp and feels_like are words are defined in weather.html for example {{ title }}. value of these words will replace value in weather.html
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        ### as temperature return number, needs to be formated with .1f (point .1 in float type)
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=weather_data["main"]["feels_like"]
    )

if __name__ == "__main__":
    serve(app, host="localhost", port=8009) ## use module from waitress to avoid security WARN

    #app.run(host="0.0.0.0", port=8009)  ## run app on local with port 8009

    index()





