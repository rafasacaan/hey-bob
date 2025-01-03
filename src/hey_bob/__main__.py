# src/help-me-bob/__main__.py
import argparse
from .services import get_random_lyrics, load_pickle

def main():
    parser = argparse.ArgumentParser(description='Get random song lyrics')
    parser.add_argument('--year', type=int, help='Specific year to get lyrics from (optional)', default=None)
    args = parser.parse_args()
    
    try:
        # Load the data first
        df = load_pickle()
        
        # Get random verse
        song_name, song_year, text = get_random_lyrics(df, year=args.year)
        
        # Print with formatting
        print(" ")
        print(text)
        print(" ")
        print(f"- '{song_name}', {song_year}, Bob Dylan")
        print(" ")
        return 0
    except FileNotFoundError:
        print("Error: Could not find the lyrics data file.")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == '__main__':
    exit(main())