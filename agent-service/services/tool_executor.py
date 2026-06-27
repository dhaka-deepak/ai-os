from tools.app_tool import AppTool
from tools.file_tool import FileTool
from tools.terminal_tool import TerminalTool
from tools.calculator import calculate
from tools.datetime_tool import get_current_time
from tools.web_search import search_web


class ToolExecutor:

    @staticmethod
    def execute_step(step: dict):

        tool = step.get("tool")
        action = step.get("action")

        print()
        print("========== TOOL EXECUTOR ==========")
        print(step)
        print("===================================")

        try:

            # ---------------------------------------
            # Application Tool
            # ---------------------------------------
            if tool == "application":

                if action == "open":

                    target = step.get("target")

                    return AppTool.open_app(
                        target
                    )

            # ---------------------------------------
            # Terminal Tool
            # ---------------------------------------
            elif tool == "terminal":

                if action == "run":

                    command = step.get("command")

                    return TerminalTool.execute(
                        command
                    )

            # ---------------------------------------
            # File Tool
            # ---------------------------------------
            elif tool == "file":

                if action == "write":

                    return FileTool.create_file(
                        step.get("path"),
                        step.get("content", "")
                    )

                elif action == "read":

                    return FileTool.read_file(
                        step.get("path")
                    )

            # ---------------------------------------
            # Calculator Tool
            # ---------------------------------------
            elif tool == "calculator":

                expression = step.get(
                    "expression"
                )

                return calculate(
                    expression
                )

            # ---------------------------------------
            # Date / Time Tool
            # ---------------------------------------
            elif tool == "datetime":

                return get_current_time()

            # ---------------------------------------
            # Web Search Tool
            # ---------------------------------------
            elif tool == "web_search":

                return search_web(
                    step.get("query")
                )

            return f"Unsupported tool: {tool}"

        except Exception as ex:

            return (
                f"Execution Error: {str(ex)}"
            )