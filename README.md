# DeepQ-AI Dashboard - Full Stack Developer Intern Assignment

An interactive Django web application that displays World Bank data through dynamic charts and graphs.

## 🚀 Features

### Dashboard Features
- **Interactive Charts**: Line charts, bar charts, and area charts using Chart.js
- **Dynamic Data**: Real-time data fetching from World Bank Open Data API
- **Filtering System**: Filter by countries, date ranges, and categories
- **Responsive Design**: Mobile-friendly Bootstrap interface

### Authentication
- Django built-in authentication system
- Login/logout functionality
- Protected dashboard access for authenticated users only

### Data Visualization
1. **GDP Trends (Line Chart)**: Shows GDP over time for selected countries
2. **Population Comparison (Bar Chart)**: Compares population across countries
3. **CO2 Emissions (Area Chart)**: Environmental data visualization over time

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5, Chart.js
- **Database**: SQLite (development), PostgreSQL (production)
- **API**: World Bank Open Data API
- **Deployment**: Heroku/Render ready

## 📊 Data Source

**World Bank Open Data**
- URL: https://data.worldbank.org/
- Indicators Used:
  - GDP (Current US$): `NY.GDP.MKTP.CD`
  - Population Total: `SP.POP.TOTL`
  - CO2 Emissions: `EN.ATM.CO2E.KT`

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/1234-ad/deepq-ai-dashboard.git
   cd deepq-ai-dashboard
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Dashboard: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

### Demo Credentials
- Username: `admin`
- Password: `admin123`

## 🌐 Deployment

### Heroku Deployment

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Alternative Deployment Options
- **Render**: Connect GitHub repo and deploy
- **Vercel**: For static frontend deployment
- **Netlify**: For static site hosting
- **Railway**: Simple deployment platform

## 📁 Project Structure

```
deepq-ai-dashboard/
├── dashboard_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashboard/                  # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/                  # HTML templates
│   ├── base.html
│   ├── dashboard/
│   │   └── dashboard.html
│   └── registration/
│       └── login.html
├── static/                     # Static files (CSS, JS, images)
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
├── Procfile                    # Heroku deployment
├── runtime.txt                 # Python version
└── README.md                   # Project documentation
```

## 🔧 API Endpoints

- `GET /api/gdp-data/` - GDP data with country and year filters
- `GET /api/population-data/` - Population data with filters
- `GET /api/co2-data/` - CO2 emissions data with filters

### Query Parameters
- `countries`: Semicolon-separated country codes (e.g., `US;CN;IN`)
- `start_year`: Start year for data range
- `end_year`: End year for data range

## 🎨 Features Implemented

### ✅ Required Features
- [x] Django backend with REST API
- [x] Interactive dashboard with multiple chart types
- [x] Dynamic data fetching from backend
- [x] Filtering system (countries, date ranges)
- [x] User authentication (login/logout)
- [x] Protected dashboard access
- [x] World Bank Open Data integration
- [x] Deployment ready

### ✅ Additional Features
- [x] Responsive design
- [x] Loading indicators
- [x] Error handling
- [x] Professional UI/UX
- [x] Multiple chart types (Line, Bar, Area)
- [x] Real-time data updates
- [x] Admin interface
- [x] Documentation

## 🔒 Security Features

- CSRF protection
- User authentication required
- Secure session management
- Environment variable configuration
- SQL injection protection (Django ORM)

## 📱 Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is created for the DeepQ-AI Full Stack Developer Intern assignment.

## 👨‍💻 Developer

Created by: **Your Name**
- GitHub: [@1234-ad](https://github.com/1234-ad)
- Assignment: DeepQ-AI Full Stack Developer Intern Position

## 📞 Support

For any questions or issues, please create an issue in the GitHub repository.

---

**Assignment Completion Date**: August 25, 2025
**Company**: DeepQ-AI
**Position**: Full Stack Developer Intern