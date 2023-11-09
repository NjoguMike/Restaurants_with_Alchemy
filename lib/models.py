import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey, Table)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)


customer_restaurant = Table(
    'customer_restaurant',
    Base.metadata,
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    extend_existing=True
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")
    customers = relationship("Customer", secondary=customer_restaurant, back_populates="restaurants")

    def reviews(self):
        return self.reviews

    def customers(self):
        return self.customers

    def __repr__(self):
        return f'Restaurant: {self.name}'
    
    @classmethod
    def fanciest(cls):
        pass

    def all_reviews(self):
        return self.reviews.fullreview()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Customer", secondary=customer_restaurant, back_populates="customers")

    def reviews(self):
        return self.reviews

    def restaurants(self):
        return self.restaurants

    def __repr__(self):
        return f'Customer: {self.first_name} + {self.last_name}'
    
    def full_name(self):
        pass

    def ravorite_restaurant(self):
        pass

    def add_review(self):
        pass

    def delete_review(self):
        pass

class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    the_review = Column(String())
    star_rating = Column(Integer())
    customer_id = Column(String(), ForeignKey('customers.id'))
    restaurant_id = Column(String(), ForeignKey('restaurants.id'))

    customer = relationship("Customer", back_populates="customer")
    restaurant = relationship("Restaurant", back_populates="customer")

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def __repr__(self):
        return f'Customer: {self.the_review} , {self.star_rating}'
    
    def full_review(self):
        return f'{self.restaurant.name} by {self.customer.fullname()}: {self.star_rating} stars.'