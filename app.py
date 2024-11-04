import os
import dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

dotenv.load_dotenv()

llm_config = {"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={
        "executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")
    },
)

user_proxy.initiate_chat(
    assistant,
    message="나미비아의 수도가 어디야?",
)
