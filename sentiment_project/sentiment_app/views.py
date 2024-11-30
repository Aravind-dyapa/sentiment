import pickle
from django.shortcuts import render
import os
from django.conf import settings

# Use the absolute path based on the project base directory
MODEL_PATH = os.path.join(settings.BASE_DIR, 'sentiment_app', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(settings.BASE_DIR, 'sentiment_app', 'vectorizer.pkl')

# Load model and vectorizer
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

def index(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")  # Using get() to avoid KeyError
        if user_input:  # Check if user_input is not empty
            input_vector = vectorizer.transform([user_input])
            result = model.predict(input_vector)[0]  # Get the prediction result
    
    return render(request, "index.html", {"result": result})
