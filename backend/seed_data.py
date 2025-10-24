"""
Script to seed the database with initial country data
"""
import json
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.country import Country
from app.models import country

# Create tables
country.Country.metadata.create_all(bind=engine)

# Sample data
sample_countries = [
    {
        "name": "Nepal",
        "capital": "Kathmandu",
        "population": 29609623,
        "region": "Asia",
        "subregion": "Southern Asia",
        "area": 147181.0,
        "flag_url": "https://flagcdn.com/w320/np.png",
        "interesting_fact": "Nepal is home to Mount Everest, the tallest mountain in the world, standing at 8,848 meters.",
        "currency": "Nepalese Rupee",
        "language": "Nepali",
        "timezone": "UTC+05:45",
        "is_independent": True
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "population": 104258327,
        "region": "Africa",
        "subregion": "Northern Africa",
        "area": 1001449.0,
        "flag_url": "https://flagcdn.com/w320/eg.png",
        "interesting_fact": "The Pyramids of Giza are one of the Seven Wonders of the Ancient World.",
        "currency": "Egyptian Pound",
        "language": "Arabic",
        "timezone": "UTC+02:00",
        "is_independent": True
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "population": 25687041,
        "region": "Oceania",
        "subregion": "Australia and New Zealand",
        "area": 7692024.0,
        "flag_url": "https://flagcdn.com/w320/au.png",
        "interesting_fact": "Australia is home to the Great Barrier Reef, the largest coral reef system in the world.",
        "currency": "Australian Dollar",
        "language": "English",
        "timezone": "UTC+10:00",
        "is_independent": True
    },
    {
        "name": "Brazil",
        "capital": "Brasilia",
        "population": 213993437,
        "region": "Americas",
        "subregion": "South America",
        "area": 8514877.0,
        "flag_url": "https://flagcdn.com/w320/br.png",
        "interesting_fact": "Brazil is home to the Amazon Rainforest, the largest tropical rainforest in the world.",
        "currency": "Brazilian Real",
        "language": "Portuguese",
        "timezone": "UTC-03:00",
        "is_independent": True
    },
    {
        "name": "France",
        "capital": "Paris",
        "population": 67407241,
        "region": "Europe",
        "subregion": "Western Europe",
        "area": 551695.0,
        "flag_url": "https://flagcdn.com/w320/fr.png",
        "interesting_fact": "The Eiffel Tower in Paris was once the tallest man-made structure in the world.",
        "currency": "Euro",
        "language": "French",
        "timezone": "UTC+01:00",
        "is_independent": True
    },
    {
        "name": "Russia",
        "capital": "Moscow",
        "population": 1324216107,
        "region": "Europe",
        "subregion": "Eastern Europe",
        "area": 17098242.0,
        "flag_url": "https://flagcdn.com/w320/ru.png",
        "interesting_fact": "Russia is the largest country in the world by area, covering more than 17 million square kilometers.",
        "currency": "Russian Ruble",
        "language": "Russian",
        "timezone": "UTC+03:00",
        "is_independent": True
    },
    {
        "name": "China",
        "capital": "Beijing",
        "population": 1444216107,
        "region": "Asia",
        "subregion": "Eastern Asia",
        "area": 9596961.0,
        "flag_url": "https://flagcdn.com/w320/cn.png",
        "interesting_fact": "The Great Wall of China is visible from space on rare occasions.",
        "currency": "Chinese Yuan",
        "language": "Chinese",
        "timezone": "UTC+08:00",
        "is_independent": True
    }
]


def seed_database():
    db = SessionLocal()
    try:
        # Check if data already exists
        existing_count = db.query(Country).count()
        if existing_count > 0:
            print(f"Database already contains {existing_count} countries. Skipping seed.")
            return
        
        # Add sample countries
        for country_data in sample_countries:
            country = Country(**country_data)
            db.add(country)
        
        db.commit()
        print(f"Successfully seeded database with {len(sample_countries)} countries.")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
