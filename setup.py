#!/usr/bin/env python3
"""
Setup script for DeepQ-AI Dashboard
Automates the initial setup process
"""

import os
import sys
import subprocess
import django
from django.core.management import execute_from_command_line

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Output: {e.output}")
        return False

def main():
    print("🚀 DeepQ-AI Dashboard Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)
    
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_project.settings')
    django.setup()
    
    # Run migrations
    print("\n🔄 Running database migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    print("✅ Database migrations completed")
    
    # Collect static files
    print("\n🔄 Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    print("✅ Static files collected")
    
    # Set up demo data
    print("\n🔄 Setting up demo users...")
    execute_from_command_line(['manage.py', 'setup_demo'])
    print("✅ Demo users created")
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Demo Credentials:")
    print("   Admin: admin / admin123")
    print("   User:  demo / demo123")
    print("\n🚀 To start the server:")
    print("   python manage.py runserver")
    print("\n🌐 Access the dashboard at:")
    print("   http://localhost:8000/")
    print("=" * 50)

if __name__ == "__main__":
    main()