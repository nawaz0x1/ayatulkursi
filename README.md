# Ayatul Kursi Background Player CLI

A production-ready Python CLI application that continuously plays Ayatul Kursi audio in the background with various playback modes and options.

---

## Features

- **🎵 Infinite Loop Playback**: Play Ayatul Kursi continuously forever
- **⏱️ Timed Playback**: Specify duration in minutes or hours
- **🤫 Whisper Mode**: Low-volume mode (10%) for background recitation
- **🔊 Volume Control**: Customize volume from 0.0 to 1.0
- **🖥️ Background Playback**: Runs in the background without blocking the terminal
- **🔄 Smooth Transitions**: Seamless looping between audio repetitions
- **🛑 Graceful Shutdown**: Clean exit with Ctrl+C
- **🌍 Cross-Platform**: Works on Windows, Linux, and macOS
- **📝 Detailed Logging**: Optional debug logging for troubleshooting
- **🎨 User-Friendly Output**: Clear messages and status information

---

## 📋 Requirements

- Python 3.10 or higher
- pygame (for audio playback)
- click (for CLI interface)

---

## 🚀 Installation

### Method 1: Install from PyPI (Recommended - Coming Soon)

```bash
pip install ayatulkursi
```

### Method 2: Install from Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ayatulkursi.git
cd ayatulkursi
```

2. Install the package in development mode:
```bash
pip install -r requirements.txt
pip install -e .
```

3. Verify installation:
```bash
ayatulkursi --help
```

### Method 3: Local Setup

1. Navigate to the project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create symbolic link or alias for easy access:
```bash
# On Windows
python -m ayatulkursi.cli --help

# Or add to PATH and run directly
ayatulkursi --help
```

---

## 📖 Usage

### Basic Usage

#### Infinite Playback (Default)
Play Ayatul Kursi continuously forever:
```bash
ayatulkursi
```

**Output:**
```
============================================================
  🎵 Ayatul Kursi - Background Audio Player
============================================================

📋 Mode: Normal Mode - Volume: 70% - Duration: Infinite
🎵 Audio: /path/to/audio/ayatul-kursi-saad-al-ghamdi.mp3

💡 Press Ctrl+C to stop playback

✓ Playback started in background
```

---

#### Timed Playback

**Play for 30 minutes:**
```bash
ayatulkursi --minutes 30
```

**Play for 2 hours:**
```bash
ayatulkursi --hours 2
```

**Play for 1 hour and 30 minutes:**
```bash
ayatulkursi --hours 1 --minutes 30
```

**Output:**
```
============================================================
  🎵 Ayatul Kursi - Background Audio Player
============================================================

📋 Mode: Normal Mode - Volume: 70% - Duration: 30m
🎵 Audio: /path/to/audio/ayatul-kursi-saad-al-ghamdi.mp3

💡 Press Ctrl+C to stop playback

✓ Playback started in background
```

---

### Advanced Options

#### Whisper Mode
Low-volume mode perfect for continuous background recitation:

```bash
# Infinite whisper mode
ayatulkursi --whisper

# Whisper mode for 8 hours
ayatulkursi --whisper --hours 8

# Whisper mode for 2 hours
ayatulkursi --whisper --hours 2
```

**Output:**
```
============================================================
  🎵 Ayatul Kursi - Background Audio Player
============================================================

📋 Mode: Whisper Mode - Volume: 10% - Duration: 8h 0m
🎵 Audio: /path/to/audio/ayatul-kursi-saad-al-ghamdi.mp3

💡 Press Ctrl+C to stop playback

🤫 Whisper mode activated - playing at low volume
✓ Playback started in background
```

---

#### Custom Volume

Set volume between 0.0 (silent) and 1.0 (maximum):

```bash
# Very low volume (30%)
ayatulkursi --volume 0.3

# Medium volume (50%)
ayatulkursi --volume 0.5

# High volume (90%)
ayatulkursi --volume 0.9

# With duration
ayatulkursi --volume 0.4 --hours 2
```

**Output:**
```
============================================================
  🎵 Ayatul Kursi - Background Audio Player
============================================================

📋 Mode: Normal Mode - Volume: 30% - Duration: Infinite
🎵 Audio: /path/to/audio/ayatul-kursi-saad-al-ghamdi.mp3

💡 Press Ctrl+C to stop playback

✓ Playback started in background
```

---

#### Custom Audio File

Use a different audio file:
```bash
ayatulkursi --audio-file /path/to/custom/audio.mp3
```

---

#### Debug Mode

Enable detailed logging for troubleshooting:
```bash
ayatulkursi --debug
```

---

### Command-Line Options

```
Options:
  --minutes INTEGER           Play for specified number of minutes
  --hours INTEGER             Play for specified number of hours
  --whisper                   Enable whisper mode (volume 10%)
  --volume FLOAT              Set volume level (0.0-1.0), default is 0.7
  --audio-file TEXT           Path to audio file (uses default if not provided)
  --debug                     Enable debug logging
  --help                      Show this message and exit
