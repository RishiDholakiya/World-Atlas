# Country Information API

A comprehensive REST API built with FastAPI for managing country information. This backend serves as the API layer for the React Country Information frontend application.

## Features

- **RESTful API** with FastAPI
- **Database Integration** with SQLAlchemy
- **Comprehensive CRUD Operations** for country data
- **Advanced Search & Filtering** capabilities
- **Automatic API Documentation** with Swagger UI
- **CORS Support** for frontend integration
- **Data Validation** with Pydantic models
- **Database Seeding** with sample data

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping (ORM)
- **Pydantic** - Data validation using Python type annotations
- **SQLite/PostgreSQL** - Database support
- **Uvicorn** - ASGI server for running the application

## API Endpoints

### Countries

- `GET /api/v1/countries/` - Get all countries (with pagination)
- `GET /api/v1/countries/search` - Search countries with filters
- `GET /api/v1/countries/{country_id}` - Get country by ID
- `GET /api/v1/countries/name/{country_name}` - Get country by name
- `GET /api/v1/countries/region/{region}` - Get countries by region
- `GET /api/v1/countries/stats/overview` - Get country statistics
- `POST /api/v1/countries/` - Create new country
- `PUT /api/v1/countries/{country_id}` - Update country
- `DELETE /api/v1/countries/{country_id}` - Delete country

### General

- `GET /` - API information
- `GET /health` - Health check

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the example environment file and configure:

```bash
cp env.example .env
```

Edit `.env` file with your configuration:

```env
DATABASE_URL=sqlite:///./country_app.db
SECRET_KEY=your-secret-key-here
API_V1_STR=/api/v1
PROJECT_NAME=Country Information API
```

### 3. Initialize Database

```bash
python seed_data.py
```

### 4. Run the Application

```bash
# Development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using Python
python -m app.main
```

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Database Schema

### Country Model

- `id` - Primary key
- `name` - Country name (unique)
- `capital` - Capital city
- `population` - Population count
- `region` - Geographic region
- `subregion` - Geographic subregion
- `area` - Land area in square kilometers
- `flag_url` - URL to country flag image
- `interesting_fact` - Fun fact about the country
- `currency` - Official currency
- `language` - Official language
- `timezone` - Timezone information
- `is_independent` - Independence status
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## Search & Filtering

The API supports advanced search capabilities:

### Query Parameters for Search

- `name` - Search by country name (partial match)
- `region` - Filter by region
- `capital` - Search by capital city
- `min_population` - Minimum population filter
- `max_population` - Maximum population filter
- `skip` - Pagination offset
- `limit` - Number of results per page

### Example Search Requests

```bash
# Search by name
GET /api/v1/countries/search?name=nepal

# Filter by region
GET /api/v1/countries/search?region=Asia

# Population range
GET /api/v1/countries/search?min_population=1000000&max_population=10000000

# Combined filters
GET /api/v1/countries/search?region=Europe&min_population=50000000
```

## Development

### Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── countries.py
│   │       └── api.py
│   ├── core/
│   │   └── config.py
│   ├── crud/
│   │   └── country.py
│   ├── models/
│   │   └── country.py
│   ├── schemas/
│   │   └── country.py
│   ├── database.py
│   └── main.py
├── requirements.txt
├── seed_data.py
└── README.md
```

### Adding New Features

1. Create models in `app/models/`
2. Define schemas in `app/schemas/`
3. Implement CRUD operations in `app/crud/`
4. Create API endpoints in `app/api/v1/`
5. Update the main router in `app/api/v1/api.py`

## Testing

Run the application and test the endpoints:

```bash
# Health check
curl http://localhost:8000/health

# Get all countries
curl http://localhost:8000/api/v1/countries/

# Search countries
curl "http://localhost:8000/api/v1/countries/search?region=Asia"
```

## Production Deployment

For production deployment:

1. Use PostgreSQL instead of SQLite
2. Set up proper environment variables
3. Use a production ASGI server like Gunicorn
4. Set up proper logging and monitoring
5. Configure reverse proxy (nginx)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.
