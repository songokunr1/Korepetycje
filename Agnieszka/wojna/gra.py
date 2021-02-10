from flask import Flask, render_template, request
from collections import OrderedDict

app = Flask(__name__)

def generuj_talie():
   t = set()
   for kolor in ('kier',): #, 'karo', 'pik', 'trefl'):
      for wartosc in range(1, 14):
         t.add( (wartosc, kolor) )
   return t

rece = list()




@app.route("/")
def index():
   global rece

   talia = generuj_talie()
   rece = [ [], [] ]
   i = 0
   for k in talia:
      rece[i].append(k)
      i += 1
      i %= 2
   return render_template('index.html')



@app.route("/gra")
def gra():
   global rece

   i = 0
   for r in rece:
      if not r:
         wygral = (i + 1) % 2
         return render_template('gra_end.html', wygral=wygral)
      i += 1

   k = list()
   print(rece)
   k.append( rece[0].pop() )
   k.append( rece[1].pop() )

   if k[0] > k[1]:
      rece[0] = [k[0]] + rece[0]
      rece[0] = [k[1]] + rece[0]
   elif k[0] < k[1]:
      rece[1] = [k[0]] + rece[1]
      rece[1] = [k[1]] + rece[1]
   else:
      rece[0] = [k[0]] + rece[0]
      rece[1] = [k[1]] + rece[1]

   return render_template('gra.html', rece=rece)




if __name__ == "__main__":
   app.run(port=5005, debug=True)
