# sample_mcp

## setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## setup mcp

cursorを開く

```bash
❯ cursor ~/.cursor/mcp.json
```

```json
{
  "mcpServers": {
    ...
    "sample-mcp": {
      "command": "/Users/〇〇/sample_mcp/venv/bin/python", // セットアップでアクティベートしたpythonの絶対パス
      "args": ["/Users/〇〇/sample_mcp/server.py"] // サーバーの絶対パス
    }
  }
}
```