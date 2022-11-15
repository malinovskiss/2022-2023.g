#try_flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World!"
  
@app.route('/datums')
def datums():
  return "Šodien ir 14.novembris"

@app.route('/lietotajs/<vards>/<vecums>')
def lietotajs(vards,vecums):
  #return f"{vards} un {vecums}"
  dati = {vards:vecums}
  dati_json = json.dumps(dati)
  return dati_json
  with open("lietotaji.json","w",encoding="utf-8") as fails:
    json.dump(dati_json,fails,indent=2,ensure_ascil=False)

app.run(host='0.0.0.0', port=81)