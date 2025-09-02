Bolo Na is a Flask-based web application that allows users to receive anonymous messages from others. Users can create an account, share their unique public link, and receive messages that only they can view in their private inbox.

###**Features**
🔐 User authentication system
🌐 Public message submission forms for each user
📥 Private inbox to view received messages
🎨 Modern, responsive UI with animated elements
🔒 Anonymous messaging system
📊 Character counter for messages

### **Project Structure**
bolo-na/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── home.html         # Login page
│   ├── dashboard.html    # User dashboard
│   ├── public.html       # Public message form
│   ├── thankyou.html     # Confirmation page
│   └── inbox.html        # Message inbox
└── static/
&nbsp;   ├── style.css         # Main stylesheet
&nbsp;   └── final.png         # Application logo

### **Installation \& Setup**
1. Clone the repository:
git clone <your-repository-url>
cd bolo-na

2\. Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3\. Install required dependencies:
pip install flask

4\. Run the application:
python app.py

5.Open your browser and navigate to http://localhost:5000

### **Default Credentials**
The application comes with a pre-configured user:
Username: Rohan
Password: 1234

### **Security Notes**
Change the app.secret\_key in app.py before deploying to production
Consider using a more secure password storage method (hashing) in production
Add rate limiting to prevent spam

##### **Customization**
Modify the color scheme by editing the CSS variables in style.css
Add more users by updating the passwords dictionary in app.py
Customize the logo by replacing static/final.png

### **Technologies Used**
Backend: Flask (Python)
Frontend: HTML5, CSS3 with custom animations
No database required (in-memory storage for demo purposes)

##### **License**
This project is open source and available under the MIT License.

##### **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.
