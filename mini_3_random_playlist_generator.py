# mini project 3: random playlist generator

import random
songs = ["Song A", "Song B", "Song C", "Song D"]
def generate_playlist():
    random.shuffle(songs) # shuffle songs
    print(f"Playlists: {songs}")
generate_playlist()

# Playlists: ['Song D', 'Song B', 'Song A', 'Song C']