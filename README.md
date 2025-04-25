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

### 3. 配置数据库连接和 OpenAI API

在 `vanna_mysql.py` 脚本中，您需要配置以下信息：

*   **MySQL 数据库连接信息**:
    *   `host`
    *   `dbname`
    *   `user`
    *   `password`
    *   `port`
*   **OpenAI API**:
    *   `api_key`
    *   `base_url` (如果使用代理或特定端点)
    *   `model` (例如 'gpt-4o-mini')

请根据您的实际情况修改脚本中的相应值。

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
*   脚本中的 API 密钥和数据库凭证是敏感信息，请妥善保管，不要直接提交到版本控制系统。考虑使用环境变量或配置文件管理这些凭证。 