import os
import pygame
import random


class AudioAssets():
    def __init__(self):
        self.directory = "./Assets/sounds/"
        self.sounds = self.__load_audio(self.directory)

    def __load_audio(self, directory):
        sounds = {}
        try:
            for file in os.listdir(directory):
                if file.endswith((".wav", ".mp3", ".ogg")):
                    sound_name = os.path.splitext(file)[0]
                    sounds[sound_name] = pygame.mixer.Sound(os.path.join("./Assets/sounds/", file))
        except:
            print(f"directory {directory} not found")

        return sounds

    def play(self, name):
        sound = self.sounds.get(name)
        if sound:
            sound.play()

    def play_shot_sound(self):
        shot_sound_name = random.choice(["shot1", "shot2"])
        sound = self.sounds.get(shot_sound_name)
        if sound:
            sound.play()