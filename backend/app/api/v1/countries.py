from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.crud import country as country_crud
from app.schemas.country import Country, CountryCreate, CountryUpdate, CountrySearch

router = APIRouter()


@router.get("/", response_model=List[Country])
def get_countries(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get all countries with pagination"""
    countries = country_crud.get_countries(db, skip=skip, limit=limit)
    return countries


@router.get("/search", response_model=List[Country])
def search_countries(
    name: Optional[str] = Query(None, description="Search by country name"),
    region: Optional[str] = Query(None, description="Filter by region"),
    capital: Optional[str] = Query(None, description="Search by capital"),
    min_population: Optional[int] = Query(None, ge=0, description="Minimum population"),
    max_population: Optional[int] = Query(None, ge=0, description="Maximum population"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Search countries with various filters"""
    search_params = CountrySearch(
        name=name,
        region=region,
        capital=capital,
        min_population=min_population,
        max_population=max_population
    )
    countries = country_crud.search_countries(db, search_params, skip=skip, limit=limit)
    return countries


@router.get("/{country_id}", response_model=Country)
def get_country(country_id: int, db: Session = Depends(get_db)):
    """Get a specific country by ID"""
    country = country_crud.get_country(db, country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@router.get("/name/{country_name}", response_model=Country)
def get_country_by_name(country_name: str, db: Session = Depends(get_db)):
    """Get a specific country by name"""
    country = country_crud.get_country_by_name(db, country_name)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@router.get("/region/{region}", response_model=List[Country])
def get_countries_by_region(region: str, db: Session = Depends(get_db)):
    """Get all countries in a specific region"""
    countries = country_crud.get_countries_by_region(db, region)
    return countries


@router.get("/stats/overview")
def get_country_statistics(db: Session = Depends(get_db)):
    """Get country statistics and overview"""
    stats = country_crud.get_country_statistics(db)
    return stats


@router.post("/", response_model=Country)
def create_country(country: CountryCreate, db: Session = Depends(get_db)):
    """Create a new country"""
    # Check if country already exists
    existing_country = country_crud.get_country_by_name(db, country.name)
    if existing_country:
        raise HTTPException(status_code=400, detail="Country already exists")
    
    return country_crud.create_country(db, country)


@router.put("/{country_id}", response_model=Country)
def update_country(
    country_id: int,
    country: CountryUpdate,
    db: Session = Depends(get_db)
):
    """Update a country"""
    updated_country = country_crud.update_country(db, country_id, country)
    if not updated_country:
        raise HTTPException(status_code=404, detail="Country not found")
    return updated_country


@router.delete("/{country_id}")
def delete_country(country_id: int, db: Session = Depends(get_db)):
    """Delete a country"""
    success = country_crud.delete_country(db, country_id)
    if not success:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"message": "Country deleted successfully"}
