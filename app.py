from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [
  {
    'id': 1,
    'title': 'Web Deevelopment',
    'time': '5 days'
  },
  {
    'id': 2,
    'title': 'App Deevelopment',
    'time': '7 days'
  },
  {
    'id': 3,
    'title': 'Logo Design',
    'time': '2 days'
  },
]


@app.route("/")
def hello_raj():
  return render_template('index.html', service=SERVICES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
