# 🚀 Steam Speed Scanner

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com)

**Find the fastest Steam download region for your connection!**

Steam Speed Scanner tests all Steam CDN (Content Delivery Network) regions worldwide and identifies which server provides the best download speed for your specific location and ISP.

![Steam Speed Scanner](https://via.placeholder.com/800x450/1a1a2e/16213e?text=Steam+Speed+Scanner+Screenshot)

---

## ✨ Features

- 🌍 **67 Regions** - Tests Steam CDN servers across all continents
- ⚡ **Real Speed Test** - Measures actual download speed (not just latency)
- 🎨 **Beautiful UI** - Professional terminal interface with colors and animations
- 🏆 **Smart Ranking** - Automatically ranks regions by speed and recommends the best
- 📊 **Detailed Results** - Shows top 10 fastest regions with speed and latency
- ⏱️ **Fast Scanning** - Concurrent testing with progress display
- 💾 **Standalone EXE** - No Python installation required

---

## 📋 Requirements

### To run from source:
- Python 3.8 or higher
- Required packages (install with `pip install -r requirements.txt`):
  - `aiohttp>=3.9.0`
  - `colorama>=0.4.6`

### To run the EXE:
- Windows 10/11
- No additional dependencies needed!

---

## 🚀 Quick Start

### Option 1: Download Pre-built EXE (Recommended)

1. Go to [Releases](https://github.com/YOUR_USERNAME/steam-speed-scanner/releases)
2. Download the latest `SteamSpeedScanner.exe`
3. Run file run_scanner.bat
4. Wait for the scan to complete
5. Press any key to exit

### Option 2: Run from Source

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/steam-speed-scanner.git
cd steam-speed-scanner

# Install dependencies
pip install -r requirements.txt

# Run the scanner
python steam_speed_scanner.py
```

### Option 3: Build EXE Yourself

```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --name "SteamSpeedScanner" steam_speed_scanner.py

# Find your EXE in the 'dist' folder
```

---

## 📖 How It Works

1. **Latency Test** - Scans all 67 Steam CDN regions to measure connection latency
2. **Speed Test** - Tests real download speed for the top 10 fastest regions
3. **Analysis** - Ranks all regions by actual download speed
4. **Recommendation** - Displays the best region for your connection

### Test Process:
```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: Latency Scan (all 67 regions)    ~1-2 minutes    │
│  Phase 2: Speed Test (top 10 regions)      ~30 seconds     │
│  Phase 3: Results & Recommendation         Instant         │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 How to Use Results

After the scan completes, you'll see a recommendation like:

```
🏆 RECOMMENDED: Netherlands - Amsterdam ⚡ Measured
   Speed: 45.23 Mbps | Latency: 68.9 ms
```

**To apply this in Steam:**

1. Open **Steam** → **Settings** → **Downloads**
2. Find **"Download Region"** dropdown
3. Select the recommended region (e.g., "Netherlands")
4. **Restart Steam** for changes to take effect

---

## 🖼️ Screenshots

### Main Interface
```
╔════════════════════════════════════════════════════════════════╗
║                    🚀 STEAM SPEED SCANNER                      ║
║         Find the fastest download region for your connection   ║
╚════════════════════════════════════════════════════════════════╝

  🌍 Scanning 67 regions...
  ⚡ Testing latency and download speed

  ⠋  [✓21/✗46]  ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░  31.3%  45.2s
```

### Results Display
```
╔════════════════════════════════════════════════════════════════╗
║           📊 STEAM DOWNLOAD REGION SPEED TEST RESULTS          ║
╚════════════════════════════════════════════════════════════════╝

  📈 SUMMARY:
  ┌──────────────────────────────────────────────────────────────┐
  │  Total Regions:  67  |  ✓ Success:  21  |  ✗ Failed:  46    │
  └──────────────────────────────────────────────────────────────┘

  🏆 TOP 10 FASTEST REGIONS:
  ┌──────────────────────────────────────────────────────────────┐
  │ Rank  Region                          Speed (Mbps)  Latency  │
  ├──────────────────────────────────────────────────────────────┤
  │ 🥇 1  Netherlands - Amsterdam            45.23     68.9ms   ✓ │
  │ 🥈 2  Germany - Frankfurt                42.15     72.3ms   ✓ │
  │ 🥉 3  UK - London                        38.67     76.1ms   ✓ │
  └──────────────────────────────────────────────────────────────┘
```

---

## 🌍 Supported Regions

### Europe (22)
Amsterdam, Frankfurt, London, Paris, Stockholm, Warsaw, Madrid, Milan, Moscow, Istanbul, Athens, Vienna, Zurich, Prague, Copenhagen, Helsinki, Oslo, Lisbon, Bucharest, Kiev, Budapest, Sofia

### North America (8)
Seattle, Los Angeles, Chicago, New York, Miami, Dallas, Montreal, Vancouver

### Asia (19)
Tokyo, Osaka, Seoul, Shanghai, Beijing, Taipei, Hong Kong, Singapore, Bangkok, Hanoi, Jakarta, Manila, Kuala Lumpur, Mumbai, Delhi, Almaty, Dubai, Tel Aviv, Riyadh

### Oceania (4)
Sydney, Melbourne, Perth, Auckland

### South America (7)
Sao Paulo, Rio de Janeiro, Porto Alegre, Buenos Aires, Santiago, Bogota, Lima

### Africa (2)
Johannesburg, Cape Town

---

## ⚙️ Advanced Usage

### Command Line Options

```bash
# Run with Python
python steam_speed_scanner.py

# Adjust concurrent connections (faster but less accurate)
# Edit the source: scanner.scan_all_endpoints(concurrent=10)
```

### Configuration

You can modify these values in `steam_speed_scanner.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `timeout_seconds` | 15 | Timeout for each region test |
| `concurrent` | 5 | Number of parallel tests |
| `SPEED_TEST_URLS` | Cloudflare | URLs for speed testing |

---

## 🔧 Troubleshooting

### Common Issues

**Problem:** All regions show as "Failed"
- **Solution:** Check your internet connection and firewall settings

**Problem:** Colors don't display correctly
- **Solution:** Use Windows Terminal or enable ANSI support in your console

**Problem:** EXE closes immediately
- **Solution:** Run `SteamSpeedScanner.bat` instead of the EXE directly

**Problem:** Slow scan time
- **Solution:** Reduce the number of regions in the source code

### Error Codes

| Error | Meaning | Solution |
|-------|---------|----------|
| `ClientConnectorDNSError` | DNS resolution failed | Check DNS settings |
| `Timeout` | Connection timed out | Increase timeout value |
| `HTTP 403` | Access forbidden | Normal, using latency estimate |

---

## 📊 Performance Benchmarks

| Test | Time |
|------|------|
| Full scan (67 regions) | ~2-3 minutes |
| Top 10 speed test | ~30-60 seconds |
| Total execution | ~3-4 minutes |

---

## 🛡️ Security & Privacy

- ✅ **No data collection** - All tests are local
- ✅ **No external API calls** - Except Steam CDN and Cloudflare speed test
- ✅ **Open source** - Code is fully transparent
- ✅ **No account required** - Works without Steam login

**Network Usage:**
- Downloads ~1-2 MB per speed test
- Total data usage: ~10-15 MB for full scan

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/steam-speed-scanner.git

# Install dev dependencies
pip install -r requirements.txt
pip install pyinstaller  # For building EXE

# Make your changes and test
python steam_speed_scanner.py

# Build and test EXE
pyinstaller --onefile --name "SteamSpeedScanner" steam_speed_scanner.py
```

---

## 🙏 Acknowledgments

- [Valve Corporation](https://www.valvesoftware.com/) - Steam platform
- [Cloudflare](https://www.cloudflare.com/) - Speed test infrastructure
- [Colorama](https://pypi.org/project/colorama/) - Cross-platform colors
- [AIOHTTP](https://docs.aiohttp.org/) - Async HTTP client

---

## 📬 Contact

- **Project Link:** https://github.com/YOUR_USERNAME/steam-speed-scanner
- **Issues:** https://github.com/YOUR_USERNAME/steam-speed-scanner/issues

---

## ⭐ Show Your Support

If this project helped you find a faster Steam region, please give it a star!

```bash
# Quick star from command line (if you have GitHub CLI)
gh repo star YOUR_USERNAME/steam-speed-scanner
```

---

<div align="center">

**Made with ❤️ for the Steam community**

[Report Bug](https://github.com/YOUR_USERNAME/steam-speed-scanner/issues) · [Request Feature](https://github.com/YOUR_USERNAME/steam-speed-scanner/issues) · [Discussions](https://github.com/YOUR_USERNAME/steam-speed-scanner/discussions)

</div>
