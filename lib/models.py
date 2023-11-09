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

    def reviews():
        "returns a collection of all the reviews for the `Restaurant`"
        pass

    def customers():
        "returns a collection of all the customers who reviewed the `Restaurant`"
        pass

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Customer", secondary=customer_restaurant, back_populates="customers")

    def reviews():
        "should return a collection of all the reviews that the `Customer` has left"
        pass

    def restaurants():
        "should return a collection of all the restaurants that the `Customer` has reviewed"

    def __repr__(self):
        return f'Customer: {self.first_name} + {self.last_name}'

class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    the_review = Column(String())
    star_rating = Column(Integer())
    customer_id = Column(String(), ForeignKey('customers.id'))
    restaurant_id = Column(String(), ForeignKey('restaurants.id'))

    customer = relationship("Customer", back_populates="customer")
    restaurant = relationship("Restaurant", back_populates="customer")

    def customer():
        "should return the `Customer` instance for this review"
        pass

    def restaurant():
        "should return the `Restaurant` instance for this review"
        pass

    def __repr__(self):
        return f'Customer: {self.the_review} , {self.star_rating}'