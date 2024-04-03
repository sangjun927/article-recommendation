from flask import Flask, render_template
import sys
import pickle
import os

app = Flask(__name__)

@app.route("/")
def articles():
    titles = []
    for article in articles:
        try:
            if len(article) >= 2:
                path = article[0]
                title = article[1]
                path_parts = path.split('/')
                if len(path_parts) >= 2:
                    filename = path_parts[-1]
                    topic = path_parts[-2]
                    titles.append((title, filename, topic))
        except Exception as e:
            print(f"Error processing article {article}: {e}", file=sys.stderr)

    return render_template('articles.html', titles=titles)


@app.route("/article/<topic>/<filename>")
def article(topic, filename):
    full_path = f'/Users/sangjun/data/bbc/{topic}/{filename}'
    
    article_data = next((article for article in articles if article[0] == full_path), None)
    
    if article_data is None:
        return "Article not found", 404
    
    title = article_data[1]
    
    print("Recommended dictionary contents:", recommended)  # Debugging statement 1
    print("Full path:", full_path)  # Debugging statement 2
    
    try:
        recommended_articles = recommended.get((full_path, title), [])
    except KeyError:
        recommended_articles = []

    print(f"Recommended articles for {full_path}: {recommended_articles}")  # Debugging statement

    if not recommended_articles:
        print("No recommended articles found.")

    return render_template('article.html', title=title, article=article_data, recommended_articles=recommended_articles)

f = open('articles.pkl', 'rb')
articles = pickle.load(f)
f.close()

f = open('recommended.pkl', 'rb')
recommended = pickle.load(f)
f.close()

if __name__ == '__main__':
    app.run(debug=True)
