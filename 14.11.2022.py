#try_flask

from flask import Flask
import json

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False

@app.route('/')
def index():
    return "Hello World!"

@app.route('/sutit/<vards>/<zina')
def sutit(vards,zina):
  tagad = datetime.now()
  laiks = tagad.strftime("%Y/%m/%d, %4:%4:%5")

  print(vards,zina,laiks)

  rinda = {
     "zina":zina,
     "vards":vards,
     "laiks":laiks

  }

  with open ("chat.json","w",encoding='utf-8') as f:
    f.write(json.dumps(rinda,indent=2,ensure_ascii=False))

  return 'Ok'



@app.route('/datums')
def datums():
    return "Šodien ir 14.novembris"

@app.route('/lietotajs/<vards>/<vecums>')
def lietotajs(vards,vecums):
    #return f"{vards} un {vecums}"
    dati = {vards:vecums}
    dati_json = json.dumps(dati)
    #return dati_json
    with open("lietotaji.json","w",encoding="utf-8") as fails:
        json.dump(dati_json,fails,indent=2,ensure_ascii=False)


app.run(host='0.0.0.0', port=81)
