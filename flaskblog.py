from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
  "author": "Hadria Tourne",
  "title": "Tough Ones, The (Häjyt)",
  "content": "fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat",
  "date_posted": "11.2.2018"
}, {
  "author": "Darrel Huxter",
  "title": "Love at Large",
  "content": "ultrices posuere cubilia curae duis faucibus accumsan odio curabitur convallis duis",
  "date_posted": "11.11.2017"
}, {
  "author": "Olivia MacLeod",
  "title": "When Willie Comes Marching Home",
  "content": "amet turpis elementum ligula vehicula consequat morbi a ipsum integer a nibh in quis justo",
  "date_posted": "14.10.2017"
}, {
  "author": "Kandy Gardener",
  "title": "Dry Cleaning (Nettoyage à sec)",
  "content": "quis libero nullam sit amet turpis elementum ligula vehicula consequat",
  "date_posted": "1.11.2017"
}, {
  "author": "Holly Owthwaite",
  "title": "Planes: Fire & Rescue",
  "content": "erat id mauris vulputate elementum nullam varius nulla facilisi cras non velit nec nisi vulputate nonummy",
  "date_posted": "2.5.2018"
}]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.jinja2', posts=posts)


@app.route("/about")
def about():
    return render_template('about.jinja2', title="about")
