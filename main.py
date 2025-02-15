import time
import sys
import os
import contextlib

# Suppress pygame output (including "Hello from the pygame community" message)
with open(os.devnull, 'w') as fnull:
    with contextlib.redirect_stdout(fnull):
        import pygame

def display_lyrics(lyrics, durations, initial_delay, typing_speed):
    for i, line in enumerate(lyrics):
        # Add delay before displaying the lyrics
        time.sleep(initial_delay)  # Delay before showing the lyrics

        # Display each word in the line
        for word in line.split():
            # Show each word with typing effect
            for letter in word:
                print(letter, end='', flush=True)  # Display letter without newline
                time.sleep(typing_speed)  # Delay based on typing speed per letter
            print(' ', end='', flush=True)  # Add space after each word
            time.sleep(0.2)  # Additional delay after each word
        print()  # Move to the next line after all words are shown
        time.sleep(durations[i])  # Delay based on the duration for each line

def main():
    # Initialize pygame
    pygame.mixer.init()
    
    # Path to the audio file
    audio_path = "asset/song.mp3"  # Replace with the path to your audio file

    # Check if the file exists
    if not os.path.isfile(audio_path):
        print("File not found:", audio_path)
        return

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error loading audio file:", e)
        return

    # Lyrics and duration (in seconds) for each line
    lyrics = [
        "Hold my hands, dont-dont tell your friends",
        "Cerita kemaren, ku ingat kermanen",
        "Manis mu kaya permen, I hope this never end",
        "Oh can you be my Gwen? and ill be the Spiderman",
        "Sakit dadaku, ku mulai merindu",
        "Ku bayangkan jika kamu tidur di samping ku",
        "Di malam yang semu",
        "Pejamkan mata ku",
        "Ku bayangkan tubuhmu jika di pelukanku"
    ]
    
    # Duration for each line of lyrics (adjust according to the song)
    durations = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]  # Replace with the appropriate durations

    # Initial delay before showing the lyrics (in seconds)
    initial_delay = 0.1  # Adjust for synchronization with the music

    # Typing speed (in seconds)
    typing_speed = 0.04  # Adjust the typing speed for better readability

    # Display lyrics
    display_lyrics(lyrics, durations, initial_delay, typing_speed)

    # Wait until the song finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    main()