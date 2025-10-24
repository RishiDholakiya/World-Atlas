from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.country import Country
from app.schemas.country import CountryCreate, CountryUpdate, CountrySearch


def get_country(db: Session, country_id: int) -> Optional[Country]:
    return db.query(Country).filter(Country.id == country_id).first()


def get_country_by_name(db: Session, name: str) -> Optional[Country]:
    return db.query(Country).filter(Country.name == name).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100) -> List[Country]:
    return db.query(Country).offset(skip).limit(limit).all()


def search_countries(db: Session, search_params: CountrySearch, skip: int = 0, limit: int = 100) -> List[Country]:
    query = db.query(Country)
    
    if search_params.name:
        query = query.filter(Country.name.ilike(f"%{search_params.name}%"))
    
    if search_params.region:
        query = query.filter(Country.region == search_params.region)
    
    if search_params.capital:
        query = query.filter(Country.capital.ilike(f"%{search_params.capital}%"))
    
    if search_params.min_population:
        query = query.filter(Country.population >= search_params.min_population)
    
    if search_params.max_population:
        query = query.filter(Country.population <= search_params.max_population)
    
    return query.offset(skip).limit(limit).all()


def create_country(db: Session, country: CountryCreate) -> Country:
    db_country = Country(**country.dict())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


def update_country(db: Session, country_id: int, country: CountryUpdate) -> Optional[Country]:
    db_country = get_country(db, country_id)
    if db_country:
        update_data = country.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_country, field, value)
        db.commit()
        db.refresh(db_country)
    return db_country


def delete_country(db: Session, country_id: int) -> bool:
    db_country = get_country(db, country_id)
    if db_country:
        db.delete(db_country)
        db.commit()
        return True
    return False


def get_countries_by_region(db: Session, region: str) -> List[Country]:
    return db.query(Country).filter(Country.region == region).all()


def get_country_statistics(db: Session) -> dict:
    total_countries = db.query(Country).count()
    regions = db.query(Country.region).distinct().all()
    total_population = db.query(Country.population).filter(Country.population.isnot(None)).all()
    
    return {
        "total_countries": total_countries,
        "regions": [region[0] for region in regions if region[0]],
        "total_population": sum([pop[0] for pop in total_population if pop[0]]),
        "average_population": sum([pop[0] for pop in total_population if pop[0]]) / len(total_population) if total_population else 0
    }
