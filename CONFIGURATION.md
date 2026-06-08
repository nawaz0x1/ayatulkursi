# Configuration Guide - Ayatul Kursi CLI

This guide covers all configuration options and advanced setup.

## Table of Contents
1. [Command-Line Options](#command-line-options)
2. [Configuration Modes](#configuration-modes)
3. [Volume Settings](#volume-settings)
4. [Duration Settings](#duration-settings)
5. [Audio File Configuration](#audio-file-configuration)
6. [Environment Variables](#environment-variables)
7. [Advanced Usage](#advanced-usage)

---

## Command-Line Options

### `--minutes INTEGER`
**Description**: Duration in minutes  
**Type**: Integer  
**Range**: Positive integers  
**Default**: None (infinite if no hours specified)  
**Examples**:
```bash
ayatulkursi --minutes 30       # 30 minutes
ayatulkursi --minutes 1        # 1 minute
ayatulkursi --minutes 120      # 2 hours via minutes
```

### `--hours INTEGER`
**Description**: Duration in hours  
**Type**: Integer  
**Range**: Positive integers  
**Default**: None (infinite if no minutes specified)  
**Examples**:
```bash
ayatulkursi --hours 2          # 2 hours
ayatulkursi --hours 8          # 8 hours
```

### `--whisper`
**Description**: Enable whisper mode (low volume)  
**Type**: Flag (boolean)  
**Volume Override**: 10% (0.1)  
**Default**: Disabled  
**Examples**:
```bash
ayatulkursi --whisper                    # Infinite whisper
ayatulkursi --whisper --hours 8          # 8 hours whisper
```

### `--volume FLOAT`
**Description**: Set playback volume  
**Type**: Float  
**Range**: 0.0 to 1.0  
**Default**: 0.7  
**Note**: Ignored if `--whisper` is used  
**Examples**:
```bash
ayatulkursi --volume 0.0       # Silent (not recommended)
ayatulkursi --volume 0.3       # Quiet (30%)
ayatulkursi --volume 0.5       # Medium (50%)
ayatulkursi --volume 0.7       # Normal (70%, default)
ayatulkursi --volume 0.9       # Loud (90%)
ayatulkursi --volume 1.0       # Maximum (100%)
```

### `--audio-file PATH`
**Description**: Custom audio file path  
**Type**: File path  
**Default**: `ayatulkursi/assets/ayatul-kursi-saad-al-ghamdi.mp3`  
**Format**: MP3 or WAV  
**Examples**:
```bash
ayatulkursi --audio-file /path/to/custom.mp3
ayatulkursi --audio-file ~/Downloads/quran.mp3
```

### `--debug`
**Description**: Enable debug logging  
**Type**: Flag (boolean)  
**Default**: Disabled (INFO level)  
**Examples**:
```bash
ayatulkursi --debug            # Show detailed logs
ayatulkursi --debug --minutes 5
```

### `--help`
**Description**: Display help message  
**Type**: Flag (boolean)  
**Examples**:
```bash
ayatulkursi --help
```

---

## Configuration Modes

### Mode 1: Infinite Playback (Default)
Plays continuously until manually stopped.

```bash
ayatulkursi
# or
ayatulkursi --volume 0.7
```

**Use Cases**:
- Continuous spiritual background
- All-day listening
- Background recitation

---

### Mode 2: Timed Playback
Plays for a specified duration and stops automatically.

```bash
# Minutes
ayatulkursi --minutes 30

# Hours
ayatulkursi --hours 2

# Combined
ayatulkursi --hours 1 --minutes 30
```

**Use Cases**:
- Meditation sessions
- Work/study blocks
- Morning routines
- Sleep preparation

---

### Mode 3: Whisper Mode
Low-volume (10%) continuous playback.

```bash
# Infinite whisper
ayatulkursi --whisper

# Timed whisper
ayatulkursi --whisper --hours 8
```

**Use Cases**:
- Background during work
- Non-intrusive listening
- Office/shared spaces
- Extended listening sessions

---

### Mode 4: Custom Configuration
Any combination of options.

```bash
# Custom volume + duration
ayatulkursi --volume 0.4 --hours 2

# Whisper + duration
ayatulkursi --whisper --hours 4

# Custom file + volume + duration
ayatulkursi --audio-file custom.mp3 --volume 0.5 --minutes 45
```

---

## Volume Settings

### Volume Reference

| Level | Percentage | Typical Use Case |
|-------|-----------|------------------|
| 0.0 | 0% | Silent (for testing) |
| 0.1 | 10% | Whisper mode - very quiet background |
| 0.2 | 20% | Very quiet - minimal distraction |
| 0.3 | 30% | Quiet - background listening |
| 0.4 | 40% | Low - comfortable background |
| 0.5 | 50% | Medium-low - clear but not loud |
| 0.6 | 60% | Medium - balanced |
| 0.7 | 70% | **DEFAULT** - standard listening |
| 0.8 | 80% | Medium-high - focused listening |
| 0.9 | 90% | High - clear and distinct |
| 1.0 | 100% | Maximum - full volume |

### Volume Examples

```bash
# For work/study (background)
ayatulkursi --volume 0.2 --hours 8

# For meditation
ayatulkursi --volume 0.5 --hours 1

# For focused listening
ayatulkursi --volume 0.8 --hours 0.5

# For sleep/relaxation
ayatulkursi --whisper --hours 2  # 10% volume
```

---

## Duration Settings

### Duration Calculation

**Minutes Only**:
```bash
ayatulkursi --minutes 45      # 45 minutes
```

**Hours Only**:
```bash
ayatulkursi --hours 2         # 2 hours (120 minutes)
```

**Combined** (adds together):
```bash
ayatulkursi --hours 1 --minutes 30   # 1.5 hours (90 minutes)
ayatulkursi --hours 2 --minutes 45   # 2.75 hours (165 minutes)
```

### Duration Examples by Activity

```bash
# Quick session (15 min)
ayatulkursi --minutes 15

# Morning routine (30 min)
ayatulkursi --minutes 30

# Work session (2 hours)
ayatulkursi --hours 2

# Extended work (4 hours)
ayatulkursi --hours 4

# Study all-day with breaks (8 hours)
ayatulkursi --whisper --hours 8

# Before sleep (2 hours)
ayatulkursi --whisper --hours 2

# All-night (infinite)
ayatulkursi --whisper  # Infinite in whisper mode
```

---

## Audio File Configuration

### Using Default Audio
The default audio file is automatically located:
```bash
ayatulkursi
# Uses: ayatulkursi/assets/ayatul-kursi-saad-al-ghamdi.mp3
```

### Using Custom Audio File

#### Absolute Path (Full Path)
```bash
ayatulkursi --audio-file /path/to/audio.mp3
ayatulkursi --audio-file C:\Users\YourName\Music\quran.mp3
```

#### Relative Path (From current directory)
```bash
ayatulkursi --audio-file ./my-audio/ayat.mp3
```

#### User Home Directory
```bash
ayatulkursi --audio-file ~/Downloads/audio.mp3
```

### Supported Formats
- MP3 (.mp3)
- WAV (.wav)
- Other formats supported by pygame.mixer

### Audio File Requirements
- **Format**: MP3 or WAV
- **Bitrate**: 128 kbps or higher recommended
- **Duration**: Any length (looped automatically)
- **Size**: Typically 5-10 MB for 3-5 minute clips

### Setting Default Audio File

To change the default permanently, edit `ayatulkursi/config.py`:

```python
def _set_default_audio_file(self) -> None:
    """Set default audio file if not specified."""
    if self.audio_file is None:
        # Modify this path
        self.audio_file = "/your/custom/path/audio.mp3"
```

---

## Environment Variables

Currently, the application does not use environment variables, but you can create shell aliases:

### Bash/Zsh (.bashrc or .zshrc)
```bash
# 30-minute default session
alias kursi30='ayatulkursi --minutes 30'

# Whisper mode
alias kursi-whisper='ayatulkursi --whisper'

# 2-hour session
alias kursi2h='ayatulkursi --hours 2'

# Custom volume
alias kursi-quiet='ayatulkursi --volume 0.3'
```

### PowerShell ($profile)
```powershell
# 30-minute default session
function kursi30 { ayatulkursi --minutes 30 }

# Whisper mode
function kursi-whisper { ayatulkursi --whisper }

# 2-hour session
function kursi2h { ayatulkursi --hours 2 }
```

---

## Advanced Usage

### Scripting

#### Create a Daily Routine Script (Bash)

```bash
#!/bin/bash
# daily-kursi.sh - Daily Ayatul Kursi routine

echo "Starting daily Ayatul Kursi routine..."

# Morning routine (15 min)
echo "Morning session..."
ayatulkursi --minutes 15 --volume 0.7

sleep 300  # Wait 5 minutes

# Work session (8 hours whisper)
echo "Work session..."
ayatulkursi --whisper --hours 8
```

Run it:
```bash
chmod +x daily-kursi.sh
./daily-kursi.sh
```

#### Create a Schedule (Using cron)

Add to crontab (`crontab -e`):

```cron
# Start whisper mode at 8 AM for 8 hours
0 8 * * * /usr/local/bin/ayatulkursi --whisper --hours 8

# Start 30-min session at 6 PM
0 18 * * * /usr/local/bin/ayatulkursi --minutes 30 --volume 0.7

# Start before bed at 10 PM
0 22 * * * /usr/local/bin/ayatulkursi --whisper --hours 2
```

### Combining with System Tools

```bash
# Play in background and get process ID
ayatulkursi --hours 2 &
echo $!

# Run with time limit using timeout command
timeout 3600 ayatulkursi --whisper

# Run with redirection
ayatulkursi --hours 2 > playback.log 2>&1
```

### Performance Tuning

The application is optimized by default, but for systems with limited resources:

1. Use whisper mode (lighter processing)
2. Use lower volume (reduces CPU load slightly)
3. Run alone without other applications
4. Use debug mode sparingly (adds logging overhead)

---

## Configuration Examples

### Example 1: Office/Work Setup
```bash
# Background listening during 8-hour work day at low volume
ayatulkursi --whisper --hours 8
```

### Example 2: Daily Meditation
```bash
# Daily 30-minute session with focused volume
ayatulkursi --minutes 30 --volume 0.7
```

### Example 3: Sleep Preparation
```bash
# Quiet background 2 hours before sleep
ayatulkursi --whisper --hours 2 --volume 0.1
```

### Example 4: Study Session
```bash
# 4-hour study session with medium-low background
ayatulkursi --hours 4 --volume 0.4
```

### Example 5: Custom Audio
```bash
# Use different recitation at specific volume for 1 hour
ayatulkursi --audio-file ~/Downloads/custom-quran.mp3 --hours 1 --volume 0.6
```

---

## Troubleshooting Configuration

### Issue: Volume not changing
**Solution**: Ensure you're using `--volume` (not `--vol`) and value is 0.0-1.0

```bash
# Correct
ayatulkursi --volume 0.5

# Incorrect
ayatulkursi --vol 0.5      # Wrong option name
ayatulkursi --volume 2.0   # Out of range
```

### Issue: Duration not working
**Solution**: Use integer values, not decimals

```bash
# Correct
ayatulkursi --minutes 30
ayatulkursi --hours 2

# Incorrect
ayatulkursi --minutes 0.5  # Use 30 seconds instead
```

### Issue: Audio file not found
**Solution**: Provide absolute path or ensure file exists

```bash
# Check file exists
ls /path/to/audio.mp3

# Use absolute path
ayatulkursi --audio-file /absolute/path/to/audio.mp3
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Default Volume** | 70% (0.7) |
| **Whisper Volume** | 10% (0.1) |
| **Default Duration** | Infinite |
| **Max Volume** | 100% (1.0) |
| **Min Volume** | 0% (0.0) |
| **Default Audio** | ayatul-kursi-saad-al-ghamdi.mp3 |
| **Supported Formats** | MP3, WAV |

**Need help?** Run `ayatulkursi --help`
