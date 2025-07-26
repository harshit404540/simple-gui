# 🕸️ Tor-Powered Custom Web Browser (PyQt6)

This is a lightweight custom web browser built with **PyQt6** and integrated with **Tor** for anonymous browsing. It includes basic navigation buttons, URL input, and a proxy toggle that starts/stops a Tor instance locally.

> **Note**: This is a minimal educational browser prototype, not a full-featured secure browsing solution.
> **Note**: Assisted by ChatGPT for coding help and design decisions.

---

## 🚀 Features

- 🧭 Basic browser navigation (Back, Forward, Refresh, Home)
- 🌐 URL search bar
- 🛡️ Tor proxy integration (SOCKS5 on port 9050) --[ Downloaded from https://www.torproject.org ]--
- ✅ Tor toggle with visual status (yellow = starting/stopping, green = activated original = deactivated)
- 🌈 Icon support for UI buttons
- 🎨 Embedded welcome page with HTML + CSS styling

## 🧅 TOR (Steps to start/stop...)

- step-1: Tap on tor button.
- step-2: Wait till button color turn green from yellow or till you see something like Bootstrapped 100% in your terminal.
- step-3: To stop tor:
        - Click again on tor button.
        - Wait till color backs to its original.

---

## 🧪 Preview

<img width="1095" height="601" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/bf50718f-e635-4c7c-91aa-d5ef0dd75b91" />

<img width="1366" height="768" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/b8067570-f493-4d48-9ffa-b09bbe3687f8" />

<img width="1099" height="566" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/0a5e2770-437c-4d30-9963-5821ae25ee5a" />
---

## 📦 Requirements

- Python 3.10 or above
- [PyQt6](https://pypi.org/project/PyQt6/)
- [PyQt6-WebEngine](https://pypi.org/project/PyQt6-WebEngine/)
- Tor binaries (`tor.exe`) and configuration file (`torrc`) included in `/tor/tor/` folder.

## Install dependencies:

- pip install PyQt6 PyQt6-WebEngine

## Cons

- Simple design.
- Cannot redirected to url using enter key(You have to click on search button).
- Unable to play videos from websites.
