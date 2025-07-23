# 🕸️ Tor-Powered Custom Web Browser (PyQt6)

This is a lightweight custom web browser built with **PyQt6** and integrated with **Tor** for anonymous browsing. It includes basic navigation buttons, URL input, and a proxy toggle that starts/stops a Tor instance locally.

> **Note**: This is a minimal educational browser prototype, not a full-featured secure browsing solution.
> **Note**: Assisted by ChatGPT for coding help and design decisions.

---

## 🚀 Features

- 🧭 Basic browser navigation (Back, Forward, Refresh, Home)
- 🌐 URL search bar
- 🛡️ Tor proxy integration (SOCKS5 on port 9050 or 9055)
- ✅ Tor toggle with visual status (yellow = starting, original = active)
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
<img width="1366" height="768" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/a10eb165-c732-4b5b-b4ad-b6fea78baf2c" />
<img width="1366" height="768" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/459973d4-5548-452e-a18a-30ec5fcc96a1" />
<img width="1366" height="768" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/7b0fb039-9b4d-4397-9406-e310844551a8" />
<img width="1366" height="768" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/7edd8196-31dd-470a-8791-b01ec91a8a37" />

---

## 📦 Requirements

- Python 3.10 or above
- [PyQt6](https://pypi.org/project/PyQt6/)
- [PyQt6-WebEngine](https://pypi.org/project/PyQt6-WebEngine/)
- Tor binaries (`tor.exe`) and configuration file (`torrc`) included in `/tor/tor/` folder.

## Install dependencies:

- pip install PyQt6 PyQt6-WebEngine

## 🔧 Change Tor Port

- step-1: Open the main.py file in any code editor.

- step-2: Scroll to the second proxy function under the comment (# -------------- TOR --> 9055 ---------------------------------------).

- step-3: Uncomment the entire second function block.

- step-4: Comment out the original proxy function (the one under # -------------- TOR --> 9050 ---------------------------------------).

- step-5: Save the file and rerun the browser.

## Cons

- Simple design.
- Cannot redirected to url using enter key(You have to click on search button).
- Unable to play videos from websites.
