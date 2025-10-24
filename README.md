# Country Information App - Full Stack Project

A comprehensive full-stack application built with React frontend and Python FastAPI backend for managing and exploring country information.

## 🌟 Features

### Frontend (React)

- **Modern React 19** with Vite for fast development
- **Responsive Design** with beautiful UI/UX
- **Country Search & Filtering** with real-time results
- **Country Details** with comprehensive information
- **Admin Panel** for managing country data
- **Router Navigation** with React Router DOM
- **External API Integration** with fallback support

### Backend (Python FastAPI)

- **RESTful API** with FastAPI framework
- **SQLAlchemy ORM** for database operations
- **Comprehensive CRUD** operations
- **Advanced Search & Filtering** capabilities
- **Automatic API Documentation** with Swagger UI
- **CORS Support** for frontend integration
- **Data Validation** with Pydantic models
- **Database Seeding** with sample data

## 🚀 Tech Stack

### Frontend

- **React 19** - Latest React with concurrent features
- **Vite** - Fast build tool and dev server
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client for API calls
- **React Icons** - Icon library
- **CSS3** - Modern styling with gradients and animations

### Backend

- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **SQLite/PostgreSQL** - Database support
- **Alembic** - Database migrations

## 📁 Project Structure

```
react_country_thapa/
├── src/                          # React Frontend
│   ├── components/
│   │   ├── Layout/
│   │   └── UI/
│   ├── pages/
│   ├── api/
│   └── styles/
├── backend/                       # Python Backend
│   ├── app/
│   │   ├── api/v1/
│   │   ├── core/
│   │   ├── crud/
│   │   ├── models/
│   │   └── schemas/
│   ├── requirements.txt
│   └── seed_data.py
└── README.md
```

## 🛠️ Installation & Setup

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn**

### 1. Clone the Repository

```bash
git clone <repository-url>
cd react_country_thapa
```

### 2. Frontend Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at: http://localhost:5173

### 3. Backend Setup

#### Option A: Using Batch File (Windows)

```bash
cd backend
start_backend.bat
```

#### Option B: Using Shell Script (Linux/Mac)

```bash
cd backend
chmod +x start_backend.sh
./start_backend.sh
```

#### Option C: Manual Setup

```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Seed database with sample data
python seed_data.py

# Start the server
python run_server.py
```

Backend will be available at: http://localhost:8000

## 📚 API Documentation

Once the backend is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **API Health Check**: http://localhost:8000/health

## 🔧 API Endpoints

### Countries

- `GET /api/v1/countries/` - Get all countries (paginated)
- `GET /api/v1/countries/search` - Search countries with filters
- `GET /api/v1/countries/{id}` - Get country by ID
- `GET /api/v1/countries/name/{name}` - Get country by name
- `GET /api/v1/countries/region/{region}` - Get countries by region
- `GET /api/v1/countries/stats/overview` - Get statistics
- `POST /api/v1/countries/` - Create new country
- `PUT /api/v1/countries/{id}` - Update country
- `DELETE /api/v1/countries/{id}` - Delete country

## 🎯 Key Features

### Frontend Features

1. **Country Browser** - Browse all countries with pagination
2. **Advanced Search** - Search by name, region, capital
3. **Filter by Region** - Filter countries by geographic region
4. **Country Details** - Detailed view with comprehensive information
5. **Admin Panel** - Full CRUD operations for country management
6. **Responsive Design** - Works on all device sizes
7. **Error Handling** - Graceful fallbacks and error states

### Backend Features

1. **RESTful API** - Clean, well-documented endpoints
2. **Database Models** - Structured country data model
3. **Search & Filtering** - Advanced query capabilities
4. **Data Validation** - Input validation and error handling
5. **CORS Support** - Cross-origin resource sharing
6. **Auto Documentation** - Interactive API documentation
7. **Database Seeding** - Sample data for testing

## 🗄️ Database Schema

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

## 🚀 Deployment

### Frontend Deployment

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

### Backend Deployment

For production deployment:

1. Use PostgreSQL instead of SQLite
2. Set up environment variables
3. Use a production ASGI server like Gunicorn
4. Configure reverse proxy (nginx)
5. Set up proper logging and monitoring

## 🧪 Testing

### Frontend Testing

```bash
# Run linting
npm run lint

# Build test
npm run build
```

### Backend Testing

```bash
cd backend

# Test API endpoints
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/countries/
```

## 📈 Performance Features

- **Lazy Loading** - Components loaded on demand
- **Pagination** - Efficient data loading
- **Caching** - API response caching
- **Optimized Queries** - Database query optimization
- **Responsive Images** - Optimized image loading
- **Code Splitting** - Reduced bundle size

## 🎨 UI/UX Features

- **Modern Design** - Clean, professional interface
- **Gradient Backgrounds** - Beautiful visual effects
- **Smooth Animations** - Enhanced user experience
- **Responsive Layout** - Mobile-first design
- **Loading States** - User feedback during operations
- **Error Boundaries** - Graceful error handling

## 🔒 Security Features

- **Input Validation** - Server-side validation
- **CORS Configuration** - Secure cross-origin requests
- **SQL Injection Prevention** - ORM-based queries
- **Data Sanitization** - Clean input processing

## 📱 Mobile Responsiveness

- **Mobile-First Design** - Optimized for mobile devices
- **Touch-Friendly Interface** - Easy navigation on touch screens
- **Responsive Grid** - Adaptive layout system
- **Optimized Performance** - Fast loading on mobile

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Resume Value

This full-stack project demonstrates:

- **Frontend Skills**: React 19, Modern JavaScript, CSS3, Responsive Design
- **Backend Skills**: Python, FastAPI, SQLAlchemy, RESTful APIs
- **Database Skills**: SQL, ORM, Data Modeling
- **DevOps Skills**: Environment Setup, API Documentation
- **Full-Stack Integration**: Frontend-Backend Communication
- **Modern Development**: Latest frameworks and best practices

Perfect for showcasing your full-stack development capabilities!
