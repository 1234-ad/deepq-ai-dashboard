# Deployment Guide - DeepQ-AI Dashboard

This guide provides step-by-step instructions for deploying the DeepQ-AI Dashboard to various platforms.

## 🚀 Quick Local Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Automated Setup
```bash
# Clone the repository
git clone https://github.com/1234-ad/deepq-ai-dashboard.git
cd deepq-ai-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run automated setup
python setup.py
```

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver
```

## 🌐 Production Deployment

### 1. Heroku Deployment

#### Prerequisites
- Heroku CLI installed
- Heroku account

#### Steps
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-deepq-dashboard

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:mini

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Collect static files
heroku run python manage.py collectstatic --noinput
```

#### Environment Variables for Heroku
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.herokuapp.com
DATABASE_URL=postgres://... (automatically set by Heroku)
```

### 2. Render Deployment

#### Prerequisites
- Render account
- GitHub repository

#### Steps
1. **Connect GitHub Repository**
   - Go to Render Dashboard
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Service**
   ```
   Name: deepq-ai-dashboard
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn dashboard_project.wsgi:application
   ```

3. **Environment Variables**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   PYTHON_VERSION=3.11.5
   ```

4. **Database Setup**
   - Add PostgreSQL database service
   - Copy DATABASE_URL to web service environment variables

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete

#### Post-Deployment Commands
```bash
# SSH into Render service or use Render Shell
python manage.py migrate
python manage.py setup_demo
python manage.py collectstatic --noinput
```

### 3. Railway Deployment

#### Prerequisites
- Railway account
- GitHub repository

#### Steps
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up

# Set environment variables
railway variables set SECRET_KEY="your-secret-key"
railway variables set DEBUG=False

# Add PostgreSQL
railway add postgresql

# Run migrations
railway run python manage.py migrate
railway run python manage.py setup_demo
```

### 4. DigitalOcean App Platform

#### Prerequisites
- DigitalOcean account
- GitHub repository

#### Steps
1. **Create App**
   - Go to DigitalOcean Apps
   - Create App from GitHub repository

2. **Configure App**
   ```yaml
   # app.yaml
   name: deepq-ai-dashboard
   services:
   - name: web
     source_dir: /
     github:
       repo: your-username/deepq-ai-dashboard
       branch: main
     run_command: gunicorn dashboard_project.wsgi:application
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: SECRET_KEY
       value: your-secret-key
     - key: DEBUG
       value: "False"
   databases:
   - name: db
     engine: PG
     version: "13"
   ```

## 🔧 Environment Configuration

### Required Environment Variables
```bash
SECRET_KEY=your-django-secret-key
DEBUG=False  # Set to True for development
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgres://user:pass@host:port/dbname  # For PostgreSQL
```

### Optional Environment Variables
```bash
# Email configuration (for password reset, etc.)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Static files (for custom CDN)
STATIC_URL=/static/
STATIC_ROOT=/app/staticfiles/

# Security settings
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

## 🗄️ Database Configuration

### SQLite (Development)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### PostgreSQL (Production)
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

## 📊 Monitoring & Logging

### Application Monitoring
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Health Check Endpoint
Add to `dashboard/urls.py`:
```python
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'healthy', 'timestamp': timezone.now()})

urlpatterns = [
    # ... existing patterns
    path('health/', health_check, name='health_check'),
]
```

## 🔒 Security Checklist

### Pre-Deployment Security
- [ ] Set `DEBUG = False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` properly
- [ ] Enable HTTPS redirects
- [ ] Set up CSRF protection
- [ ] Configure secure headers
- [ ] Use environment variables for secrets
- [ ] Enable database connection encryption

### Post-Deployment Security
- [ ] Set up SSL certificate
- [ ] Configure firewall rules
- [ ] Enable database backups
- [ ] Set up monitoring and alerts
- [ ] Regular security updates
- [ ] Access logging and monitoring

## 🚨 Troubleshooting

### Common Issues

#### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT and STATIC_URL settings
# Ensure WhiteNoise is configured properly
```

#### Database Connection Errors
```bash
# Check DATABASE_URL format
# Verify database credentials
# Ensure database server is accessible
```

#### Import Errors
```bash
# Check Python version compatibility
# Verify all dependencies are installed
pip install -r requirements.txt
```

#### World Bank API Timeouts
```python
# Increase timeout in views.py
response = requests.get(url, params=params, timeout=30)
```

### Performance Optimization

#### Database Optimization
```python
# Add database indexes
class WorldBankData(models.Model):
    # ... fields
    class Meta:
        indexes = [
            models.Index(fields=['country_code', 'year']),
            models.Index(fields=['indicator_code', 'year']),
        ]
```

#### Caching
```python
# Add Redis caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

## 📞 Support

For deployment issues or questions:
- Check the [GitHub Issues](https://github.com/1234-ad/deepq-ai-dashboard/issues)
- Review Django deployment documentation
- Contact: jotevot109@baxidy.com

---

**Last Updated:** August 18, 2025  
**Version:** 1.0.0