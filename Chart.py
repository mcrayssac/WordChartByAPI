import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import Import

def read_csv_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        word_freq = {}
        for row in reader:
            word_freq[row['word']] = int(row['count'])
    return word_freq

file_name = 'word_counts.csv'
word_freq = read_csv_file(file_name)

def create_wordcloud(word_freq):
    # Créez un nuage de mots
    wc = WordCloud(width=800, height=400, background_color='white', colormap='viridis')
    wc.generate_from_frequencies(word_freq)

    # Affichez le nuage de mots
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

create_wordcloud(word_freq)

