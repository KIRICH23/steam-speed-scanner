# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of Steam Speed Scanner seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, create a new issue with the title "[SECURITY]" and describe the vulnerability in detail. Include:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the issue
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Time

We will acknowledge your report within **48 hours** and send a more detailed response within **5 business days** indicating the next steps in handling your report.

### Security Considerations

This application:
- ✅ Does **not** collect any user data
- ✅ Does **not** require authentication
- ✅ Does **not** store sensitive information
- ✅ Makes only outbound connections to Steam CDN and Cloudflare
- ✅ Does **not** modify Steam files or settings automatically

**Known Security Boundaries:**
- Network requests are made to Steam CDN servers (steamcontent.com)
- Speed tests use Cloudflare's public speed test endpoints
- No data is transmitted to third-party analytics or tracking services

## Security Best Practices

When using Steam Speed Scanner:

1. **Download from official sources only** - GitHub releases or this repository
2. **Verify file hashes** - Check SHA256 hash of downloaded EXE
3. **Run in a safe environment** - Especially when testing
4. **Monitor network traffic** - Use tools like Wireshark if concerned
5. **Keep updated** - Use the latest version for security patches

## Contact

For security concerns, please open an issue with the [SECURITY] label.

---

**Thank you for helping keep Steam Speed Scanner secure!**
