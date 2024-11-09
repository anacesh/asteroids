# pyright: basic
import pygame
import os

from Assets.audioassets import AudioAssets
from Assets.fontassets import FontAssets
from Assets.textureassets import TextureAssets


class Assets:
    _instance = None

    @staticmethod
    def get_instance():
        if Assets._instance is None:
            Assets._instance = Assets()
        return Assets._instance

    def __init__(self):
        if Assets._instance is not None:
            raise Exception("bro it is singleton, use get_instance() method instead")
        self.audio = AudioAssets()
        self.textures = TextureAssets()
        self.fonts = FontAssets()





