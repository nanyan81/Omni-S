# 项目级契约规范（Contracts）

本目录是 Omni-S 跨模块协作的**唯一事实来源（Single Source of Truth）**。任何影响上下游接口的改动，必须先在此目录更新并经过相关负责人评审。

## 目录内容

- `data/spatial_data_schema.md`：项目级空间组学数据语义、核心字段、坐标单位与对象 ID 规范（工作流平台与 3D 重构共同遵守）。
- `error/error_schema.json`：统一任务结果与异常报告的 JSON Schema（v1.0，由异常捕获与回溯成员主责维护）。
- `algorithm/`：算法接入标准契约说明（对应模板见 `components/algorithms/_template/`）。

## 变更原则

1. 字段命名、数据类型、错误码枚举的变更必须通过 PR 提交，并 @ 受影响的上下游成员。
2. 所有 Schema 需保留版本号（如 `schema_version: "1.0"`），保证历史 `runs/` 结果可追溯。
