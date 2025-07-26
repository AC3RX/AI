import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import difflib

class MovieBot:
    def __init__(self):
        self.movies = [
            {'title': 'The Shawshank Redemption', 'genres': ['Drama'], 'director': 'Frank Darabont', 'actors': ['Tim Robbins', 'Morgan Freeman']},
            {'title': 'The Godfather', 'genres': ['Crime', 'Drama'], 'director': 'Francis Ford Coppola', 'actors': ['Marlon Brando', 'Al Pacino']},
            {'title': 'The Dark Knight', 'genres': ['Action', 'Crime', 'Drama'], 'director': 'Christopher Nolan', 'actors': ['Christian Bale', 'Heath Ledger']},
            {'title': 'Pulp Fiction', 'genres': ['Crime', 'Drama'], 'director': 'Quentin Tarantino', 'actors': ['John Travolta', 'Uma Thurman']},
            {'title': 'Fight Club', 'genres': ['Drama'], 'director': 'David Fincher', 'actors': ['Brad Pitt', 'Edward Norton']},
            {'title': 'Inception', 'genres': ['Action', 'Adventure', 'Sci-Fi'], 'director': 'Christopher Nolan', 'actors': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt']},
            {'title': 'The Matrix', 'genres': ['Action', 'Sci-Fi'], 'director': 'Lana Wachowski', 'actors': ['Keanu Reeves', 'Laurence Fishburne']},
            {'title': 'Goodfellas', 'genres': ['Crime', 'Drama'], 'director': 'Martin Scorsese', 'actors': ['Robert De Niro', 'Ray Liotta']},
            {'title': 'The Silence of the Lambs', 'genres': ['Crime', 'Thriller'], 'director': 'Jonathan Demme', 'actors': ['Jodie Foster', 'Anthony Hopkins']},
            {'title': 'Interstellar', 'genres': ['Adventure', 'Drama', 'Sci-Fi'], 'director': 'Christopher Nolan', 'actors': ['Matthew McConaughey', 'Anne Hathaway']}
        ]
        self.df = pd.DataFrame(self.movies)
        self.df['metadata'] = self.df.apply(lambda x: ' '.join(x['genres']) + ' ' + x['director'] + ' ' + ' '.join(x['actors']), axis=1)
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['metadata'])
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def _get_index(self, title):
        titles = self.df['title'].tolist()
        matches = difflib.get_close_matches(title, titles, n=1, cutoff=0.6)
        if not matches:
            return None
        return self.df[self.df['title'] == matches[0]].index[0]

    def recommend(self, query):
       
        idx = self._get_index(query)
        if idx is not None:
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:4]
            movie_indices = [i[0] for i in sim_scores]
            return self.df['title'].iloc[movie_indices].tolist()
        
        
        director_movies = self.df[self.df['director'].str.contains(query, case=False)]['title'].tolist()
        if director_movies:
            return director_movies
        
        
        genre_movies = self.df[self.df['genres'].apply(lambda x: query.lower() in [g.lower() for g in x])]['title'].tolist()
        if genre_movies:
            return genre_movies
        
        
        actor_movies = self.df[self.df['actors'].apply(lambda x: query.lower() in [a.lower() for a in x])]['title'].tolist()
        if actor_movies:
            return actor_movies
        
        return []

def main():
    bot = MovieBot()
    print("Smart Movie Recommendation Bot")
    print("Just type anything related to movies - title, director, genre, or actor")
    print("Type 'exit' to quit\n")
    
    while True:
        query = input("What would you like recommendations for? ").strip()
        
        if query.lower() == 'exit':
            break
            
        if not query:
            print("Please enter something...")
            continue
            
        recs = bot.recommend(query)
        
        if not recs:
            print(f"Sorry, I couldn't find anything matching '{query}'")
        else:
            print(f"\nRecommendations based on '{query}':")
            for i, movie in enumerate(recs, 1):
                print(f"{i}. {movie}")
            print()

if __name__ == '__main__':
    main()