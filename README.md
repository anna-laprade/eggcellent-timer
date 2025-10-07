# Eggcellent Timer 

This is a little flask app that allows users to specify an egg style (soft-boiled, hard-boiled, poached) and their location. The app will then calculate the altitude of their location and create a timer accordingly. The user can then use the timer while an egg animation plays in the background.
 

## Features
* Dynamic timer based on egg style and local altitude
* Location detection and location input auto-complete via LocationIQ API
* Altitude retrieval via Open Elevation API
* Simple, cute, user-friendly UI with animated egg graphic


## Dependencies 
1. Python 3.x
2. HTML5 / CSS3
3. Jinja2
4. Flask ([https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/))  
5. Requests ([https://pypi.org/project/requests/](https://pypi.org/project/requests/))  


These can be installed with either
``` pip install <package> ```
Or using the requirements.txt file and 
``` pip install -r requirements.txt ```


## API Dependencies
1. LocationIQ ([https://locationiq.com/](https://locationiq.com/))
2. Open Elevation [Open Elevation](https://open-elevation.com/)

## Installation
1. Create and activate a virtual environment using 
``` python -m venv <venv name> ```
Then activate it using 
*Linux/MacOS:*
``` source /<venv name>/bin/activate ```
*Windows* 
``` .\venv\Scripts\activate ```


2. Install dependencies with either 
``` pip install <package> ``` for each package
Or using the requirements.txt file and 
``` pip install -r  requirements.txt ```


3. Open the ``` index.html ``` file, and change the line 
``` const apiKey = "YOUR_API_KEY_HERE"; ```
To have the value of your API key for Location IQ (get it at ([https://locationiq.com/](https://locationiq.com/)))


4. To run the app, use 
``` flask run ```
And copy the resulting URL into your browser 







