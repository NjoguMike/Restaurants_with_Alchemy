import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)


# class Review(Base):
#     pass

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f'Customer: {self.name}'

class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    review = Column(String())
    star_rating = Column(Integer())
    customer_id = Column(String(), ForeignKey('customers.id'))
    restaurant_id = Column(String(), ForeignKey('restaurants.id'))

    def __repr__(self):
        return f'Customer: {self.name}'