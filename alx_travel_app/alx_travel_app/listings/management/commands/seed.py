
# listings/management/commands/seed.py
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds the database with sample data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))
        fake = Faker()
        
        # Clear existing data to prevent duplicates
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()
        User.objects.all().exclude(is_superuser=True).delete() # Keep superuser

        # Create sample users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password'
            )
            users.append(user)

        # Create sample listings
        listings = []
        for _ in range(20):
            listing = Listing.objects.create(
                title=fake.catch_phrase(),
                description=fake.text(),
                price=random.randint(50, 500),
                city=fake.city(),
                country=fake.country(),
                address=fake.street_address(),
                owner=random.choice(users)
            )
            listings.append(listing)

        # Create sample bookings and reviews
        for user in users:
            for _ in range(random.randint(1, 5)):
                listing = random.choice(listings)
                check_in = fake.date_between(start_date='-30d', end_date='+30d')
                check_out = fake.date_between(start_date=check_in, end_date='+60d')
                total_price = listing.price * (check_out - check_in).days
                
                Booking.objects.create(
                    guest=user,
                    listing=listing,
                    check_in_date=check_in,
                    check_out_date=check_out,
                    total_price=total_price
                )
                
                # Create a review for some bookings
                if random.random() > 0.5:
                    Review.objects.create(
                        guest=user,
                        listing=listing,
                        rating=random.randint(1, 5),
                        comment=fake.text(max_nb_chars=100)
                    )

        self.stdout.write(self.style.SUCCESS('Database successfully seeded with sample data!'))
