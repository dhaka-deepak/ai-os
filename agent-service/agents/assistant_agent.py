from pathlib import Path

from services.memory_client import MemoryClient
from services.ollama_client import generate

from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent


PROMPT_FILE = (
    Path(__file__)
    .parent.parent
    / "prompts"
    / "system_prompt.txt"
)

with open(
    PROMPT_FILE,
    "r",
    encoding="utf-8"
) as file:

    SYSTEM_PROMPT = file.read()


class AssistantAgent:

    @staticmethod
    def process(
        session_id,
        message
    ):

        # -----------------------------------
        # Save User Message
        # -----------------------------------
        MemoryClient.save_message(
            session_id,
            "user",
            message
        )
        
        print("=" * 60)
        print("ASSISTANT AGENT")
        print(message)
        print("=" * 60)

        # -----------------------------------
        # Load Conversation History
        # -----------------------------------
        history = MemoryClient.get_messages(
            session_id
        )

        conversation = ""

        for sender, content in history:

            conversation += (
                f"{sender}: {content}\n"
            )

        # -----------------------------------
        # Ask Planner Agent
        # -----------------------------------
        plan = PlannerAgent.create_plan(
            message
        )
        
        print("=" * 60)
        print("PLAN")
        print(plan)
        print("=" * 60)

        print()
        print("========== EXECUTION PLAN ==========")
        print(plan)
        print("====================================")
        print()

        # -----------------------------------
        # If planner generated executable steps,
        # execute them.
        # -----------------------------------
        if plan.get("steps"):

            answer = ExecutorAgent.execute(
                plan
            )
            
            print("=" * 60)
            print("EXECUTION RESULT")
            print(answer)
            print("=" * 60)

        else:

            # -----------------------------------
            # Normal Chat
            # -----------------------------------

            prompt = f"""
{SYSTEM_PROMPT}

Conversation History:

{conversation}

User:
{message}

Assistant:
"""

            answer = generate(
                prompt
            )

        # -----------------------------------
        # Save Assistant Response
        # -----------------------------------
        MemoryClient.save_message(
            session_id,
            "assistant",
            answer
        )

        return answer