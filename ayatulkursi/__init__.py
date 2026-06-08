"""
Ayatul Kursi - Background Audio Player CLI
A production-ready Python CLI application for playing Ayatul Kursi audio
continuously in the background with various playback modes.
"""

__version__ = "1.0.1"
__author__ = "nawaz0x1"
__description__ = "Production-ready Ayatul Kursi background audio player CLI"

from .player import AyatulKursiPlayer
from .config import PlayerConfig

__all__ = ["AyatulKursiPlayer", "PlayerConfig", "__version__"]
