import datetime
import random

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from bookings.models import Booking
from classes.models import ClassSession, ClassType
from customers.models import Customer

CUSTOMERS = [
    {"first_name": "Jazmine", "last_name": "Clayton"},
    {"first_name": "Bryant", "last_name": "Bailey"},
    {"first_name": "Derek", "last_name": "Knox"},
    {"first_name": "Valerie", "last_name": "Matthews"},
    {"first_name": "Micah", "last_name": "Hebert"},
    {"first_name": "Silas", "last_name": "Pennington"},
    {"first_name": "Ryann", "last_name": "Juarez"},
    {"first_name": "Keenan", "last_name": "Carroll"},
    {"first_name": "Demarion", "last_name": "Frye"},
    {"first_name": "Macey", "last_name": "Williams"},
]

CLASS_TYPES = [
    {
        "name": "Yoga",
        "description": "A transformative yoga class that guides students through a harmonious blend of physical postures, breathwork, and mindfulness, fostering a sense of inner peace and overall well-being.",
    },
    {
        "name": "Crossfit",
        "description": "An intense and dynamic crossfit class that combines functional movements, strength training, and high-intensity intervals to help individuals push their limits and achieve peak fitness performance.",
    },
    {
        "name": "Karate",
        "description": "A disciplined karate class that focuses on traditional martial arts techniques, self-defense skills, and personal growth, fostering physical strength, mental resilience, and overall character development.",
    },
    {
        "name": "Zumba",
        "description": "A lively and exhilarating Zumba class that combines energetic dance movements with infectious music, creating a fun-filled workout experience that improves cardiovascular fitness, boosts energy levels, and ignites a passion for movement.",
    },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        customers = []
        class_types = []
        class_sessions = []
        bookings = []

        for customer_data in CUSTOMERS:
            fname, lname = customer_data["first_name"], customer_data["last_name"]
            email_provider = random.choice(["gmail", "outlook", "lycos"])
            email = f"{fname.lower()}.{lname.lower()}@{email_provider}.com"

            customer = Customer.objects.create(
                first_name=fname,
                last_name=lname,
                email=email,
            )

            customers.append(customer)

        for class_type_data in CLASS_TYPES:
            class_type = ClassType.objects.create(
                name=class_type_data["name"],
                description=class_type_data["description"],
            )

            class_types.append(class_type)

        current_date = datetime.datetime.now().date()

        for i in range(30):
            current_date += datetime.timedelta(days=1)

            for class_type in class_types:
                session = ClassSession.objects.create(
                    class_type=class_type,
                    starts_at=datetime.datetime.combine(
                        current_date,
                        datetime.time(
                            hour=random.choice([9, 10, 11, 4, 5, 6]),
                            minute=random.choice([0, 30]),
                        ),
                    ),
                )

                class_sessions.append(session)

        for customer in customers:
            booked_count = 0

            while booked_count < 4:
                try:
                    booking = Booking.objects.create(
                        customer=customer, class_session=random.choice(class_sessions)
                    )
                    bookings.append(booking)
                    booked_count += 1
                except IntegrityError:
                    pass
