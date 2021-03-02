# Event Booking Project   :ticket:

### Introduction
The event booking project is a web application based on the event booking system and has been developed in `Django(Python)`. `sqllite3` is used for database management. `HTML`, `CSS`, `Javascript` and `Bootstrap` are used for the front end of the project. 

The user can view all events on the home page. If the event is full then it will be automatically removed from the home page. User can click on any event on the home page for event details. And the event will be shown by their ID. On the event details page, the user can book an event with the booking form. After booking the event the user will redirect to the booking summary page. Details like booking ID and booking details will appear on the summary page.

The organizer can perform tasks like add / update / view / delete in the event. Organizers can view all bookings and filter bookings according to their category.

* organizer id and password
 	- ID : test
 	- Password : mypass13

**Features** 
* User (url:`/`)
    - User can view all events.
    - User can view event details.
    - User can book event in event details.
    - Users can view booking summary after booking event.

* Organizer (url:`/admin`)
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
+   Create .env file in event_book.
    
    - make copy of env.sample with rename .env.
    - add env variable values.

+  Install the app's dependencies. I advice using a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
    
	- `cd event_book`
    - `python -m venv .venv`
    - `source .venv/bin/activate`
    - `pip install -r requirements.txt`

* Run the app  
	* ` python manage.py runserver ` 

### Backend Dependencies:

1. [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern.

2. [SQlite](https://www.sqlite.org/index.html) - This is a light-weight relational database that eventbuzz uses to store event data.

3. [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) - Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers.

4. [Pillow](https://pillow.readthedocs.io/en/stable/) - PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

