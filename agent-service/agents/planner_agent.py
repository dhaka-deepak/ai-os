import json
import re
from pathlib import Path

from services.ollama_client import generate


PROMPT_FILE = (
    Path(__file__)
    .parent.parent
    / "prompts"
    / "planner_prompt.txt"
)


with open(
    PROMPT_FILE,
    "r",
    encoding="utf-8"
) as file:

    PLANNER_PROMPT = file.read()


class PlannerAgent:

    @staticmethod
    def create_plan(user_request: str):

        prompt = f"""
{PLANNER_PROMPT}

User Request:

{user_request}

Return ONLY JSON.

Example:

{{
    "steps":[
        {{
            "tool":"application",
            "action":"open",
            "target":"vscode"
        }}
    ]
}}
"""

        response = generate(prompt)

        print()
        print("========== RAW PLANNER ==========")
        print(response)
        print("================================")
        print()

        try:

            # If Ollama already returned valid JSON
            return json.loads(response)

        except Exception:

            pass

        try:

            # Extract first JSON object if extra text exists
            match = re.search(
                r"\{[\s\S]*\}",
                response
            )

            if match:

                return json.loads(
                    match.group(0)
                )

        except Exception as ex:

            print("Planner Error:", ex)

        return {
            "steps": []
        }