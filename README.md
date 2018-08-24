<h1>Python-morning-wakeup</h1>
<p>This is a Python program to sound an alarm at a preset time, then to give the user a briefing including the current date and time, upcoming events for the day from a Calendar, unread emails or other contact notifications, the weather, and news headlines. To be able to run it ensure you have the installed packages below and go through the described configuration.</p>

<h2>Dependencies:</h2>
<p>Have <a href="https://pypi.org/project/pip/">pip (Python Package Index)</a> installed. From there go to your Terminal/cmd/etc and run the following commands to install the required packages:</p>
<ul>
<li>pip install weather-api. Note on Linux this may in turn also require: sudo apt-get update && sudo apt-get install espeak</li>
<li>pip install pyttsx</li>
<li>pip install inflect</li>
<li>pip install newsapi-python</li>
<li>pip install --upgrade google-api-python-client oauth2client</li>
</ul>

<h2>Configuration:</h2>
<p>Set the values of the following variables under "# CONFIGURATION" at the top of briefing.py:</hp>
<ol>
<li>Choose your form of address ("formOfAddress")</li>
<li>Find and input your city's name and <a href="https://developer.yahoo.com/weather/documentation.html">Yahoo WOEID</a> ("woeid" and "cityName")</li>
<li>Get a free API key from <a href="https://newsapi.org/">newsapi.org</a> and save it to "newsApiOrgAPIKey.txt" in the same directory as briefing.py.</li>
<li>Optional: also change the <a href="https://newsapi.org/docs/endpoints/sources">news sources</a> the headlines are taken from ("newsApiOrgSources")</li>
<li>Download credentials.json from <a href="https://developers.google.com/calendar/quickstart/python">https://developers.google.com/calendar/quickstart/python</a> into to the same folder as this README.</li>
</ol>
