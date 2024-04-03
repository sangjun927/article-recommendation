# Article Recommendation

## Project Overview
This article recommendation system was developed as part of the Data Acquisition (MSDS 692) course at the University of San Francisco. The primary objective of the project is to demonstrate the process of creating a simple article recommendation engine utilizing word vectors, specifically using Stanford's GloVe project trained on Wikipedia data. The system reads a database of word vectors and a corpus of text articles, organizing them into a structured format (list of lists) for subsequent processing and analysis.

By implementing word embeddings from the GloVe model, the project highlights the practical application of natural language processing techniques in building a recommendation system. The engine processes the articles, converts the textual content into numerical data using the GloVe word vectors, and then uses these representations to identify and recommend similar articles based on content similarity.

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
