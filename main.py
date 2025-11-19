
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app  = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Tarjimon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uz = db.Column(db.String(100), nullable=False)
    en = db.Column(db.String(100), nullable=False)
    created_at =  db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Tarjimon: {self.uz} - {self.en}"


# http://127.0.0.1:5000/?izlash=dog
# http://127.0.0.1:5000/?izlash=car

@app.route("/")
def home():
    soz = request.args.get("izlash")
    natija = Tarjimon.query.filter_by(en=soz).first()
    return render_template("index.html", natija=natija)


@app.route("/malumot_qosh")
def malumotlar_qoshish():
    tarjimon_sozlar = {
        "mushuk": "cat",
        "it": "dog",
        "uy": "house",
        "odam": "person",
        "bola": "child",
        "ona": "mother",
        "ota": "father",
        "do‘st": "friend",
        "suv": "water",
        "ovqat": "food",
        "non": "bread",
        "choy": "tea",
        "kitob": "book",
        "mashina": "car",
        "telefon": "phone",
        "ism": "name",
        "yaxshi": "good",
        "katta": "big",
        "kichik": "small",
        "issiq": "hot",
        "sovuq": "cold",
        "tez": "fast",
        "sekin": "slow",
        "oq": "white",
        "qora": "black",
        "qizil": "red",
        "ko‘k": "blue",
        "yashil": "green",
        "kun": "day",
        "tun": "night",
        "ertalab": "morning",
        "kech": "evening",
        "hozir": "now",
        "keyin": "later",
        "oldin": "before",
        "men": "I",
        "sen": "you",
        "u": "he/she/it",
        "biz": "we",
        "siz": "you (plural/polite)",
        "ular": "they",
        "bor": "there is/are",
        "yo‘q": "no / there isn’t",
        "ha": "yes",
        "rahmat": "thank you",
        "iltimos": "please",
        "salom": "hello",
        "xayr": "goodbye",
        "qandaysiz": "how are you",
        "yaxshiman": "I’m fine",
        "va": "and",
        "lekin": "but",
        "yoki": "or",
        "agar": "if",
        "chunki": "because",
        "bir": "one",
        "ikki": "two",
        "uch": "three",
        "to‘rt": "four",
        "besh": "five",
        "olti": "six",
        "yetti": "seven",
        "sakkiz": "eight",
        "to‘qqiz": "nine",
        "o‘n": "ten",
        "yigirma": "twenty",
        "yuz": "hundred",
        "ming": "thousand",
        "ish": "work",
        "maktab": "school",
        "universitet": "university",
        "o‘qituvchi": "teacher",
        "o‘quvchi": "student",
        "shifokor": "doctor",
        "kasal": "sick",
        "dorixona": "pharmacy",
        "pul": "money",
        "do‘kon": "shop",
        "bozor": "market",
        "oshxona": "kitchen",
        "xona": "room",
        "eshik": "door",
        "deraza": "window",
        "stul": "chair",
        "stol": "table",
        "yoz": "write",
        "o‘qi": "read",
        "ko‘r": "see",
        "bor": "go",
        "kel": "come",
        "ol": "take",
        "ber": "give",
        "gapir": "speak",
        "tingla": "listen",
        "tushun": "understand",
        "sev": "love",
        "yoqtir": "like",
        "xohla": "want",
        "kerak": "need",
        "bugun": "today",
        "erta": "tomorrow",
        "kecha": "yesterday",
        "hafta": "week",
        "oy": "month",
        "yil": "year"
    }
    
    # for uz,en in tarjimon_sozlar.items():
    #     soz = Tarjimon(
    #         uz=uz,
    #         en=en
    #     )
    #     db.session.add(soz)
    #     db.session.commit()
    return redirect(url_for("home"))


@app.route("/soz_qosh", methods=["POST"])
def soz_qosh():
    en = request.form.get("en")
    uz = request.form.get("uz")
    checking = Tarjimon.query.filter_by(en=en, uz=uz).first()
    if not checking:
        soz = Tarjimon(
            uz=uz,
            en=en
        )
        db.session.add(soz)
        db.session.commit()
    return redirect(url_for("home"))







if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)