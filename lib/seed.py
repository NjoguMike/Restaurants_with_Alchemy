from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Restaurant, Customer, Reviews
from faker import Faker


engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

