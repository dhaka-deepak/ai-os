import subprocess
import shutil
from pathlib import Path


class AppTool:

    @staticmethod
    def open_app(app_name, target=None):

        app_name = app_name.lower().strip()

        # -------------------------
        # VS Code
        # -------------------------
        if app_name in [
            "vscode",
            "vs code",
            "visual studio code",
            "code"
        ]:

            code_path = shutil.which("code")

            if code_path:

                if target:
                    subprocess.Popen(
                        [code_path, str(target)]
                    )
                else:
                    subprocess.Popen(
                        [code_path]
                    )

                return "VS Code opened."

            possible_paths = [

                r"C:\Users\Deepak Dhaka\AppData\Local\Programs\Microsoft VS Code\Code.exe",

                r"C:\Program Files\Microsoft VS Code\Code.exe",

                r"C:\Program Files (x86)\Microsoft VS Code\Code.exe"
            ]

            for path in possible_paths:

                if Path(path).exists():

                    if target:
                        subprocess.Popen(
                            [path, str(target)]
                        )
                    else:
                        subprocess.Popen(
                            [path]
                        )

                    return "VS Code opened."

            return (
                "VS Code not found. "
                "Install it or add 'code' to PATH."
            )

        # -------------------------
        # PowerShell
        # -------------------------
        elif app_name in [
            "powershell",
            "power shell"
        ]:

            subprocess.Popen(
                ["powershell.exe"]
            )

            return "PowerShell opened."

        # -------------------------
        # Notepad
        # -------------------------
        elif app_name == "notepad":

            subprocess.Popen(
                ["notepad.exe"]
            )

            return "Notepad opened."

        # -------------------------
        # Calculator
        # -------------------------
        elif app_name in [
            "calculator",
            "calc"
        ]:

            subprocess.Popen(
                ["calc.exe"]
            )

            return "Calculator opened."

        # -------------------------
        # Paint
        # -------------------------
        elif app_name == "paint":

            subprocess.Popen(
                ["mspaint.exe"]
            )

            return "Paint opened."

        # -------------------------
        # Chrome
        # -------------------------
        elif app_name == "chrome":

            chrome = shutil.which("chrome")

            if chrome:

                subprocess.Popen(
                    [chrome]
                )

                return "Chrome opened."

            chrome_paths = [

                r"C:\Program Files\Google\Chrome\Application\chrome.exe",

                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]

            for path in chrome_paths:

                if Path(path).exists():

                    subprocess.Popen(
                        [path]
                    )

                    return "Chrome opened."

            return "Chrome not installed."

        return f"Unsupported application: {app_name}"