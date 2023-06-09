from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
 {
  'author':"Jesse Mucheke",
  'title':"The day that rains",
  'content':"My first content",
  'date_posted':"April 20, 2023"
 },
 {
  'author':"Jessica Kadzo",
  'title':"I am God's son",
  'content':"My second content",
  'date_posted':"April 22, 2023"
 }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
 return render_template("about.html", title='About')

if __name__ == '__main__':
 app.run(debug=True)