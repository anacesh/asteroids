# pyright: basic
import pygame
import os

class Assets():
    def __init__(self):
        self.audio = self.__load_audio()

    def __load_audio(self):
        files = {}
        for file in os.listdir("./Assets/sounds/"):
            if file.endswith(".wav") or file.endswith(".mp3") or file.endswith(".ogg"):
                sound_name = os.path.splitext(file)[
                    0
                ]  # Получаем имя файла без расширения для ключа
                files[sound_name] = pygame.mixer.Sound(os.path.join("./Assets/sounds/", file))
        return files

    def play(self, name):
        self.audio.get(name, None).play()





