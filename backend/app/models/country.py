from sqlalchemy import Column, Integer, String, Text, Float, Boolean
from app.database import Base


class Country(Base):
    __tablename__ = "countries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    capital = Column(String(100), nullable=True)
    population = Column(Integer, nullable=True)
    region = Column(String(50), nullable=True)
    subregion = Column(String(50), nullable=True)
    area = Column(Float, nullable=True)
    flag_url = Column(String(500), nullable=True)
    interesting_fact = Column(Text, nullable=True)
    currency = Column(String(100), nullable=True)
    language = Column(String(100), nullable=True)
    timezone = Column(String(100), nullable=True)
    is_independent = Column(Boolean, default=True)
    created_at = Column(String(50), nullable=True)
    updated_at = Column(String(50), nullable=True)
