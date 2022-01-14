import os
import sys

class App(object):
    os.environ.setdefault('SETTINGS', 'game_files.settings')
    try:
        """IMPORT SETTINGS,RUN"""
        from game_files.settings import SETTINGS, RUN
        from game_files import manage, mapdata, textures
        RUN = RUN
        ALLOW_SETTINGS = SETTINGS
    except ImportError as exc:
        raise ImportError(
            'COULDNT IMPORT AND RUN GAME.'
        )

if __name__ == "__main__":
    app = App()