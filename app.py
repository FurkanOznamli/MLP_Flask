from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

with open("sigorta_ucreti_tahmin_modeli.pkl", "rb") as f:
    model, encoder = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    tahmin = None
    
    if request.method == "POST":
        yas = float(request.form["yas"])
        bmi = float(request.form["bmi"])
        cocuk = float(request.form["cocuk"])
        cinsiyet = request.form["cinsiyet"]
        sigara = request.form["sigara"]
        bolge = request.form["bolge"]

        # DataFrame formatında girdi oluşturuyoruz
        input_df = pd.DataFrame([{
            "yas": yas,
            "cinsiyet": cinsiyet,
            "vucut_kitle_indeksi": bmi,
            "cocuk_sayisi": cocuk,
            "sigara_iciyor_mu": sigara,
            "bolge": bolge
        }])

        # One-Hot Encoding
        input_encoded = encoder.transform(input_df)

        # Tahmin yap
        tahmin = model.predict(input_encoded)[0]
        tahmin = round(tahmin, 2)

    return render_template("index.html", tahmin=tahmin)

if __name__ == "__main__":
    app.run(debug=True)
