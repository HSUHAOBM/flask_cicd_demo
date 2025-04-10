

本地跑
flask_cicd_demo pytest


用docker 跑測試
在測試完後自動移除 container：
```shll
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
```

