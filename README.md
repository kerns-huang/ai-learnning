# Vanna Text-to-SQL 项目

本项目使用 Vanna 库将自然语言查询转换为 SQL 语句，并连接到 MySQL 数据库执行查询。

## 环境设置

### 1. Python 环境

建议使用 Python 3.8 或更高版本。您可以使用 `venv` 或 `conda` 创建虚拟环境。

使用 `venv`:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. 安装依赖

项目所需的依赖项已在 `requirements.txt` 文件中列出。使用以下命令安装：

```bash
pip install -r requirements.txt
```

### 3. 配置文件设置

项目使用 `config.ini` 文件来管理配置信息。为了安全起见，实际的配置文件不会被提交到 Git 仓库。您需要：

1. 复制配置文件模板：
```bash
cp config.template.ini config.ini
```

2. 编辑 `config.ini` 文件，填入您的配置信息：

```ini
[mysql]
host = your_host          # MySQL 服务器地址
database = your_database  # 数据库名称
user = your_user         # 数据库用户名
password = your_password # 数据库密码
port = 3306             # 数据库端口

[openai]
api_key = your_api_key   # OpenAI API 密钥
base_url = your_base_url # OpenAI API 基础URL
model = your_model      # 使用的模型名称

[vanna]
data_path = ./data      # Vanna 数据存储路径
```

注意：
- 请确保 `config.ini` 文件不会被提交到 Git 仓库（已在 `.gitignore` 中配置）
- 配置文件中的敏感信息（如密码、API密钥等）请妥善保管
- 建议将 `config.ini` 文件放在项目根目录下

## 运行项目

配置完成后，直接运行主脚本：

```bash
python vanna_mysql.py
```

脚本将：
1.  连接到指定的 MySQL 数据库。
2.  获取数据库中的所有表。
3.  使用 Vanna 训练每个表的 DDL (Data Definition Language) schema。
4.  您可以修改脚本末尾的 `question` 变量，输入您的自然语言查询。
5.  脚本将调用 Vanna 的 `ask` 方法来处理查询（默认实现可能会直接打印 SQL 或执行查询）。

## 注意

*   请确保您的 MySQL 服务正在运行，并且网络可以访问 OpenAI API 端点。
*   脚本中的 API 密钥和数据库凭证是敏感信息，请妥善保管，不要直接提交到版本控制系统。
*   配置文件 `config.ini` 包含了敏感信息，请确保它不会被提交到版本控制系统。

