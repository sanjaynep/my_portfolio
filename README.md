# My Portfolio

A personal portfolio website built with Django, showcasing projects, skills, and providing a contact form for potential clients or employers to reach out.

## 🚀 Features

- **Responsive Design**:  Mobile-friendly portfolio website
- **Contact Form**: Integrated contact form for visitor inquiries
- **Project Showcase**: Display your projects and work
- **Admin Panel**: Django admin interface for easy content management
- **PostgreSQL Database**: Production-ready database support
- **Static Files Management**: Efficient static files handling with WhiteNoise

## 🛠️ Tech Stack

- **Framework**: Django 6.0+
- **Database**: PostgreSQL (with psycopg2-binary)
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Python Version**: 3.13+
- **Package Manager**: uv (modern Python package manager)

## 📋 Prerequisites

- Python 3.13 or higher
- PostgreSQL (for production)
- pip or uv package manager

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sanjaynep/my_portfolio. git
cd my_portfolio
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

Using pip: 
```bash
pip install -r requirements.txt
```

Or using uv:
```bash
uv pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root directory and add your configuration:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost: 5432/portfolio_db
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup

Run migrations to set up the database: 

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Collect static files

```bash
python manage.py collectstatic
```

## 🚀 Running the Application

### Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

### Production Server

```bash
gunicorn portfolio.wsgi:application
```

## 📁 Project Structure

```
my_portfolio/
├── myapp/              # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── forms.py        # Contact form
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configuration
├── portfolio/          # Project settings
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL configuration
│   ├── wsgi.py         # WSGI configuration
│   └── asgi. py         # ASGI configuration
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project metadata
└── . env                # Environment variables (not in repo)
```

## 🎨 Customization

1. **Update Templates**:  Modify HTML files in the `templates/` directory
2. **Style Changes**: Edit CSS files in the `static/` directory
3. **Add Projects**: Use the Django admin panel at `/admin` to add new projects
4. **Contact Form**: Customize the contact form in `myapp/forms.py`

## 📝 Available Models

- **Contact**:  Stores contact form submissions with fields like name, email, and message

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Keep your `SECRET_KEY` secure
- Set `DEBUG=False` in production
- Update `ALLOWED_HOSTS` with your domain names

## 📦 Dependencies

- **django**:  Web framework
- **psycopg2-binary**: PostgreSQL adapter
- **dj-database-url**: Database URL parser
- **gunicorn**:  WSGI HTTP server
- **whitenoise**:  Static file serving
- **python-dotenv**: Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Sanjay Nepal**
- GitHub: [@sanjaynep](https://github.com/sanjaynep)

## 📞 Contact

For any inquiries, please use the contact form on the website or open an issue on GitHub. 

---

⭐ If you found this project helpful, please consider giving it a star! 
