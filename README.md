# 🧠 AI Translator + Talking Face (Django)

This project translates English → German and generates a realistic AI talking face that speaks the translated text aloud.

## 🚀 Features
- Translate English text into German  
- Generate an AI video with a talking face  
- Simple and clean UI  
- Django backend  
- OpenAI Realtime API for talking-face generation  

## 📌 Project Structure
translator/
│── core/
│   ├── views.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── talk.html
│── translator/
│── manage.py
│── requirements.txt
│── README.md

## 🛠 Tech Used
- Python 3
- Django
- Requests
- OpenAI Realtime (for video generation)

## ▶️ How to Run
```bash
pip install -r requirements.txt
python manage.py runserver
API_KEY = "YOUR_OPENAI_API_KEY"
📹 Talking Face

Takes German text from URL /talk/?text=Hallo

Sends request to OpenAI

Returns MP4 video

📤 Deploy / Push to GitHub
git add .
git commit -m "Updated project"
git push
✅ 2. requirements.txt (copy–paste this into requirements.txt)
Django==5.0.2
requests==2.31.0
python-dotenv==1.0.1


If you used OpenAI Python SDK, add:

openai==1.55.0

📌 Add these files to Git

After creating both files, run:

git add README.md requirements.txt
git commit -m "Added README and requirements"
git push
