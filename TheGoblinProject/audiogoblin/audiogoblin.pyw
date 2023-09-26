import pygame
import tkinter as tk
from tkinter import filedialog

def main():
    pygame.init()

    # Initialize the display (not actually needed for an audio player)
    pygame.display.set_mode((200, 100))

    # Initialize the mixer
    pygame.mixer.init()

    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Open a file dialog to choose an audio file
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.aac")])

    if not file_path:
        exit(-1)

    sound = pygame.mixer.Sound(file_path)

    print(f"Playing {file_path}")
    channel = sound.play()

    # Wait for the audio to finish playing
    while channel.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick rate as needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                channel.stop()
                pygame.quit()
                return

    pygame.quit()

if __name__ == "__main__":
    main()

