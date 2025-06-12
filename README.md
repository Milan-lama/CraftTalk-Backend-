# CraftTalk - Real-Time Chat Application Backend

A robust Django-based backend system for a real-time chat application with WebSocket support and secure user authentication.

## 🚀 Features

- **Real-Time Communication:** WebSocket-based chat functionality using Django Channels
- **Secure Authentication:** Token-based authentication system
- **Message Management:** Store and retrieve chat messages
- **User Management:** Complete user registration and authentication system
- **PostgreSQL Database:** Reliable data storage with PostgreSQL
- **CORS Support:** Configured for cross-origin resource sharing
- **RESTful API:** Well-structured API endpoints

## 🛠️ Technologies Used

- Django 5.0.7
- Django Channels
- Django REST Framework 
- PostgreSQL
- Token Authentication
- WebSockets
- CORS Headers

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual Environment (recommended)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CraftTalk-Backend.git
   cd CraftTalk-Backend
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**
   - Create a database named 'crafttalk2'
   - Update database settings in `CraftTalk/settings.py` if needed

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the server**
   ```bash
   python manage.py runserver
   ```

## 🌐 API Endpoints

### Authentication
- `POST /api/login/` - User login
- `POST /api/userapi/` - User registration
- `GET /api/userapi/` - Get all users

### Messages
- `GET /api/ShowMessages/<str:receiver>/` - Get chat messages
- `WS /ws/socket-server/<str:username>/` - WebSocket endpoint for real-time chat

## 💻 WebSocket Usage

Connect to WebSocket with authentication token:
```javascript
const socket = new WebSocket(`ws://localhost:8000/ws/socket-server/${username}/?token=${authToken}`);
```

## 🔐 Environment Variables

Configure in `CraftTalk/settings.py`:
```python
SECRET_KEY = "your-secret-key"
DEBUG = True/False
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crafttalk2',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Milan Lama - mlama0018@gmail.com
Project Link: [https://github.com/yourusername/CraftTalk-Backend](https://github.com/yourusername/CraftTalk-Backend)
