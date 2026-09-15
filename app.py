import webview
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    html_path = resource_path('wea.html')
    window = webview.create_window('Погодный информер', html_path, width=480, height=650, resizable=True, min_size=(350, 500))
    webview.start()

if __name__ == '__main__':
    main()
