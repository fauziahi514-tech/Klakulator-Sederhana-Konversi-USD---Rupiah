import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def ambil_kurs_terbaru():
    try:
        # Mengambil data kurs terbaru USD ke IDR
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        data = response.json()
        # Mengambil nilai IDR dari daftar mata uang
        return data['rates']['IDR']
    except:
        # Jika internet mati, gunakan angka cadangan
        return 16200 

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    usd = None
    kurs = ambil_kurs_terbaru()
    
    if request.method == 'POST':
        try:
            usd = float(request.form['usd'])
            total = usd * kurs
            # Format rupiah: titik untuk ribuan, koma untuk desimal
            hasil = "{:,.2f}".format(total).replace(",", "X").replace(".", ",").replace("X", ".")
        except ValueError:
            hasil = "Error: Input tidak valid"

    return render_template('index.html', hasil=hasil, usd=usd, kurs=round(kurs, 2))

if __name__ == '__main__':
    app.run(debug=True)