from flask import Flask, render_template
import requests

app = Flask(__name__)

# Halaman utama dengan tombol/tab liga
@app.route('/')
def home():
    return render_template("home.html")

# Klasemen Liga Inggris
@app.route('/premierleague')
def premier_league():
    url = "https://premier-league-standings1.p.rapidapi.com/"

    headers = {
	"x-rapidapi-key": "035dd2649bmshcfa3a58921ad63cp1022c1jsn4e3c0b56f801",
	"x-rapidapi-host": "premier-league-standings1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    klasemen = response.json()
    return render_template('premier.html', klasemen=klasemen)

# Klasemen Liga Spanyol
@app.route('/laliga')
def laliga():
    url = "https://laliga-standings.p.rapidapi.com/"

    headers = {
	"x-rapidapi-key": "035dd2649bmshcfa3a58921ad63cp1022c1jsn4e3c0b56f801",
	"x-rapidapi-host": "laliga-standings.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    klasemen = response.json()
    return render_template('laliga.html', klasemen=klasemen)

# Klasemen Serie A
@app.route('/seriea')
def serie_a():
    url = "https://serie-a-standings.p.rapidapi.com/"
    headers = {
        "x-rapidapi-key": "ac2de6ff01msha261f7c9809c707p1f525djsnba0b4eb55c92",
        "x-rapidapi-host": "serie-a-standings.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    klasemen = response.json()
    return render_template('seriea.html', klasemen=klasemen)

if __name__ == '__main__':
    app.run(debug=True)
