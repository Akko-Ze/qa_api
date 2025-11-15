import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_deepseek import ChatDeepSeek
from langchain_classic.memory import ConversationBufferWindowMemory
# from langchain_classic.chains import LLMChain
from langchain_classic.prompts import ChatPromptTemplate

load_dotenv(override=True)
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# 初始化 DeepSeek 模型
llm = ChatDeepSeek(model="deepseek-chat", api_key=DEEPSEEK_API_KEY)

# 保存最近 5 条对话
memory = ConversationBufferWindowMemory(k=5)

# 构建多轮对话 prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你叫小智，是一名助人为乐的助手"),
    ("human", "{question}")
])

# conversation_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
conversation_chain = RunnableSequence(prompt | llm)


def get_deepseek_answer(question: str) -> str:
    """返回 DeepSeek 回答"""
    return conversation_chain.invoke({"question": question})
