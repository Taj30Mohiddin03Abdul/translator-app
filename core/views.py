from django.shortcuts import render
from django.shortcuts import redirect
from googletrans import Translator
from .models import TranslationHistory
from django.conf import settings
import requests
import time

def translate_text(request):
    translated_text = ""
    english_text = ""

    # Load all history (latest first)
    history = TranslationHistory.objects.all().order_by('-timestamp')

    if request.method == "POST":
        english_text = request.POST.get("english_text")

        translator = Translator()
        translated = translator.translate(english_text, src='en', dest='de')
        translated_text = translated.text

        # Save to database
        TranslationHistory.objects.create(
            english_text=english_text,
            german_text=translated_text
        )

        # Refresh history after adding
        history = TranslationHistory.objects.all().order_by('-timestamp')

    return render(request, "index.html", {
        "english_text": english_text,
        "translated_text": translated_text,
        "history": history
    })

def clear_history(request):
    TranslationHistory.objects.all().delete()
    return redirect("translate")


DID_API_KEY = "YWJkdWx0YWptb2hpZGRpbjMwNTAzQGdtYWlsLmNvbQ:ahalczS6OjwfF2XUuREOG"

def ai_talk(request):
    text = request.GET.get("text", "")
    video_url = None

    if text:
        # 1. Create video task
        create_url = "https://api.d-id.com/talks"
        headers = {
            "Authorization": DID_API_KEY,
            "Content-Type": "application/json"
        }

        payload = {
            "script": {
                "type": "text",
                "input": text,
                "voice_id": "de-DE-TanjaNeural"
            },
            "source_url": "https://i.imgur.com/jQ6sF.jpg"
        }

        response = requests.post(create_url, json=payload, headers=headers).json()
        talk_id = response.get("id")

        # 2. Poll until the video is ready
        if talk_id:
            status_url = f"https://api.d-id.com/talks/{talk_id}"

            for _ in range(15):  # wait max 15 × 1 sec = 15 seconds
                status = requests.get(status_url, headers=headers).json()

                if "result" in status and "url" in status["result"]:
                    video_url = status["result"]["url"]
                    break

                time.sleep(1)  # wait 1 second

    return render(request, "talk.html", {
        "text": text,
        "video_url": video_url
    })