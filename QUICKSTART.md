# 🚀 Quick Start Guide - Ayatul Kursi CLI

Get up and running in just 3 minutes!

## Installation (3 steps)

### Step 1: Clone or Download
```bash
cd /path/to/ayatulkursi
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Package
```bash
pip install -e .
```

## ✅ Verify Installation

```bash
ayatulkursi --help
```

You should see the help message with all available options.

---

## 🎵 Quick Examples

### Start Infinite Playback
```bash
ayatulkursi
```
Press **Ctrl+C** to stop.

### Play for 30 Minutes
```bash
ayatulkursi --minutes 30
```

### Play for 2 Hours
```bash
ayatulkursi --hours 2
```

### Whisper Mode (Low Volume - 10%)
```bash
ayatulkursi --whisper
```

### Custom Volume (50%)
```bash
ayatulkursi --volume 0.5
```

### Whisper Mode for 8 Hours
```bash
ayatulkursi --whisper --hours 8
```

---

## 🎯 Common Use Cases

**Morning Routine** (15 minutes):
```bash
ayatulkursi --minutes 15
```

**Work/Study** (All day, quiet mode):
```bash
ayatulkursi --whisper
```

**Before Bed** (2 hours, quiet):
```bash
ayatulkursi --whisper --hours 2
```

**Meditation** (1 hour, medium volume):
```bash
ayatulkursi --hours 1 --volume 0.5
```

---

## 📝 All Options

```
--minutes INTEGER    How long to play (in minutes)
--hours INTEGER      How long to play (in hours)
--whisper            Use whisper mode (10% volume)
--volume FLOAT       Set volume (0.0-1.0)
--audio-file PATH    Use custom audio file
--debug              Show detailed logs
--help               Show help message
```

---

## ❓ Troubleshooting

### "ayatulkursi: command not found"
Try reinstalling:
```bash
pip install --force-reinstall -e .
```

### "pygame not found"
Install dependencies:
```bash
pip install -r requirements.txt
```

### "Audio file not found"
Ensure the audio file exists in: `ayatulkursi/assets/ayatul-kursi-saad-al-ghamdi.mp3`

### Need more help?
Run with debug mode:
```bash
ayatulkursi --debug
```

---

## 📚 Learn More

- Full documentation: See [README.md](README.md)
- Installation details: See [INSTALL.md](INSTALL.md)
- Example outputs: See [EXAMPLES.md](EXAMPLES.md)

---

**You're all set!** Start with:
```bash
ayatulkursi
```

Enjoy! 🎵
