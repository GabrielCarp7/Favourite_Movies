# Movie Tracker

A web application built with Flask and SQLAlchemy that allows users to keep track of their favorite movies. The app uses an external movie API to fetch movie details, which are then displayed along with the user's review and rating.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [API Used](#api-used)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- User authentication
- Search for movies using an API
- Add movies to your favorites list
- Write a short review and rate each movie
- Display a card for each movie with details, user review, and rating

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (venv, virtualenv, etc.)
- Flask
- SQLAlchemy
- Requests (for API interaction)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GabrielCarp7/Favourite_Movies.git
    cd Favourite_Movies
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root and add your API key:
    ```plaintext
    API_KEY=your_api_key_here
    ```

5. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the application:**

    ```bash
    flask run
    ```

7. **Access the application:**

    Open your browser and go to `http://127.0.0.1:5000/`

## Usage

1. **Search for a movie:**

    Use the search bar to find a movie. The app will fetch data from the external movie API.

2. **Add a movie to your favorites:**

    Once you find a movie, add it to your favorites. You'll be prompted to write a short review and rate the movie.

3. **View your favorite movies:**

    Go to the "My Movies" page to see a list of all your favorite movies. Each movie will be displayed in a card with a short description, your review, and your rating.  

## Technologies

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (for development), PostgreSQL/MySQL (for production)

## API Used

- **[The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)**: Used to fetch movie details such as title, description, and poster image.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## Contact

Gabriel Carp - [LinkedIn](https://www.linkedin.com/in/gabriel-carp-3b704022b/)
