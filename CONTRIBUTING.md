# Contributing to Steam Speed Scanner

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (Windows version, Python version, etc.)

**Example:**
```markdown
**Bug:** Scanner crashes on startup
**OS:** Windows 11 23H2
**Python:** 3.12
**Steps:**
1. Run SteamSpeedScanner.exe
2. Wait for header to display
3. App crashes with error message

**Expected:** Scanner should start normally
**Actual:** Crash with "Connection error"
```

### Suggesting Features

Feature suggestions are welcome! Please provide:

- **Use case** - Why is this feature needed?
- **Proposed solution** - How should it work?
- **Alternatives considered** - Other approaches you've thought about

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## 📋 Code Style

- Use **type hints** for function parameters and return values
- Follow **PEP 8** style guidelines
- Keep functions **focused and small**
- Add **docstrings** for public functions
- Use **descriptive variable names**

## 🧪 Testing

Before submitting a PR:

- [ ] Test on Windows 10/11
- [ ] Test with Python 3.8+
- [ ] Verify EXE builds successfully
- [ ] Check that colors display correctly
- [ ] Ensure no sensitive data is logged

## 📝 Commit Messages

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
feat: add new speed test endpoint
fix: resolve DNS error handling
docs: update README with screenshots
style: format code according to PEP 8
refactor: improve progress display logic
perf: optimize concurrent requests
```

## 🎨 UI/UX Guidelines

When modifying the interface:

- Maintain **color consistency** (green=good, red=error, yellow=warning)
- Keep **animations smooth** (60fps where possible)
- Ensure **readability** on dark and light terminals
- Test with **different terminal sizes**

## 🔒 Security

- Never commit API keys or credentials
- Don't log sensitive user data
- Validate all user inputs
- Keep dependencies updated

## 📦 Dependencies

When adding new dependencies:

- Add to `requirements.txt`
- Document in README.md
- Ensure cross-platform compatibility
- Consider impact on EXE size

## 🚀 Release Process

1. Update version in code
2. Update CHANGELOG.md
3. Create release tag
4. Build EXE
5. Create GitHub release with attachments

## 💬 Questions?

- Check existing [discussions](https://github.com/steam-speed-scanner/discussions)
- Read the [README.md](README.md)
- Review [troubleshooting guide](README.md#troubleshooting)

---

**Thank you for contributing to Steam Speed Scanner! 🚀**
