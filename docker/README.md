# Docker 环境与镜像管理

**负责人**：项目负责人

## 职责范围

- 审核算法层提交的依赖清单（`requirements.txt`、`environment.yml`、`system_dependencies.md`）及 CUDA/PyTorch 兼容性。
- 按模块或算法维护独立目录（例如 `docker/base/`、`docker/stinr/`），编写 `Dockerfile` 与构建说明。
- 统一管理镜像命名与版本号（例如 `omni-s/<algo>:<version>`），便于 `runs/run_xxx/metadata.json` 记录与复现。

## 注意事项

- 离线导出的镜像归档 `.tar` 文件统一放服务器 `/Dataset/spatial-project/shared/container-archives/`，**严禁提交进本仓库**。
