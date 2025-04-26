import configparser
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI


def load_config():
    """加载配置文件"""
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    return config

# 加载配置
config = load_config()

db_user = config['mysql']['user']
db_password = config['mysql']['password']
#db_host = "localhost:3306"
db_host = config['mysql']['host']
db_name = config['mysql']['database']
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")


# 配置  llm 大模型
llm = ChatOpenAI(
    temperature=0.01,
    model="deepseek-chat",  
    openai_api_key = "sk-9846f14a2104490b960adbf5c5b3b32e",
    openai_api_base="https://api.deepseek.com"
)

# 设置 db 和 llm 大模型
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 创建 sql agent  
agent_executor = create_sql_agent(
    llm=llm,  # 设置 llm 大模型
    toolkit=toolkit,  # 设置工具
    verbose=True  # 设置 verbose
)

# Task: 描述数据表
agent_executor.run("描述与订单相关的表及其关系")

# 这个任务，实际上数据库中 没有HeroDetails表
agent_executor.run("描述HeroDetails表")

agent_executor.run("找出英雄攻击力最高的前5个英雄")