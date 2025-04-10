

本地跑
flask_cicd_demo pytest


用docker 跑測試
在測試完後自動移除 container：
```shll
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
```



語法	意思
if: success()	只有上一步成功才執行
if: failure()	只有上一步失敗才執行
if: always()	不論成功或失敗都會執行
if: github.ref == 'refs/heads/main'	只有 main 分支才跑（做分支控制）