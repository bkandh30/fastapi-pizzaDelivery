from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:heisenberg22@localhost/pizzaDelivery', echo=True)

Base = declarative_base()

Session = sessionmaker()