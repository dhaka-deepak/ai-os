from services.tool_executor import ToolExecutor


class ExecutorAgent:

    @staticmethod
    def execute(plan: dict):

        steps = plan.get(
            "steps",
            []
        )

        if not steps:

            return "Nothing to execute."

        execution_log = []

        print()
        print("========== EXECUTOR ==========")

        for index, step in enumerate(steps):

            print(f"Executing Step {index + 1}")

            print(step)

            result = ToolExecutor.execute_step(
                step
            )

            execution_log.append(
                result
            )

        print("==============================")
        print()

        return "\n".join(execution_log)