```

---

## 🎯 Use Cases

### 1. Daily Recitation Routine
```bash
# Play for 15 minutes in the morning
ayatulkursi --minutes 15
```

### 2. All-Day Background Recitation
```bash
# Play continuously with whisper mode
ayatulkursi --whisper
```

### 3. Work/Study Sessions
```bash
# Play quietly during work
ayatulkursi --volume 0.3 --whisper --hours 8
```

### 4. Night-Time Listening
```bash
# Low volume for 6 hours before sleep
ayatulkursi --whisper --hours 6
```

### 5. Prayer Time Sessions
```bash
# Dedicated recitation for 1 hour
ayatulkursi --hours 1 --volume 0.8
```

---

## 🤫 Understanding Whisper Mode

Whisper Mode is a special feature designed for continuous, non-intrusive playback:

- **Volume**: Automatically set to 10% (very low)
- **Duration**: Can be infinite or limited (use `--hours` and `--minutes`)
- **Purpose**: Background recitation while working, studying, or relaxing
- **Example**: `ayatulkursi --whisper --hours 8`

### Why Use Whisper Mode?

- ✅ Minimizes distraction while maintaining presence
- ✅ Ideal for work/study environments
- ✅ Comfortable for extended listening
- ✅ Respectful volume for shared spaces

---

## 🔧 Troubleshooting

### Issue: "Audio file not found"
**Solution**: Ensure the audio file `ayatul-kursi-saad-al-ghamdi.mp3` is located in the `assets/` directory relative to the installation.

```bash
# Check audio file location
ls ayatulkursi/assets/
# Should show: ayatul-kursi-saad-al-ghamdi.mp3
```

### Issue: "pygame not found" or "ModuleNotFoundError"
**Solution**: Install required dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Audio cuts off or has crackling
**Solution**: 
- Try adjusting volume: `--volume 0.6`
- Check system audio settings
- Ensure no other applications are using audio
- Update pygame: `pip install --upgrade pygame`

### Issue: Command not found after installation
**Solution**: 
- Reinstall the package: `pip install -e .`
- Or run with Python module: `python -m ayatulkursi.cli`
- Ensure `~/.local/bin` is in your PATH (Linux/macOS)

### Issue: Graceful shutdown not working
**Solution**:
- Press Ctrl+C (may need to press twice)
- On Windows, you can also close the terminal window
- Check if debug mode provides more information: `--debug`

### Getting Help
Enable debug mode to see detailed logs:
```bash
ayatulkursi --debug
```

---

## 📦 Project Structure

```
ayatulkursi/
├── ayatulkursi/
│   ├── __init__.py           # Package initialization
│   ├── cli.py                # Command-line interface
│   ├── player.py             # Audio player logic
│   └── config.py             # Configuration management
├── assets/
│   └── ayatul-kursi-saad-al-ghamdi.mp3  # Audio file
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Project configuration
└── LICENSE                   # MIT License
```

---

## 🛠️ Development

### Setting up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ayatulkursi.git
cd ayatulkursi
```

2. Install in development mode with dev dependencies:
```bash
pip install -r requirements.txt
pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest
```

4. Run linting:
```bash
black ayatulkursi/
flake8 ayatulkursi/
mypy ayatulkursi/
isort ayatulkursi/
```

### Code Style
- Uses Black for code formatting
- PEP 8 compliant
- Type hints throughout
- Comprehensive docstrings

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [pygame](https://www.pygame.org/) for audio playback
- CLI powered by [click](https://click.palletsprojects.com/)
- Ayatul Kursi recitation by Saad Al-Ghamdi

---

## 📞 Support & Feedback

- 🐛 Report bugs: [GitHub Issues](https://github.com/nawaz0x1/ayatulkursi/issues)
- 💡 Suggest features: [GitHub Discussions](https://github.com/nawaz0x1/ayatulkursi/discussions)
- 📧 Contact: nawazhaider60@example.com

---

## 🎓 Learn More

### What is Ayatul Kursi?

Ayatul Kursi (Verse of the Throne) is the 255th verse of Surah Al-Baqarah (Chapter 2) in the Quran. It is considered one of the most powerful and important verses in Islam.

This application allows you to continuously listen to beautiful recitations of this verse in the background.

### Recommended Listening Times

- **Morning**: 10-15 minutes after Fajr prayer
- **Throughout the day**: Use whisper mode while working
- **Before sleep**: 1-2 hours in whisper mode
- **During stress**: 30+ minutes at any comfortable volume

---

**Made with ❤️ for spiritual wellness**
