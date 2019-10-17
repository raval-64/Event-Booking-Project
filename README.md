# event-booking-project
This is the Django(python) project for event booking. 
## Change for local system 
### Open Settings.py
change debug=false<br>
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
