from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

API_KEY = API_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)


class EditForm(FlaskForm):
    new_rating = StringField("Your Rating:", validators=[DataRequired()])
    new_review = StringField("Your Review:", validators=[DataRequired()])
    done = SubmitField("Done")


class AddForm(FlaskForm):
    add_movie = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    movies = Movie.query.all()

    return render_template("index.html", all_movies=movies)


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = EditForm()

    if form.validate_on_submit():
        rating = form.new_rating.data
        review = form.new_review.data

        with app.app_context():
            element_to_update = db.get_or_404(Movie, id)
            element_to_update.rating = float(rating)
            element_to_update.review = review
            db.session.commit()

        return redirect("/")

    return render_template("edit.html", form=form)


@app.route('/delete/<int:id>')
def erase(id):
    with app.app_context():
        data = db.get_or_404(Movie, id)
        db.session.delete(data)
        db.session.commit()
    return redirect('/')


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        movie_name = form.add_movie.data
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9"
                             ".eyJhdWQiOiIxOTM5NDBlOWViMDFkYjI0YjljZWNlNzg1NjMyYmQwMSIsInN1YiI6IjY2"
                             "MTU3MTY2MTVhNGExMDE3ZGY4OWJhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ"
                             ".dAuFL1oq35UB4Jlpcv"
                             "7izNRp5UMSO7eFvBXJAhBiPnA"
        }
        response = requests.get(url, headers=headers).text
        movies_dict = json.loads(response)

        all_versions = []

        for movies in movies_dict["results"]:
            all_versions.append(f"{movies['title']}")

        return render_template("select.html", options=all_versions)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_title = request.args.get("title")

    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9"
                         ".eyJhdWQiOiIxOTM5NDBlOWViMDFkYjI0YjljZWNlNzg1NjMyYmQwMSIsInN1YiI6IjY2"
                         "MTU3MTY2MTVhNGExMDE3ZGY4OWJhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ"
                         ".dAuFL1oq35UB4Jlpcv"
                         "7izNRp5UMSO7eFvBXJAhBiPnA"
    }
    response = requests.get(url, headers=headers).text
    movies_dict = json.loads(response)

    for movies in movies_dict["results"]:

        if movies["title"] == movie_title:
            new_movie = Movie(
                title=movies["title"],
                year=movies["release_date"].split("-")[0],
                description=movies["overview"],
                img_url=f"https://image.tmdb.org/t/p/original/{movies["poster_path"]}",
                rating=1.1,
                ranking=0,
                review="None"
            )
            db.session.add(new_movie)
            db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
