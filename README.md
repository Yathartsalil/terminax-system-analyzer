# Terminal System Analyzer

Lightweight modular system monitoring toolkit for Linux power users and developers.

## Features
- Live CPU usage monitoring
- Memory and swap statistics
- Top CPU-consuming processes
- Clean modular architecture
- Built using `psutil` and `rich`

## Installation

```bash
git clone https://github.com/yourusername/terminal-system-analyzer.git
cd terminal-system-analyzer
pip install -r requirements.txt
python main.py
```

## Project Structure

```
terminal-system-analyzer/
│
├── analyzer/
│   ├── cpu.py
│   ├── memory.py
│   ├── disk.py
│   ├── network.py
│   ├── processes.py
│   └── dashboard.py
│
├── main.py
├── requirements.txt
└── README.md
```

## License
MIT
