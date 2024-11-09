import os
import pygame


class TextureAssets:
    def __init__(self):
        self.directory = "./Assets/textures/"
        self.images = self.__load_textures(self.directory)

    def __load_textures(self, directory):
        images = {}
        try:
            for file in os.listdir(directory):
                if file.endswith((".png", ".jpg", ".jpeg")):
                    image_name = os.path.splitext(file)[0]
                    images[image_name] = pygame.image.load(os.path.join("./Assets/textures/", file)).convert_alpha()
        except:
            print(f"directory {directory} not found")

        return images