<h1>Python-morning-wakeup</h1>
<p>This is a Python program that sounds an alarm at a preset time, then gives a briefing including the date and time, upcoming events, unread emails, the weather, and news headlines. To use it follow the below instructions. The alarm clock mp3 file was taken from <a href="http://soundbible.com/1787-Annoying-Alarm-Clock.html">http://soundbible.com/1787-Annoying-Alarm-Clock.html</a>.</p>

<h2>Dependencies:</h2>
<ul>
<li><a href="https://www.python.org/downloads/">Python 3</a></li>
<li>On Linux, run the dependencies_linux.sh shell script (once) to install all dependencies</li>
<li>On Windows, run the dependencies_windows.bat batch file (once) to install all dependencies</li>
</ul>

<h2>Configuration:</h2>
<p>Set the values of the following variables in text files to save in this directory:</p>
<ol>
<li>Choose your form of address and save it to conf/form_of_address.txt (i.e. named form_of_address.txt and, as with all the configuration text files, in the conf directory).</li>
<li>To set up email for Office 365, follow the instructions found at <a href="https://pypi.org/project/O365/#authentication">https://pypi.org/project/O365/#authentication</a> to register your app with Azure.
Choose the User.Read, offline_access, and Mail.Read permissions and save the client id to office_365_client_id.txt and the client secret to office_365_client_secret.txt.
After this, the first time you run the app (and subsequent times requiring re-authentication) you will be given a URL to go to an oAuth Microsoft login.
Grant permissions and wait to be forwarded to a blank page. Copy and paste the URL of the blank page into your CLI and press Enter to give the value. The application should then be authorised.</li>
<li>Get a free API key from <a href="https://home.openweathermap.org/users/sign_up">openweathermap.org</a> and save it to owm_api_key.txt</li>
<li>Save the name of your city to city_name.txt</li>
<li>Find your city on <a href="https://openweathermap.org/city">openweathermap.org</a> and find its city ID.
When you click onto a result and are directed to the /city page, the numbers following the /city are the city ID of the selected city. Save this city ID to city_id.txt.</li>
<li>Get a free API key from <a href="https://newsapi.org/">newsapi.org</a> and save it to news_api_org_api_key.txt.</li>
<li>Choose the <a href="https://newsapi.org/sources">news sources</a> the headlines are taken from, and save them to news_api_org_sources.txt. They should be formatted as a comma-separated string of source ids.</li>
<li>Download credentials.json from <a href="https://developers.google.com/calendar/quickstart/python">https://developers.google.com/calendar/quickstart/python</a> into the src folder.</li>
<li>Manually run print(getEvents()) once - taking the getEvents() method from the getEvents.py source file. This is to bring up the authorisation process for the Google APIs for reading Calendar and Gmail, and thereby generating the required token.json file. You can do this with the command "python -c 'import get_events; print(get_events())'" in the src folder.</li>
<li>Choose the time you wish to be woken up, and save the hours and minutes separately to hours_to_wake_at.txt and mins_to_wake_at.txt respectively.</li>
</ol>

<h2>Usage:</h2>
<ul>
<li>On Linux, run the wakeup_linux.sh shell script to run the program</li>
<li>On Windows, run the wakeup_windows.bat batch file to run the program</li>
</ul>
