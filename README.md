# qa_api
简易问答机器人：langchain+fastapi

## 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/Akko-Ze/qa_api.git
cd qa_api
```

### 2. 创建虚拟环境

```python
python -m venv .venv
```

### 3. 安装依赖

```python
pip install -r requirements.txt
```

### 4. 设置API KEY

在项目根目录创建.env文件

```python
DEEPSEEK_API_KEY="你的 DeepSeek API Key"
```

### 5. 启动服务

```python
uvicorn main:app --reload
```

访问浏览器

http://127.0.0.1:8000

