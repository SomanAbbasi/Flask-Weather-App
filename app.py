from flask import Flask,render_template,request
#Used to make HTTP request from external API such as OpenWeatherAPI
import requests

app=Flask(__name__)
#Weather API
API_KEY='81b37b075a5ad2039811709d88a3b3b4'


#Create a Routing Page 
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST': #Check Out user click on Submit Button
        city=request.form['city']  # Fetch datd from from search field

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response=requests.get(url) #Response in JSON Format
        data=response.json() #Convert JSON response into Python Dirc.
        
        """
        {
            "cod": 200,
            "main": {
                "temp": 32.5,
                "humidity": 45
            },
            "weather": [
                {
                "description": "clear sky",
                "icon": "01d"
                }
            ],
            "wind": {
                "speed": 3.5
            }
        }
        """
        #Processing API response
        if data['cod']==200:
            weather={
                'city':city,
                'temperature':data['main']['temp'],
                'humidity':data['main']['humidity'],
                'pressure':data['main']['humidity'],
                
                'description':data['weather'][0]['description'],
                'icon':data['weather'][0]['icon'],
                'wind':data['wind']['speed']
            }
            return render_template('result.html',weather=weather)
        else:
            error=f"City '{city}' not found."
            return render_template('index.html',error=error)
        
        
    return render_template('index.html')
        
            
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
