from flask import Flask, render_template, request, send_file

import zi_p

import linkedin_scraper
app = Flask(__name__)

@app.route('/')
def student():
   
   return render_template('index.html')
   

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result['URL'])
      linkedin_scraper.scrapper(result['URL'])
      zi_p.zipit()
      return render_template("messagescreen.html")

@app.route('/download')
def download_file():
   p = "webzip.zip"
   return send_file(p,as_attachment=True)


@app.route('/index2')
def index2():
   
   return render_template('index2.html')

if __name__ == '__main__':
   app.run(debug = True)