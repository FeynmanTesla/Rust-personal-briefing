<h1>Python-morning-wakeup</h1>
<p>A Python program that sounds an alarm at a preset time, then gives a briefing including the date and time, upcoming events, unread emails and/or other messages, the weather, and news headlines. To be able to run it ensure you have the installed packages below and go through the described configuration. Alarm clock mp3 file taken from <a href="http://soundbible.com/1787-Annoying-Alarm-Clock.html">http://soundbible.com/1787-Annoying-Alarm-Clock.html</a>.</p>

<h2>Dependencies:</h2>
<p>Have <a href="https://pypi.org/project/pip/">pip (Python Package Index)</a> installed. From there go to your Terminal/cmd/etc and run the following commands to install the required packages:</p>
<ul>
<li>pip install weather-api. Note on Linux this may in turn also require: sudo apt-get update && sudo apt-get install espeak</li>
<li>pip install pyttsx</li>
<li>pip install inflect</li>
<li>pip install newsapi-python</li>
<li>pip install --upgrade google-api-python-client oauth2client</li>
<li>pip install O365</li>
</ul>

<h2>Configuration:</h2>
<p>Set the values of the following variables in text files to save in this directory:</p>
<ol>
<li>Choose your form of address and save it to formOfAddress.txt (as with all the following text files, in the same directory as briefing.py and this README).</li>
<li>Find and input your city's name and <a href="https://developer.yahoo.com/weather/documentation.html">Yahoo WOEID</a>. Save them to cityName.txt and woeid.txt, respectively.</li>
<li>Get a free API key from <a href="https://newsapi.org/">newsapi.org</a> and save it to newsApiOrgAPIKey.txt.</li>
<li>Choose the <a href="https://newsapi.org/docs/endpoints/sources">news sources</a> the headlines are taken from, and save them to newsApiOrgSources.txt. They should be formatted as a comma-separated string of source ids.</li>
<li>Download credentials.json from <a href="https://developers.google.com/calendar/quickstart/python">https://developers.google.com/calendar/quickstart/python</a> into to the same folder as this README.</li>
<li>Save your office 365 email address and password to office365EmailAddress.txt and office365EmailPassword.txt</li>
</ol>
