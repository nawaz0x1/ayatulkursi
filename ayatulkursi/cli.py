"""
Command-line interface for Ayatul Kursi player.
Provides user-friendly CLI with various playback options.
"""

import click
import logging
import signal
import sys
from typing import Optional

from .player import AyatulKursiPlayer
from .config import PlayerConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Global player instance for signal handling
_player: Optional[AyatulKursiPlayer] = None


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    global _player
    if _player:
        click.echo("\n")
        click.secho("⏹  Stopping playback...", fg="yellow")
        _player.stop()
        click.secho("✓ Ayatul Kursi player closed gracefully", fg="green")
        sys.exit(0)


@click.command()
@click.option(
    "--minutes",
    type=int,
    default=None,
    help="Play for specified number of minutes",
)
@click.option(
    "--hours",
    type=int,
    default=None,
    help="Play for specified number of hours",
)
@click.option(
    "--whisper",
    is_flag=True,
    default=False,
    help="Enable whisper mode (volume 10%)",
)
@click.option(
    "--volume",
    type=float,
    default=0.7,
    help="Set volume level (0.0-1.0), default is 0.7",
)
@click.option(
    "--audio-file",
    type=click.Path(exists=True),
    default=None,
    help="Path to audio file (optional, uses default if not provided)",
)
@click.option(
    "--debug",
    is_flag=True,
    default=False,
    help="Enable debug logging",
)
def main(
    minutes: Optional[int],
    hours: Optional[int],
    whisper: bool,
    volume: float,
    audio_file: Optional[str],
    debug: bool,
) -> None:
    """
    🎵 Ayatul Kursi - Background Audio Player

    Play Ayatul Kursi audio continuously in the background with various options.

    Examples:

    \b
    # Infinite playback
    ayatulkursi

    \b
    # Play for 30 minutes
    ayatulkursi --minutes 30

    \b
    # Play for 2 hours
    ayatulkursi --hours 2

    \b
    # Whisper mode (low volume)
    ayatulkursi --whisper

    \b
    # Custom volume
    ayatulkursi --volume 0.3

    \b
    # Whisper mode for 8 hours
    ayatulkursi --whisper --hours 8
    """
    global _player

    # Set up logging
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    # Display banner
    click.secho("\n" + "=" * 60, fg="cyan")
    click.secho("  🎵 Ayatul Kursi - Background Audio Player", fg="cyan", bold=True)
    click.secho("=" * 60 + "\n", fg="cyan")

    # Validate inputs
    if volume < 0.0 or volume > 1.0:
        click.secho(
            f"❌ Error: Volume must be between 0.0 and 1.0, got {volume}",
            fg="red",
        )
        sys.exit(1)

    if minutes is not None and minutes < 1:
        click.secho(
            f"❌ Error: Minutes must be positive, got {minutes}",
            fg="red",
        )
        sys.exit(1)

    if hours is not None and hours < 1:
        click.secho(f"❌ Error: Hours must be positive, got {hours}", fg="red")
        sys.exit(1)

    # Create configuration
    try:
        config = PlayerConfig(
            volume=volume if not whisper else 0.1,
            duration_minutes=minutes,
            duration_hours=hours,
            whisper_mode=whisper,
            audio_file=audio_file,
        )
    except ValueError as e:
        click.secho(f"❌ Configuration Error: {e}", fg="red")
        sys.exit(1)

    # Check if audio file exists
    if config.audio_file:
        import os

        if not os.path.exists(config.audio_file):
            click.secho(
                f"❌ Error: Audio file not found at {config.audio_file}",
                fg="red",
            )
            click.echo("\nPlease ensure the audio file is in the 'assets' directory")
            sys.exit(1)

    # Display configuration
    mode_desc = config.get_mode_description()
    click.secho(f"📋 Mode: {mode_desc}", fg="blue")

    if config.audio_file:
        click.secho(f"🎵 Audio: {config.audio_file}", fg="blue")

    click.secho(
        "\n💡 Press Ctrl+C to stop playback\n",
        fg="yellow",
    )

    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Create and start player
    try:
        _player = AyatulKursiPlayer(
            audio_file=config.audio_file,
            volume=config.volume if not whisper else 0.1,
        )

        # Start playback
        duration_seconds = config.get_total_duration_seconds()
        _player.play(duration_seconds=duration_seconds)

        # Display startup message
        if whisper:
            click.secho("🤫 Whisper mode activated - playing at low volume", fg="green")
        else:
            click.secho("✓ Playback started in background", fg="green")

        # Keep the main thread alive
        while _player.is_playing:
            import time

            time.sleep(1)

        # If we reach here, playback finished naturally
        click.echo("")
        click.secho("✓ Playback finished", fg="green")

    except FileNotFoundError as e:
        click.secho(f"❌ Error: {e}", fg="red")
        click.echo(
            "\nMake sure the audio file 'ayatul-kursi-saad-al-ghamdi.mp3' is in the assets/ directory"
        )
        sys.exit(1)
    except ImportError as e:
        click.secho(f"❌ Error: {e}", fg="red")
        click.echo("\nInstall required dependencies: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        click.secho(f"❌ Unexpected error: {e}", fg="red")
        if debug:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
