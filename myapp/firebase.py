import pyrebase

# Pyrebase Configuration
firebaseConfig = { 
    "apiKey": "AIzaSyDUMuIv9PTQfEmjR-VhGozh3K7csIpB8lE",
    "authDomain": "djangoauth-7053d.firebaseapp.com",
    "databaseURL": "https://djangoauth-7053d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "djangoauth-7053d",
    "storageBucket": "djangoauth-7053d.firebasestorage.app",
    "messagingSenderId": "732802255513",
    "appId": "1:732802255513:web:b3ef371bb7d40593d34608",
    "measurementId": "G-LVLB7JY0N1"
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth_instance = firebase.auth()
storage = firebase.storage()  # Initialize Firebase Storage

# Path to the Firebase Admin SDK service account key file
service_account_path = 'D:/4th Year Files/djangoauth-7053d-firebase-adminsdk-g1h6n-8f9923e28c.json'
 