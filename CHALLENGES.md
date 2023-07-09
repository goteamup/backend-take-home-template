# Global Booking Limit 

Gymtastic loves enthusiastic and active customers, but some have been booking multiple sessions per day, which means less capacity for prospective customers.

Implement logic to return an HTTP error response if a customer attempts to book more than one class session in a single day.

# Attendance Milestones

Gymtastic would like to recognize customers who are persistent and book classes regularly. 

Extend the app to allow defining milestones, so that the business can specify an interval (e.g. 1 month, 1 year, 2 weeks) and a session count. When a customer books a session and hits the count, the system should automatically trigger an congratulatory email to the customer.

# Premium Class Types

Gymtastic sees an upselling opportunity. They recently invested in a pool and would like to offer swimming lessons to customers who purchase a premium membership. 

Extend the app to model any new domain objects and logic required to support this use case, but leave out any payment transaction logic. 

# Workout Tracking 

Gymtastic has some customers who use the free weights and cardio equipment, but don't attend class sessions. The business would like to keep them engaged and feeling productive. It has an idea to provide workout tracking features in its mobile app. Extend the app to provide a way for customers to track their activities during self-guided workouts. Gymtastic's space features dumbells, bench presses, treadmills, kettleballs, and stationary bikes.

# Late Cancels

Gymastic has had a problem lately with customers cancelling at the last moment. This hurts revenue because it leaves little time for another customer to purchase the open slot. They'd like to be able to configure a late cancel cutoff for each class type, and be able to track which bookings are cancelled past the cutoff. 

Hints:
- Gymtastic's app doesn't yet capture a booking status or allow changing it via the REST API. This functionality should be added when building this feature.
