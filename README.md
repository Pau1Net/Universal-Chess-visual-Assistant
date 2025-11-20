# Universal Chess Visual Assistant

A computer vision-powered chess assistant that provides real-time move recommendations through visual overlay. The system detects chess boards from any source (websites, apps, physical boards), recognizes piece positions using deep learning, and displays optimal moves by drawing arrows directly on the screen.

## ⚠️ Educational Purpose Disclaimer

This project is developed for **educational and research purposes only**. While the system can analyze chess positions, its primary purpose is to demonstrate computer vision and machine learning techniques. The techniques developed here are intended for application in other domains such as image recognition, game AI, and assistive technologies.

## 🎯 Core Features

The program provides **visual accompaniment** during chess games with the following capabilities:

- **Automatic Board Detection**: Searches for and detects chess boards from screen captures
- **Piece Recognition**: Uses TensorFlow neural network to identify all pieces and board position
- **Color Detection**: Automatically determines user's piece color (or allows manual selection)
- **Move Recommendations**: Calculates best moves using chess engine analysis
- **Visual Overlay**: Draws arrows showing recommended moves directly on the board
- **Universal Compatibility**: Works with any chess platform (websites, desktop apps, mobile apps)
- **Real-time Analysis**: Continuously monitors and updates recommendations throughout the game

## 🚀 Quick Start

### Prerequisites

- **Python 3.11 or 3.12** (TensorFlow does not support Python 3.13+ yet)
- macOS, Linux, or Windows
- Homebrew (for macOS users)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Universal-Chess-visual-Assistant.git
cd Universal-Chess-visual-Assistant
```

2. **Install Python 3.12** (if needed)
```bash
# macOS
brew install python@3.12

# Ubuntu/Debian
sudo apt install python3.12

# Windows - Download from python.org
```

3. **Create virtual environment and install dependencies**
```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. **Download or train the chess piece recognition model**
   - Place `model.pb` in the project root or `model/` directory
   - Model must be a TensorFlow frozen graph trained to recognize chess pieces

## 📋 Implementation Roadmap

To make this project fully functional, the following components need to be implemented:

### ✅ Completed Components

- [x] TensorFlow model integration for piece classification
- [x] Basic move validation logic for all piece types
- [x] Pyglet window and rendering framework
- [x] FEN notation generation from board state
- [x] Virtual environment setup with all dependencies

### 🔨 Required Implementations

#### 1. **Board Detection Module** (High Priority)
- [ ] Implement `find_grayscale_tiles(img)` function in `dchessboard.py`
  - Screen capture functionality
  - Chessboard edge detection using computer vision
  - Perspective transformation to normalize board view
  - Grid extraction to isolate 64 squares
  - Tile preprocessing for model input

#### 2. **FEN Processing Utilities** (High Priority)
- [ ] Implement `get_castling_status(fen)` - Detect castling rights from position
- [ ] Implement `unflip_fen(fen)` - Convert black perspective to white perspective
- [ ] Implement `shorten_fen(fen)` - Compress consecutive empty squares (e.g., "11111111" → "8")

#### 3. **Chess Engine Integration** (High Priority)
- [ ] Install and integrate Stockfish chess engine
- [ ] Replace placeholder logic in `best_move.py` with Stockfish API calls
- [ ] Implement UCI protocol communication
- [ ] Add configurable engine depth/time settings
- [ ] Parse and convert engine output to board coordinates

#### 4. **Visual Overlay System** (Medium Priority)
- [ ] Implement `draw_arrow()` function in `visual.py`
  - Arrow rendering with start/end coordinates
  - Color coding (green for best move, yellow for alternatives)
  - Opacity and styling controls
  - Multi-move preview option
- [ ] Add screen overlay mode (transparent window over chess board)
- [ ] Implement coordinate transformation (board → screen coordinates)

#### 5. **Screen Capture & Real-time Processing** (Medium Priority)
- [ ] Continuous screen monitoring loop
- [ ] Configurable capture region selection
- [ ] Change detection to trigger analysis only when board updates
- [ ] Performance optimization for real-time operation

#### 6. **User Interface** (Medium Priority)
- [ ] Hotkey system for activation/deactivation
- [ ] Settings panel for configuration:
  - Board region selection
  - Piece color selection (auto/manual)
  - Engine strength settings
  - Overlay appearance options
- [ ] Status indicators (analyzing, ready, error)

#### 7. **Model Training/Distribution** (Low Priority)
- [ ] Document model training process
- [ ] Provide pre-trained `model.pb` file
- [ ] Create dataset generation tools
- [ ] Add model accuracy testing suite

## 📁 Project Structure

```
Universal-Chess-visual-Assistant/
├── visual.py              # Visual overlay system (Pyglet rendering)
├── dchessboard.py         # Board detection & piece recognition (TensorFlow)
├── best_move.py           # Move calculation (will integrate Stockfish)
├── requirements.txt       # Python dependencies
├── .gitignore            # Git exclusions
└── venv/                 # Virtual environment (not in git)
```

## 🔧 Development Commands

**Activate virtual environment:**
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Run visual overlay (basic test):**
```bash
python visual.py
```

**Test board recognition (requires model.pb):**
```bash
python dchessboard.py
```

**Deactivate virtual environment:**
```bash
deactivate
```

## 🧪 Testing

Currently, the project includes:
- `visual.py` - Displays test image (`igcboard.jpg` required)
- `dchessboard.py` - Board recognition (needs helper functions)
- `best_move.py` - Basic move validation (needs Stockfish integration)

## 🛠️ Technical Stack

- **Computer Vision**: OpenCV (to be integrated for board detection)
- **Deep Learning**: TensorFlow 2.x with frozen graph model
- **Chess Engine**: Stockfish (to be integrated)
- **Graphics**: Pyglet for rendering overlays
- **Numerical Computing**: NumPy for array operations

## 📝 Current Status

**Original Development Timeline:**
- Start date: January 8, 2023
- Completion announced: January 18, 2023
- Source code distribution halted: February 5, 2023

**This Repository:**
This is a snapshot of the core components with the implementation framework in place. The codebase requires the items in the roadmap above to become fully functional.

## 🤝 Contributing

Contributions are welcome! Areas where help is needed:
1. Implementing the missing helper functions (board detection)
2. Stockfish integration
3. Screen capture and overlay system
4. Model training and distribution
5. Cross-platform testing

## 📄 License

See LICENSE file for details.

## 🔗 Resources

- [Stockfish Chess Engine](https://stockfishchess.org/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Pyglet Documentation](https://pyglet.readthedocs.io/)
- [Python Chess Library](https://python-chess.readthedocs.io/)


