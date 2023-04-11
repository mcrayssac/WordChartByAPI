import praw
from datetime import datetime, timedelta
import csv
from collections import Counter
import re


# Remplacez ces valeurs par celles de votre application Reddit
# client_id = "YOUR_CLIENT_ID"
# client_secret = "YOUR_CLIENT_SECRET"
# user_agent = "YOUR_USER_AGENT"
client_id = "5FlgOaJq14pY7wHkY8K5nQ"
client_secret = "cZLU0zJr9Kw52IxnRCf_7uXVv0Kt7A"
user_agent = "WordChartByAPI/0.0.1"

# Créez une instance de l'API Reddit avec vos identifiants
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

def search_reddit_posts(keyword, limit=10, sort_by="new"):
    # Recherchez les publications dans l'ensemble du site
    search_results = reddit.subreddit("all").search(keyword, limit=limit, sort=sort_by)

    word_counter = Counter()

    # Parcourez les résultats de la recherche
    for post in search_results:
        # Vérifiez si le mot-clé est présent dans le titre
        if keyword.lower() in post.title.lower():
            # Nettoyez et séparez les mots du titre
            words = re.findall(r'\w+', post.title.lower())

            # Enlevez les mots courts (longueur <= 3)
            words = [word for word in words if len(word) > 3]

            # Comptez les occurrences de chaque mot
            word_counter.update(words)

    # Triez les mots par nombre d'occurrences
    sorted_words = word_counter.most_common()

    # Sauvegardez les mots les plus fréquents dans un fichier CSV
    with open('word_counts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, count in sorted_words:
            writer.writerow({'word': word, 'count': count})

    print("Le classement des mots a été sauvegardé dans word_counts.csv.")

# Exemple d'utilisation
search_keyword = "Python"
search_reddit_posts(search_keyword, limit=100000, sort_by="new")
