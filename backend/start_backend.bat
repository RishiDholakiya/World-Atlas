@echo off
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Seeding database with sample data...
python seed_data.py

echo.
echo Starting FastAPI server...
echo Server will be available at: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo.
python run_server.py

pause
