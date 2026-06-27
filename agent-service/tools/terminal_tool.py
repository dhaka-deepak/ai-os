import subprocess


class TerminalTool:

    @staticmethod
    def execute(commands):

        if isinstance(
            commands,
            str
        ):
            commands = [commands]

        outputs = []

        for command in commands:

            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            outputs.append(
                result.stdout
            )

        return "\n".join(outputs)