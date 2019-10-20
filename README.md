# Event Booking Project   :ticket:

### Introduction
The event booking project is a web application based on the event booking system and has been developed in `Django(Python)`. `sqllite3` is used for database management. `HTML`, `CSS`, `Javascript` and `Bootstrap` are used for the front end of the project. 

**Features** 
* User(url:`/`)
    - User can view all events.
    - User can view event details.
    - User can book event in event details.
    - Users can view booking summary after booking event.

* Organizer(url:`/admin`)
    - Organizer can perform [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations on the event.
    - Organizer can view bookings information such as name, email, mobile number, booked event.
    - Organizer can filter event bookings by category.

### Installation and setup:  

* Navigate to a directory of choice on terminal.  

* Clone this repository from Github on that directory.  

	* Using SSH;
 		> ` git@github.com:raval-64/event-booking-project.git `  

	* Using HTTP;
		>  ` https://github.com/raval-64/event-booking-project.git `  


* Navigate to the repo's folder on your computer  
	* ``` cd event-booking-project ```  

* Install the app's dependencies. I advice using a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)  
	* ``` pip install -r requirements.txt ``` 
* Change some code from the project because the project is set for deployment, so it needs to be set for the local environment first.  
	* ``` cd event_book ```
	* ``` update settings.py ```
		* ``` DEBUG = True ```
		* ``` delete this code from file ```
		
		```
		SECURE_CONTENT_TYPE_NOSNIFF = True
		SECURE_BROWSER_XSS_FILTER = True
		SESSION_COOKIE_SECURE = True
		CSRF_COOKIE_SECURE = True
		X_FRAME_OPTIONS = 'DENY'
		SECURE_SSL_REDIRECT = False
		SECURE_HSTS_SECONDS = 259200
		SECURE_HSTS_INCLUDE_SUBDOMAINS = True
		SECURE_HSTS_PRELOAD = True
		```
* Run the app  
	* ` python manage.py runserver ` 

### Backend Dependencies:

1. [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern.

2. [SQlite](https://www.sqlite.org/index.html) - This is a light-weight relational database that eventbuzz uses to store event data.

3. [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) - Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers.

4. [Pillow](https://pillow.readthedocs.io/en/stable/) - PIL is the Python Imaging Library by Fredrik Lundh and Contributors.



