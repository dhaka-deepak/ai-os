from pathlib import Path


class FileTool:

    BASE_DIR = Path.home() / "AI_OS_FILES"

    BASE_DIR.mkdir(
        exist_ok=True
    )

    @staticmethod
    def create_file(
        filename,
        content
    ):

        path = (
            FileTool.BASE_DIR
            / filename
        )

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return f"File created: {path}"

    @staticmethod
    def write_file(
        filename,
        content
    ):

        path = Path(filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return f"Updated: {path}"

    @staticmethod
    def read_file(
        filename
    ):

        path = (
            FileTool.BASE_DIR
            / filename
        )

        if not path.exists():

            return "File not found"

        return path.read_text(
            encoding="utf-8"
        )