from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Restaurant, Customer, Reviews
from faker import Faker
import random


engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

taverns = []
for i in range(10):
    restaurant = Restaurant(
        name = 'The_' + fake.last_name(),
        price = random.randint(200,550)
    )
    session.add(restaurant)
    session.commit()
    taverns.append(restaurant)

customers =[]
for i in range(15):
    customer = Customer(
        first_name = fake.first_name(),
        last_name = fake.last_name()
    )
    session.add(customer)
    session.commit()
    customers.append(customer)

for customer in customers:
    review = Reviews(
        the_review = fake.sentence(),
        star_rating = random.randint(1,10),
        customer_id = customer.id,
        restaurant_id = random.choice(taverns).id
    )
    session.add(Reviews)
    session.commit()
    # print(review)