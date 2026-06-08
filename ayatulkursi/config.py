"""
Configuration module for Ayatul Kursi player.
Handles settings validation and defaults.
"""

import os
from dataclasses import dataclass
from typing import Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class PlayerConfig:
    """Configuration class for audio player settings."""

    volume: float = 0.7
    duration_minutes: Optional[int] = None
    duration_hours: Optional[int] = None
    whisper_mode: bool = False
    audio_file: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        self._validate_volume()
        self._apply_whisper_mode()
        self._set_default_audio_file()

    def _validate_volume(self) -> None:
        """Validate volume is between 0.0 and 1.0."""
        if not 0.0 <= self.volume <= 1.0:
            raise ValueError(f"Volume must be between 0.0 and 1.0, got {self.volume}")

    def _apply_whisper_mode(self) -> None:
        """Apply whisper mode settings if enabled."""
        if self.whisper_mode:
            self.volume = 0.1

    def _set_default_audio_file(self) -> None:
        """Set default audio file if not specified."""
        if self.audio_file is None:
            # Look for the audio file in the assets directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            package_dir = os.path.dirname(current_dir)
            audio_path = os.path.join(
                package_dir, "assets", "ayatul-kursi-saad-al-ghamdi.mp3"
            )

            # Also check in the original location
            if not os.path.exists(audio_path):
                audio_path = os.path.join(
                    package_dir, "audio", "ayatul-kursi-saad-al-ghamdi.mp3"
                )

            self.audio_file = audio_path

    def get_total_duration_seconds(self) -> Optional[float]:
        """
        Calculate total duration in seconds.

        Returns:
            Total duration in seconds or None if infinite.
        """
        total_seconds = 0

        if self.duration_hours is not None:
            total_seconds += self.duration_hours * 3600

        if self.duration_minutes is not None:
            total_seconds += self.duration_minutes * 60

        return total_seconds if total_seconds > 0 else None

    def get_mode_description(self) -> str:
        """
        Get a human-readable description of the current mode.

        Returns:
            Description string.
        """
        mode = "Whisper Mode" if self.whisper_mode else "Normal Mode"
        volume_pct = int(self.volume * 100)

        duration = self.get_total_duration_seconds()
        if duration is None:
            return f"{mode} - Volume: {volume_pct}% - Duration: Infinite"

        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)

        if hours > 0:
            return f"{mode} - Volume: {volume_pct}% - Duration: {hours}h {minutes}m"
        return f"{mode} - Volume: {volume_pct}% - Duration: {minutes}m"
