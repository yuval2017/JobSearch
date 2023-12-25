import platform
import shutil
import subprocess


class Paths:
    @staticmethod
    def find_chrome_path():
        system_platform = platform.system()

        if system_platform == 'Windows':
            # Try to find Chrome path using shutil on Windows
            chrome_path = shutil.which('chrome.exe')

        elif system_platform == 'Darwin':
            # Try to find Chrome path using shutil on macOS
            chrome_path = shutil.which('Google Chrome') or shutil.which('google-chrome')

            if chrome_path is None:
                # Try to find Chrome path using subprocess on macOS
                try:
                    chrome_path = subprocess.check_output(
                        ['mdfind', 'kMDItemDisplayName=="Google Chrome"']).decode().strip()
                except subprocess.CalledProcessError:
                    pass

        elif system_platform == 'Linux':
            # Try to find Chrome path using shutil on Linux
            chrome_path = shutil.which('google-chrome')

        else:
            # Unsupported operating system
            print(f"Unsupported operating system: {system_platform}")
            chrome_path = None

        return chrome_path
