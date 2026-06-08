"""
Audio player module for Ayatul Kursi.
Handles playback in background using threading.
"""

import threading
import time
import logging
import os
from typing import Optional
from pathlib import Path

try:
    import pygame
except ImportError:
    pygame = None

logger = logging.getLogger(__name__)


class AyatulKursiPlayer:
    """
    Background audio player for Ayatul Kursi.

    Uses pygame.mixer for audio playback and threading for background execution.
    Handles seamless looping and graceful shutdown.
    """

    def __init__(self, audio_file: str, volume: float = 0.7) -> None:
        """
        Initialize the audio player.

        Args:
            audio_file: Path to the audio file to play.
            volume: Volume level (0.0-1.0).

        Raises:
            FileNotFoundError: If audio file doesn't exist.
            ImportError: If pygame is not installed.
        """
        if pygame is None:
            raise ImportError("pygame is required. Install it with: pip install pygame")

        if not os.path.exists(audio_file):
            raise FileNotFoundError(
                f"Audio file not found: {audio_file}\n"
                f"Full path: {os.path.abspath(audio_file)}"
            )

        self.audio_file = audio_file
        self.volume = volume
        self.is_playing = False
        self.is_paused = False
        self._playback_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()

        # Initialize pygame mixer
        self._init_mixer()

    def _init_mixer(self) -> None:
        """Initialize pygame mixer for audio playback."""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=44100, size=-16, channels=2)
                logger.debug("Pygame mixer initialized")
        except Exception as e:
            logger.error(f"Failed to initialize pygame mixer: {e}")
            raise

    def play(self, duration_seconds: Optional[float] = None) -> None:
        """
        Play audio in background thread.

        Args:
            duration_seconds: How long to play in seconds, or None for infinite.
        """
        if self.is_playing:
            logger.warning("Audio is already playing")
            return

        self._stop_event.clear()
        self._pause_event.clear()
        self.is_playing = True

        self._playback_thread = threading.Thread(
            target=self._playback_loop,
            args=(duration_seconds,),
            daemon=True,
        )
        self._playback_thread.start()
        logger.info("Playback started in background")

    def _playback_loop(self, duration_seconds: Optional[float]) -> None:
        """
        Main playback loop running in a separate thread.

        Args:
            duration_seconds: Total duration to play or None for infinite.
        """
        start_time = time.time()
        loop_count = 0

        try:
            while not self._stop_event.is_set():
                # Check if we've exceeded the duration
                if duration_seconds is not None:
                    elapsed = time.time() - start_time
                    if elapsed >= duration_seconds:
                        logger.info(f"Duration limit reached ({duration_seconds}s)")
                        break

                # Handle pause
                while self._pause_event.is_set() and not self._stop_event.is_set():
                    time.sleep(0.1)

                # Load and play the audio
                try:
                    pygame.mixer.music.load(self.audio_file)
                    pygame.mixer.music.set_volume(self.volume)
                    pygame.mixer.music.play()
                    loop_count += 1

                    # Calculate remaining time for this playback session
                    if duration_seconds is not None:
                        elapsed = time.time() - start_time
                        remaining = duration_seconds - elapsed
                        logger.debug(f"Loop {loop_count}: {remaining:.1f}s remaining")
                    else:
                        logger.debug(f"Loop {loop_count} started")

                    # Wait for music to finish or stop event
                    while (
                        pygame.mixer.music.get_busy() and not self._stop_event.is_set()
                    ):
                        time.sleep(0.1)

                        # Check if duration exceeded during playback
                        if duration_seconds is not None:
                            elapsed = time.time() - start_time
                            if elapsed >= duration_seconds:
                                pygame.mixer.music.stop()
                                break

                except Exception as e:
                    logger.error(f"Error during playback: {e}")
                    break

                # Small delay between loops for smooth transition
                time.sleep(0.1)

        except Exception as e:
            logger.error(f"Fatal error in playback loop: {e}")
        finally:
            self.is_playing = False
            pygame.mixer.music.stop()
            logger.info(f"Playback stopped after {loop_count} loops")

    def pause(self) -> None:
        """Pause the current playback."""
        if not self.is_playing or self.is_paused:
            logger.warning("Cannot pause: not currently playing")
            return

        pygame.mixer.music.pause()
        self._pause_event.set()
        self.is_paused = True
        logger.info("Playback paused")

    def resume(self) -> None:
        """Resume paused playback."""
        if not self.is_playing or not self.is_paused:
            logger.warning("Cannot resume: not paused")
            return

        pygame.mixer.music.unpause()
        self._pause_event.clear()
        self.is_paused = False
        logger.info("Playback resumed")

    def stop(self) -> None:
        """Stop playback and clean up."""
        if not self.is_playing:
            logger.warning("Playback is not running")
            return

        self._stop_event.set()

        # Wait for thread to finish
        if self._playback_thread and self._playback_thread.is_alive():
            self._playback_thread.join(timeout=5)

        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        logger.info("Playback stopped")

    def set_volume(self, volume: float) -> None:
        """
        Set playback volume.

        Args:
            volume: Volume level (0.0-1.0).

        Raises:
            ValueError: If volume is out of range.
        """
        if not 0.0 <= volume <= 1.0:
            raise ValueError(f"Volume must be between 0.0 and 1.0, got {volume}")

        self.volume = volume
        pygame.mixer.music.set_volume(volume)
        logger.info(f"Volume set to {int(volume * 100)}%")

    def is_music_playing(self) -> bool:
        """
        Check if music is currently playing.

        Returns:
            True if music is playing, False otherwise.
        """
        return self.is_playing and not self.is_paused
