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
  return f"{vards} un {vecums}"
  with open("lietotaji.json","w",encoding="utf-8") as fails:

app.run(host='0.0.0.0', port=81)