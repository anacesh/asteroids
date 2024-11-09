import os
import pygame


class FontAssets:
    def __init__(self):
        self.directory = "./Assets/fonts/"
        self.fonts = self.__load_fonts(self.directory)

    def __load_fonts(self, directory):
        fonts = {}
        try:
            for file in os.listdir(directory):
                if file.endswith(".ttf"):
                    font_name = os.path.splitext(file)[0]
                    fonts[font_name] = pygame.font.Font(os.path.join("./Assets/fonts/", file), 24)
        except:
            print(f"directory {directory} not found")

        return fonts