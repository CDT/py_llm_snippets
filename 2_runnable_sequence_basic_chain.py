from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from deepseek_config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL

# 1. Load the model (you already know this)
llm = ChatOpenAI(model=DEEPSEEK_MODEL,
                 api_key=DEEPSEEK_API_KEY,
                 base_url=DEEPSEEK_BASE_URL,
                 temperature=0.7)

# 2. Define the prompt template
prompt = PromptTemplate.from_template(
    "What is a creative tagline for a {product} startup?"
)

# 3. Build a RunnableSequence with the pipe operator
chain = prompt | llm

# 4. Call it
result = chain.invoke({"product": "AI-powered coffee machine"})
print(result.content)   # result is an AIMessage
