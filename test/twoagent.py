import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Set the OAI_CONFIG_LIST environment variable directly in the script
os.environ['OAI_CONFIG_LIST'] = os.path.join(os.path.dirname(__file__), 'agentchat/contrib/example_agent_builder_library.json')

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"work_dir": "coding", "use_docker": True}
)  # IMPORTANT: set to True to run code in docker, recommended

# Correct the model parameter to be a single string
assistant.llm_config["model"] = "gpt-4"

user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
