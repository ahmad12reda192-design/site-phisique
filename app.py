from flask import Flask
app = Flask(__name__)

STYLE = "<style>body{font-family:Arial;background:#f0f4ff;text-align:center;padding:30px}h1{color:#1a3cff}.card{background:white;padding:20px;margin:15px auto;max-width:600px;border-radius:15px;box-shadow:0 4px 10px #ccc}a{display:inline-block;background:#1a3cff;color:white;padding:12px 25px;margin:5px;border-radius:10px;text-decoration:none;font-weight:bold}a:hover{background:#ff6600}</style>"

@app.route("/")
def home():
    return STYLE + "<h1>Physique B Darija</h1><p>Salam! Hna ghadi tfhem Physique b Darija sahla</p><div class='card'><h2>Chno bghiti t3lem?</h2><a href='/dars1'>Dars 1 : Chnahiya Physique</a><br><br><a href='/dars2'>Dars 2 : Lharaka</a><br><br><a href='/dars3'>Dars 3 : L9owa</a></div>"

@app.route("/dars1")
def dars1():
    return STYLE + "<h1>Dars 1 : Chnahiya Physique</h1><div class='card'><p>Physique howa 3ilm li kaychre7 lina kifach khedam l3alam.</p><p>3lach tay7et tefaha? 3lach taytir lbolon? Hadchi kamel howa Physique!</p></div><a href='/'>Rje3 l Accueil</a> <a href='/dars2'>Dars Jdid -></a>"

@app.route("/dars2")
def dars2():
    return STYLE + "<h1>Dars 2 : Lharaka</h1><div class='card'><p>Lharaka hiya mli chi haja katbedel blastha.</p><p>Exemple: Tomobil ghadi, bnadem kayjri, kora katdour.</p><p>Kolchi f lharaka 3ndo Sor3a - wach ghadi bchwiya wla bzerba?</p></div><a href='/'>Rje3 l Accueil</a> <a href='/dars3'>Dars Jdid -></a>"

@app.route("/dars3")
def dars3():
    return STYLE + "<h1>Dars 3 : L9owa</h1><div class='card'><p>L9owa hiya li katkhli chi haja tbda t7erek wla t7bes.</p><p>Exemple: Mli katdefe3 lbit, katsta3mel 9owa.</p><p>Mli katjer l9er3a, katsta3mel 9owa.</p></div><a href='/'>Rje3 l Accueil</a>"

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)