# Installation Instructions for Ayatul Kursi

## Quick Start

### 1. Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### 2. Standard Installation

#### Option A: From Source (Recommended for Development)

```bash
# Navigate to the project directory
cd path/to/ayatulkursi

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .

# Verify installation
ayatulkursi --help
```

#### Option B: Direct Installation

```bash
# Navigate to the project directory
cd path/to/ayatulkursi

# Install with all dependencies
pip install .
```

#### Option C: Editable Install with Development Tools

```bash
# For developers who want to contribute
cd path/to/ayatulkursi

# Install with development dependencies
pip install -e ".[dev]"
```

### 3. Verify Installation

After installation, verify everything works:

```bash
# Should display help message
ayatulkursi --help

# Should play audio
ayatulkursi --minutes 1
```

### 4. Troubleshooting Installation

#### Issue: "pygame not found" or compilation errors on Linux

**Solution**: Install system dependencies first

```bash
# On Ubuntu/Debian
sudo apt-get install python3-dev libsdl2-dev libsdl2-image-dev \
  libsdl2-mixer-dev libsdl2-gfx-dev libsdl2-ttf-dev libfreetype6-dev

# Then install pygame
pip install pygame --no-binary pygame

# Or use pre-built wheels
pip install pygame
```

#### Issue: "pygame not found" on macOS

**Solution**:
```bash
# Using Homebrew
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf libfreetype

# Then install pygame
pip install pygame
```

#### Issue: Command "ayatulkursi" not found after installation

**Solution**: 

On **Linux/macOS**:
```bash
# Reinstall and check PATH
pip install --force-reinstall -e .

# Verify installation location
which ayatulkursi

# Add to PATH if needed
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # or ~/.zshrc
```

On **Windows**:
```bash
# Reinstall
pip install --force-reinstall -e .

# Run using Python module
python -m ayatulkursi.cli --help
```

#### Issue: Audio file not found

**Solution**: Ensure audio file is in the correct location

```bash
# Check if audio file exists
ls ayatulkursi/assets/
# Should show: ayatul-kursi-saad-al-ghamdi.mp3

# If missing, copy from your audio directory
cp /path/to/audio/file.mp3 ayatulkursi/assets/ayatul-kursi-saad-al-ghamdi.mp3
```

### 5. Virtual Environment Setup (Recommended)

For a clean, isolated environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install the package
pip install -r requirements.txt
pip install -e .

# Verify
ayatulkursi --help

# Deactivate when done
deactivate
```

### 6. Uninstallation

```bash
# Remove the package
pip uninstall ayatulkursi

# Remove dependencies (if not needed elsewhere)
pip uninstall pygame click
```

### 7. Updating

```bash
# If updating from a newer version
cd path/to/ayatulkursi

# Pull latest changes
git pull origin main

# Reinstall
pip install --force-reinstall -e .
```

### 8. System-wide Installation (Linux/macOS)

```bash
# Install for all users
sudo pip install .

# Or install in user space
pip install --user -e .
```

## Advanced Installation

### Using Poetry (Alternative)

If you prefer poetry over pip:

```bash
# Install dependencies
poetry install

# Run the CLI
poetry run ayatulkursi --help

# Or activate the virtual environment
poetry shell
ayatulkursi --help
```

### Using Conda (Alternative)

If you use Anaconda/Miniconda:

```bash
# Create environment
conda create -n ayatulkursi python=3.10

# Activate
conda activate ayatulkursi

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Verify
ayatulkursi --help
```

## Platform-Specific Notes

### Windows
- No additional system dependencies required
- Pygame will be automatically compiled if needed
- May need to install Visual C++ Build Tools for compilation

### Linux
- Requires SDL2 development libraries
- Follow the troubleshooting section above
- Different distributions may have different package names

### macOS
- Requires SDL2 libraries (install via Homebrew)
- If using Apple Silicon (M1/M2), ensure using native Python, not Rosetta

## After Installation

### First Run

```bash
# Simple test
ayatulkursi --minutes 1

# With debug information
ayatulkursi --debug --minutes 1

# Whisper mode test
ayatulkursi --whisper --minutes 2
```

### Getting Help

```bash
# View all options
ayatulkursi --help

# Run with debug logging
ayatulkursi --debug

# Report issues
# Visit: https://github.com/nawaz0x1/ayatulkursi/issues
```

## Environment Setup for Development

If you want to contribute to the project:

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black ayatulkursi/

# Check code style
flake8 ayatulkursi/
mypy ayatulkursi/

# Sort imports
isort ayatulkursi/
```

---

**Installation Complete!** You're ready to use Ayatul Kursi. Start with `ayatulkursi --help`.
