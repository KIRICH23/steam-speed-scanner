# 🚀 Quick Start Guide

Get Steam Speed Scanner up and running in minutes!

---

## ⚡ Option 1: Download EXE (Fastest - No Installation)

**Perfect for:** Users who just want to run the scanner

### Steps:

1. **Download**
   - Go to [Releases](https://github.com/YOUR_USERNAME/steam-speed-scanner/releases)
   - Download `SteamSpeedScanner.exe` from the latest release

2. **Run**
   - Double-click `SteamSpeedScanner.bat` (recommended)
   - Or run `SteamSpeedScanner.exe` from Command Prompt

3. **Wait for results** (~3-4 minutes)

4. **Apply the recommended region in Steam**

**✅ Done!**

---

## 🐍 Option 2: Run from Source

**Perfect for:** Developers, Python users, customization

### Prerequisites:
- Python 3.8 or higher ([Download](https://www.python.org/downloads/))
- pip (comes with Python)

### Steps:

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/steam-speed-scanner.git
cd steam-speed-scanner

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scanner
python steam_speed_scanner.py
```

**✅ Done!**

---

## 🔨 Option 3: Build EXE Yourself

**Perfect for:** Advanced users, custom builds

### Steps:

```bash
# 1. Clone and install (see Option 2)
git clone https://github.com/YOUR_USERNAME/steam-speed-scanner.git
cd steam-speed-scanner
pip install -r requirements.txt

# 2. Install PyInstaller
pip install pyinstaller

# 3. Build the EXE
pyinstaller --onefile --name "SteamSpeedScanner" steam_speed_scanner.py

# 4. Find your EXE
# The executable will be in the 'dist' folder
```

**✅ Done!**

---

## 📋 What to Expect

### Scan Progress:

```
╔══════════════════════════════════════════════════════════════╗
║                    🚀 STEAM SPEED SCANNER                    ║
╚══════════════════════════════════════════════════════════════╝

  🌍 Scanning 67 regions...
  ⚡ Testing latency and download speed

  ⠋  [✓21/✗46]  ████████████░░░░░░░░░░░░  31.3%  45.2s

  🔥 Testing real download speed for top 10 regions...
  [1/10] Testing Netherlands - Amsterdam...
```

### Results:

```
🏆 TOP 10 FASTEST REGIONS:
┌────────────────────────────────────────────────────────┐
│ 🥇 1  Netherlands - Amsterdam    45.23 Mbps   68.9ms  │
│ 🥈 2  Germany - Frankfurt        42.15 Mbps   72.3ms  │
│ 🥉 3  UK - London                38.67 Mbps   76.1ms  │
└────────────────────────────────────────────────────────┘

🏆 RECOMMENDED: Netherlands - Amsterdam ⚡ Measured
   Speed: 45.23 Mbps | Latency: 68.9 ms
```

---

## 🎯 Apply Results in Steam

1. **Open Steam**
2. Go to **Steam** → **Settings** → **Downloads**
3. Find **"Download Region"** dropdown
4. **Select the recommended region**
5. **Restart Steam**

---

## ❓ Troubleshooting

### Problem: "Python is not recognized"
**Solution:** Install Python from [python.org](https://www.python.org/downloads/) and check "Add to PATH"

### Problem: "ModuleNotFoundError"
**Solution:** Run `pip install -r requirements.txt`

### Problem: "EXE closes immediately"
**Solution:** Use `SteamSpeedScanner.bat` instead of the EXE directly

### Problem: "All regions failed"
**Solution:** 
- Check internet connection
- Disable VPN/proxy temporarily
- Check firewall settings

### Problem: "Colors don't display"
**Solution:** Use Windows Terminal or enable ANSI in console

---

## 📞 Need Help?

- 📖 Read the [README.md](README.md)
- 🐛 Report issues on [GitHub Issues](https://github.com/YOUR_USERNAME/steam-speed-scanner/issues)
- 💬 Ask in [Discussions](https://github.com/YOUR_USERNAME/steam-speed-scanner/discussions)

---

**Happy gaming! 🎮**
