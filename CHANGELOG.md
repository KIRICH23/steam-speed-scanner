# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Add export results to CSV/JSON
- Add custom region testing
- Add historical speed tracking
- Add system tray icon mode
- Add auto-apply recommended region

## [1.0.0] - 2026-03-16

### Added
- 🌍 Support for 67 Steam CDN regions worldwide
- ⚡ Real download speed testing using Cloudflare speed test
- 🎨 Professional UI with colors and animations
- 🏆 Automatic region ranking and recommendation
- 📊 Detailed results with top 10 fastest regions
- 📈 Summary statistics (total, success, failed)
- ⏱️ Progress display with spinner and progress bar
- 💾 Standalone Windows EXE (no Python required)
- 🎯 Batch file wrapper for reliable console pause
- 📝 Comprehensive documentation (README, CONTRIBUTING, LICENSE)
- 🔧 Colorama support for Windows console colors
- 📦 PyInstaller build configuration

### Technical
- Async/concurrent region testing (5 parallel by default)
- Two-phase testing: latency scan + speed test for top 10
- Fallback to latency-based estimates when direct speed test fails
- Robust error handling with detailed error messages
- Cross-platform color support

### Fixed
- Console window closing immediately after test
- ANSI color codes showing as text in Windows console
- Missing measure_real_speed method error

### Changed
- Updated from generic CDN endpoints to actual Steam cache server hostnames
- Improved speed measurement accuracy
- Enhanced UI/UX with boxes, icons, and formatted output

---

## Version History

- **1.0.0** (2026-03-16) - Initial public release
  - Full region scanning
  - Real speed testing
  - Professional UI
  - Standalone EXE

---

## Release Notes

### Version 1.0.0 - Initial Release

The first stable release of Steam Speed Scanner includes:

**Core Features:**
- Scan all 67 Steam download regions
- Measure latency and download speed
- Automatic recommendation of best region
- Beautiful terminal interface

**Performance:**
- Full scan in ~3-4 minutes
- Concurrent testing for speed
- Minimal data usage (~10-15 MB)

**Compatibility:**
- Windows 10/11
- Python 3.8+ (for source)
- Standalone EXE available

**Known Issues:**
- Some regions may fail due to DNS resolution (normal)
- Colors may not display in very old terminals

---

## Upcoming Features

- [ ] CSV/JSON export
- [ ] Custom endpoint testing
- [ ] Speed history tracking
- [ ] Auto-apply recommended region
- [ ] Minimize to system tray
- [ ] Scheduled scanning
- [ ] Comparison mode (before/after)

---

**Full changelog available at:** https://github.com/YOUR_USERNAME/steam-speed-scanner/releases
