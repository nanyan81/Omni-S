# 开源算法复现与封装（Algorithms）

**负责人**：算法层成员

## 接入方式

每接入一个开源算法，复制 `_template/` 目录并重命名为算法名（如 `stinr/`、`bering/`、`nucleus_segmentation/`），按模板补齐全部三类交付物。

## 必须提交的三类交付物

| 交付方向 | 接收成员 | 必交文件 |
|---|---|---|
| 一：工作流接口清单 | 工作流编排成员 | `run.py`、`input_spec.yaml`、`output_spec.yaml`、`config.yaml`、`runtime.md` |
| 二：依赖及环境清单 | 项目负责人 | `requirements.txt` / `environment.yml`、`system_dependencies.md` |
| 三：原始异常说明 | 异常捕获与回溯成员 | `error_mapping.yaml`（含原生异常、退出码、日志特征说明） |

## 注意事项

- 算法失败必须返回**非零退出码**，不能吞噬异常。
- 模型权重文件统一放服务器 `/Dataset/spatial-project/`，**严禁提交进 `weights/`**，仅在 `system_dependencies.md` 中写明下载来源与校验信息。
