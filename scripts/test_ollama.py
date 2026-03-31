# Test Ollama LLM integration
from langchain_community.llms import Ollama

# Create an instance of the Ollama LLM
llm = Ollama(
    base_url="http://localhost:11434",
    model="llama3"
)

# Test can call the Ollama LLM and get a response
response = llm.invoke("What is retrieval augmented generation? Answer in 2 sentences.")
print(response)