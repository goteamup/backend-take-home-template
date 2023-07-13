# Intro

Gymtastic is small fitness center with big dreams of helping their community become active and healthy. They've been using an Excel spreadsheet to manage their business, but they'd like to build a more powerful system using Python, Django, Django REST Framework and SQL.

So far, they've built some basic models and endpoints for class types, class sessions, customers and bookings. An example of a class type is yoga, and a class session would be specific date and time for a yoga class. Bookings link customers to the class sessions they attend.

Please follow the setup steps below and follow the project instructions to help Gymtastic grow their business.

# Setup

The project requires Python 3.8 or higher.

Steps:
- Create a Python virtual environment by running `python3 -m venv .venv` in the project root.
- Activate the environment with source .venv/bin/activate
- Run `python manage.py migrate` to create the database tables in a local SQLite database.
- Create some fixture data by running `python manage.py genfixtures`.
- Start the web server by running `python manage.py runserver`.

Congrats! Now you can browse the existing API endpoints at the following URLs:
- [http://localhost:8000/api/class_sessions](http://localhost:8000/api/class_sessions)
- [http://localhost:8000/api/class_types](http://localhost:8000/api/class_types)
- [http://localhost:8000/api/customers](http://localhost:8000/api/customers)
- [http://localhost:8000/api/bookings](http://localhost:8000/api/bookings)


# Project Instructions

Please read over the feature descriptions below and pick two for implementation in the REST API. Please don't spend more than 3 hours on this project. For simplicity, don't implement any authentication or permissions. Assume a trusted client will be making all the requests. If you have time to write tests or you like to use TDD, that's nice, but please focus on extending the domain model and implementing the required business logic for the features.

The first step is to clone this repository to your workstation. Once you're done, you can submit it by sending the project in a file archive email attachment or by pushing the code to your own public repo and sharing the link with us. Please send us an email when you're done.

If it's been a while since you've used this project stack, you'd likely want to reference the documentation for [Django](https://docs.djangoproject.com/en/4.2/) and [Django REST Framework](https://www.django-rest-framework.org/).

In summary:
- Pick two features below and implement them
- Don't spend more than 3 hours on this project
- Don't implement any authentication or permissions
- Tests are always nice, but prioritize data modeling and business logic
- Send us an email when you're done. Attach the files in an archive or link us to a public repo with the code.

## Features

### Global Booking Limit 

Gymtastic loves enthusiastic and active customers, but some have been booking multiple sessions per day, which means less capacity for prospective customers.

Implement logic to return an HTTP error response if a customer attempts to book more than one class session in a single day.

### Attendance Milestones

Gymtastic would like to recognize customers who are persistent and book classes regularly. 

Extend the app to allow defining milestones, so that the business can specify an interval (e.g. 1 month, 1 year, 2 weeks) and a session count. When a customer books a session and hits the count, the system should automatically trigger an congratulatory email to the customer.

### Premium Class Types

Gymtastic sees an upselling opportunity. They recently invested in a pool and would like to offer swimming lessons to customers who purchase a premium membership. 

Extend the app to model any new domain objects and logic required to support this use case.

Pointers:
- Don't implement any logic related to online payments or transactions. Gymtastic deals only in cash :)


### Workout Tracking 

Gymtastic has some customers who use the free weights and cardio equipment, but don't attend class sessions. The business would like to keep them engaged and feeling productive. It has an idea to provide workout tracking features in its mobile app. Extend the app to provide a way for customers to track their activities during self-guided workouts. Gymtastic's space features dumbells, bench presses, treadmills, kettleballs, and stationary bikes.

### Late Cancels

Gymastic has had a problem lately with customers cancelling at the last moment. This hurts revenue because it leaves little time for another customer to purchase the open slot. They'd like to be able to configure a late cancel cutoff for each class type, and be able to track which bookings are cancelled past the cutoff. 

Pointers:
- Gymtastic's app doesn't yet capture a booking status or allow changing it via the REST API. This functionality should be added when building this feature.


# Evaluation Criteria

We'll focus on the following aspects:
- Correctness
- Readability 
- Efficiency of SQL queries
- Familiarity with Django and Django REST Framework best practices

