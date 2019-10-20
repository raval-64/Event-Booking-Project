# Event Booking Project   :ticket:

### Introduction
The event booking project is a web application based on the event booking system and has been developed in `Django(Python)`. `HTML`, `CSS`, `Javascript` and `CSS bootstrap` frameworks are used for the project. 

**Features** 
* User:
    - User can view all events
    - User can view event details
    - User can book event in event details
    - Users can view booking summary after booking events.

## Change for local system 
### install python-pip
### pip install -r requirements.txt
### Open Settings.py
Change DEBUG = True<br>
#### Delete this code from settings.py
SECURE_CONTENT_TYPE_NOSNIFF = True<br>
SECURE_BROWSER_XSS_FILTER = True<br>
SESSION_COOKIE_SECURE = True<br>
CSRF_COOKIE_SECURE = True<br>
X_FRAME_OPTIONS = 'DENY'<br>
SECURE_SSL_REDIRECT = False<br>
SECURE_HSTS_SECONDS = 259200<br>
SECURE_HSTS_INCLUDE_SUBDOMAINS = True<br> 
SECURE_HSTS_PRELOAD = True<br>
