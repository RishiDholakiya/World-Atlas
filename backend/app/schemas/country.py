from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CountryBase(BaseModel):
    name: str
    capital: Optional[str] = None
    population: Optional[int] = None
    region: Optional[str] = None
    subregion: Optional[str] = None
    area: Optional[float] = None
    flag_url: Optional[str] = None
    interesting_fact: Optional[str] = None
    currency: Optional[str] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    is_independent: Optional[bool] = True


class CountryCreate(CountryBase):
    pass


class CountryUpdate(CountryBase):
    name: Optional[str] = None


class Country(CountryBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        from_attributes = True


class CountrySearch(BaseModel):
    name: Optional[str] = None
    region: Optional[str] = None
    capital: Optional[str] = None
    min_population: Optional[int] = None
    max_population: Optional[int] = None
