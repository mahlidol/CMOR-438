import os
import sys

# Add src/ to Python path so lanastance can be imported
sys.path.append(os.path.abspath("src"))

from lanastance.preprocessing import extract_song_features
