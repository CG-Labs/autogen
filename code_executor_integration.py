from pathlib import Path
from autogen import ConversableAgent
from autogen.coding import DockerCommandLineCodeExecutor, CodeBlock

# Define the working directory for the executor
work_dir = Path("/app/coding")
work_dir.mkdir(exist_ok=True)

# Instantiate the DockerCommandLineCodeExecutor
executor = DockerCommandLineCodeExecutor(work_dir=work_dir)

# Create a ConversableAgent with the code execution capability
code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={
        "executor": executor,
    },
    human_input_mode="NEVER",
)

# Example function to execute the web scraping tool
def execute_web_scraping_tool(url):
    code_block = f"""
import requests
from bs4 import BeautifulSoup

def fetch_web_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_information(soup):
    title = soup.title.string if soup.title else 'No title found'
    return {{'title': title}}

if __name__ == "__main__":
    url = "{url}"
    content = fetch_web_page(url)
    soup = parse_html(content)
    info = extract_information(soup)
    print(info)
"""
    result = executor.execute_code_blocks([CodeBlock(language="python", code=code_block, work_dir=str(work_dir))])
    return result

# Example function to execute the document comparison tool
def execute_document_comparison_tool(file1, file2):
    code_block = f"""
import os
from document_comparison_tool import compare_documents

file1 = "{file1}"
file2 = "{file2}"

if __name__ == "__main__":
    if os.path.exists(file1) and os.path.exists(file2):
        report = compare_documents(file1, file2)
        print(report)
    else:
        print("One or both files do not exist.")
"""
    result = executor.execute_code_blocks([CodeBlock(language="python", code=code_block, work_dir=str(work_dir))])
    return result

# Example usage
if __name__ == "__main__":
    # Execute the web scraping tool
    web_scraping_result = execute_web_scraping_tool("https://example.com")
    print("Web Scraping Result:", web_scraping_result)

    # Execute the document comparison tool
    document_comparison_result = execute_document_comparison_tool("/app/sample1.txt", "/app/sample2.txt")
    print("Document Comparison Result:", document_comparison_result)
