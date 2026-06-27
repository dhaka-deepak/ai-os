import subprocess


class VSCodeTool:

    @staticmethod
    def open_folder(folder):

        subprocess.Popen(
            [
                "code",
                folder
            ]
        )

        return f"VS Code opened: {folder}"