from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

# 🕉️ Custom Quotes (Hinglish) from Bhagavad Gita & Ramayana
spiritual_quotes = [
    ("Karm karo, phal ki chinta mat karo.", "Bhagavad Gita"),
    ("Yeh sharir nashwar hai, atma amar hai.", "Bhagavad Gita"),
    ("Jab jab dharm ki hani hoti hai, tab tab main avtar leta hoon.", "Bhagavad Gita"),
    ("Maryada purushottam banna asaan nahi hota.", "Ramayana"),
    ("Apne kartavya se kabhi mat bhatakna, yahi sachcha dharm hai.", "Ramayana"),
    ("Satya aur dharm ki jeet hamesha hoti hai.", "Ramayana"),
    ("Jo hua achha hua, jo ho raha hai wo bhi achha ho raha hai.", "Bhagavad Gita")
]

def fetch_quote(mood):
    # Handle special spiritual/dharmic mood
    if mood.lower() in ["spiritual", "dharmic"]:
        quote, author = random.choice(spiritual_quotes)
        return quote, author

    # Default: Fetch from ZenQuotes
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            return quote, author
        else:
            return "Couldn't fetch quote at this time.", ""
    except Exception as e:
        return f"Error: {str(e)}", ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quote', methods=['POST'])
def get_quote():
    mood = request.json.get('mood', '')
    quote, author = fetch_quote(mood)
    return jsonify({'quote': quote, 'author': author})

if __name__ == '__main__':
    app.run(debug=True)
