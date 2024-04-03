# Article Recommendation

## Project Overview
This project, part of the Data Acquisition course (MSDS 692) at the University of San Francisco, creates a simple article recommendation engine. It uses word vectors from the GloVe project, trained on Wikipedia, to analyze and recommend similar articles. The process involves loading word vectors and a collection of text articles into a structured format for analysis. The aim is to learn how to build a recommendation system using these word embeddings.

## Installation
1. Clone the repository:

`git clone <repository-url>`

2. Navigate to the project directory:

`cd article-recommendation`

3. Set up a virtual environment:

`python -m venv env-ar`

`source env-ar/bin/activate` # Unix-based systems

`env-ar\Scripts\activate` # Windows

5. Install the required dependencies:

`pip install -r requirements.txt`

## Usage
1. To start the Flask server, run:

`FLASK_APP=server.py flask run`

2. Access the web interface at `http://localhost:5000/` to interact with the article recommendation system.
## Data File
The data files `articles.pkl`, 'recommended.pkl', and 'bbc data' required for this project is hosted on Google Drive. You can download it using the following link:
[Download Data](https://drive.google.com/drive/folders/1P28c0FOZz4PSHPSJ7JqwLCVBD7Jw2mmU?usp=sharing)

## File Structure
- `doc2vec.py`: Script for processing articles and generating embeddings.
- `server.py`: Flask server script to serve the web interface.
- `templates/`: HTML templates for the web interface.
- `requirements.txt`: Lists all the dependencies required to run the project.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
