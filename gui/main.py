import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtNetwork import *
import subprocess
import os
import threading
import time
   
class window:
   def __init__(self):
      self.app = QApplication(sys.argv)
      self.app.aboutToQuit.connect(self.cleanup) 
      self.widget = QWidget()
      self.textbar = QLineEdit()
      self.label = QLabel()
      self.layout = QVBoxLayout()
      self.buttons = QHBoxLayout()
      self.search = QHBoxLayout()
      self.browser = QWebEngineView()
      self.tor_process = None
      self.icons = os.path.abspath("icons")
      self.Buttons()
      self.icon_size()
      self.set_icons()
      self.setup_window()

   def Buttons(self):
      self.home_button = QPushButton()
      self.proxy_button = QPushButton()
      self.refresh_button = QPushButton()
      self.back_button = QPushButton()
      self.forward_button = QPushButton()
      self.load_url = QPushButton()

   def set_icons(self):
      self.widget.setWindowIcon(QIcon(os.path.join(self.icons,"logo.png")))
      self.home_button.setIcon(QIcon(os.path.join(self.icons,"home_button.png")))
      self.proxy_button.setIcon(QIcon(os.path.join(self.icons,"proxy_button.png")))
      self.refresh_button.setIcon(QIcon(os.path.join(self.icons,"refresh_button.png")))
      self.load_url.setIcon(QIcon(os.path.join(self.icons,"search_button.png")))
      self.back_button.setIcon(QIcon(os.path.join(self.icons,"back_button.png")))
      self.forward_button.setIcon(QIcon(os.path.join(self.icons,"forward_button.png")))
   
   def icon_size(self):
      self.home_button.setIconSize(QSize(24,24))
      self.proxy_button.setIconSize(QSize(24,24))
      self.load_url.setIconSize(QSize(20,20))
      self.refresh_button.setIconSize(QSize(24,24))
      self.back_button.setIconSize(QSize(24,24))
      self.forward_button.setIconSize(QSize(24,24))

   def setup_window(self):
      self.widget.setGeometry(200,200,650,350)
      self.widget.setWindowTitle(" ")
      self.textbar.setPlaceholderText("   URL...")
      self.search.addWidget(self.textbar)
      self.proxy_button.clicked.connect(self.proxy)
      self.load_url.clicked.connect(self.search_url)
      self.home_button.clicked.connect(self.go_home)
      self.refresh_button.clicked.connect(self.refresh)
      self.back_button.clicked.connect(self.back)
      self.forward_button.clicked.connect(self.forward)
      self.buttons.addWidget(self.home_button)
      self.buttons.addWidget(self.proxy_button)
      self.buttons.addWidget(self.refresh_button)
      self.buttons.addWidget(self.back_button)
      self.buttons.addWidget(self.forward_button)
      self.search.addWidget(self.load_url)
      self.browser.setHtml("""
         <html>
            <head>
               <title>Welcome</title>
               <style>
                  body {
                     background-color: black;
                     display: flex;
                     flex-direction: column;
                     align-items: center;
                     justify-content: center;
                     height: 100vh;
                     margin: 0;
                  }
                  h1 {
                     color: green;
                     text-align: center;
                  }
               </style>
            </head>
            <body>
               <h1>Welcome To My Custom Browser...</h1>
            </body>
         </html>
      """)
      self.layout.addLayout(self.buttons)
      self.layout.addLayout(self.search)
      self.layout.addWidget(self.browser)
      self.widget.setLayout(self.layout)
      self.browser.urlChanged.connect(self.update_url_bar)
      self.widget.show()

   def refresh(self):
      self.browser.reload()

   def back(self):
      self.browser.back()

   def forward(self):
      self.browser.forward()

   def go_home(self):
      self.browser.setHtml("""
         <html>
            <head>
               <title>Welcome</title>
               <style>
                  body {
                     background-color: black;
                     display: flex;
                     flex-direction: column;
                     align-items: center;
                     justify-content: center;
                     height: 100vh;
                     margin: 0;
                  }
                  h1 {
                     color: green;
                     text-align: center;
                  }
               </style>
            </head>
            <body>
               <h1>Welcome To My Custom Browser...</h1>
            </body>
         </html>
      """)

   def proxy(self):
      if self.tor_process is None: 
         self.proxy_button.setStyleSheet("background-color: yellow;")
         tor_path = os.path.abspath("tor//tor//tor.exe")
         torrc_path = os.path.abspath("tor//tor//tor//torrc")
         print("Starting Tor...")
         self.tor_process = subprocess.Popen(
            [tor_path, "-f", torrc_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True, 
            bufsize=1 
         )
         self.tor_thread = threading.Thread(target=self.tor_output_9050, daemon=True)
         self.tor_thread.start()

      else:
         if self.tor_process:
            print("Terminating Tor...")
            self.proxy_button.setStyleSheet("background-color: yellow;")
            self.tor_process.terminate()
            self.tor_process = None
         QTimer.singleShot(3000, self.tor_kill) 

   def tor_output_9050(self):
      for line in self.tor_process.stdout:
            print(line)
            if "100%" in line:
               proxy = QNetworkProxy(QNetworkProxy.ProxyType.Socks5Proxy, "127.0.0.1", 9050)
               QNetworkProxy.setApplicationProxy(proxy)
               self.proxy_button.setStyleSheet("background-color: green;")
               print("Tor Proxy is set...")

   def tor_kill(self):
      no_proxy = QNetworkProxy(QNetworkProxy.ProxyType.NoProxy)
      QNetworkProxy.setApplicationProxy(no_proxy)
      self.proxy_button.setStyleSheet("background-color: None;")
      print("Terminated Tor")

   def cleanup(self):
        if self.tor_process:
            print("Terminating Tor on app exit...")
            self.tor_process.terminate()
            self.tor_process = None

   def search_url(self):
      url_text = self.textbar.text().strip()
      if url_text:
         url = QUrl(url_text)
         if url.scheme() == "":
            url.setScheme("https")  
         self.browser.setUrl(url)
      else:
         print("Please enter a valid URL.") 

   def update_url_bar(self, url):
      url_str = url.toString()
      if not url_str.startswith("data:"):
         self.textbar.setText(url_str)

if __name__ == "__main__":
   exe = window()
   sys.exit(exe.app.exec())
