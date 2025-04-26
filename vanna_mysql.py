### 使用vanna 做 text2sql的具体实现过程

#!/usr/bin/env python
# coding: utf-8

import configparser
from vanna.openai import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
import mysql.connector
from openai import OpenAI

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None,client=None):
        # 分离配置，只将OpenAI客户端传递给OpenAI_Chat
        self.client = client
        # 初始化两个基类 向量数据库和LLM配置
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

def load_config():
    """加载配置文件"""
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    return config

# 加载配置
config = load_config()

# 创建OpenAI客户端
client = OpenAI(
    api_key=config['openai']['api_key'],
    base_url='https://chatapi.littlewheat.com/v1'
)

# 初始化Vanna实例
vn = MyVanna(config={
    'model': 'gpt-4o-mini',
    'path': './data'
},client=client)

# 连接到MySQL数据库
try:
    connection = mysql.connector.connect(
        host=config['mysql']['host'],
        database=config['mysql']['database'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        port=int(config['mysql']['port'])
    )
    print("成功连接到MySQL数据库")
    
    # 获取所有表名
    cursor = connection.cursor()
    cursor.execute("""
        SELECT TABLE_NAME 
        FROM information_schema.TABLES 
        WHERE TABLE_SCHEMA = %s
    """, (config['mysql']['database'],))
    tables = cursor.fetchall()
    
    # 训练每个表的schema
    for (table_name,) in tables:
        try:
            # 获取表的创建语句
            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            _, create_table = cursor.fetchone()
            
            print(f"正在训练表 {table_name} 的schema...")
            vn.train(ddl=create_table)
            
        except Exception as e:
            print(f"训练表 {table_name} 失败: {str(e)}")
            continue
    
    print("Schema训练完成")
    
    # 示例：使用Vanna进行自然语言查询
    question = "找出英雄攻击力最高的前5个英雄"
    vn.ask(question)
    
except mysql.connector.Error as err:
    print(f"数据库连接错误: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL连接已关闭")


# In[ ]:


# #help(vn.ask)
# #vn.ask("查询heros表中 英雄攻击力前5名的英雄")
# sql=vn.generate_sql("查询heros表中 英雄攻击力前5名的英雄")
# print('sql=', sql)
# vn.run_sql(sql)

