# Flask CI/CD Demo

- Flask
- pytest 測試
- Compose 容器化
- 使用 GitHub Actions 實作 CI/CD，自動測試與自動部署到 Linode
- Slack 通知部署成功與失敗


## 本地測試方式

```bash
pip install -r requirements.txt
pytest
```

---

## 使用 Docker 執行測試

```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
```
自動在測試結束後移除 container，避免掛著不結束。

---

## GitHub Actions 條件語法備忘

| 語法                              | 意思                             |
|-----------------------------------|----------------------------------|
| `if: success()`                   | 只有上一步成功才執行              |
| `if: failure()`                   | 只有上一步失敗才執行              |
| `if: always()`                    | 不論成功或失敗都會執行            |
| `if: github.ref == 'refs/heads/main'` | 只有 main 分支才跑               |

---

## GitHub Secrets 說明

| Secret 名稱              | 說明                                     |
|--------------------------|------------------------------------------|
| `LINODE_HOST`            | Linode 的主機 IP                         |
| `LINODE_USERNAME`        | 登入使用者名稱（如 root）               |
| `LINODE_SSHKEY`          | SSH 私鑰內容（貼整份，不是 .pub）         |
| `LINODE_PROJECT_PATH`    | 部署用的資料夾路徑，例如 `/home/ian/flask-cicd-demo` |
| `SLACK_WEBHOOK_URL`      | Slack 的 webhook URL 用於通知           |

---

## Slack 通知功能

在 CI/CD 過程中，會根據測試成功或失敗透過 Slack Webhook 發送通知，包含：

- Repo 名稱
- 分支名稱
- Commit ID（可點擊）
- Push 作者
- 成功 ✅ 或失敗 ❌ 標記

