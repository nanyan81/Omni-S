# 异常捕获与运行回溯（Runtime）

**负责人**：异常捕获与回溯成员

## 职责范围

1. **统一错误码与 Schema**：维护 `common/error_codes.py` 与 `contracts/error/error_schema.json`。
2. **通用 Runtime Wrapper**（`wrapper/`）：
   - 启动各算法的专用 Wrapper（`run.py`）；
   - 收集 Exit Code、stdout、stderr、Signal；
   - 即使退出码为 0，也执行必需输出完整性检查（缺失则判为 `OUTPUT_ERROR`）；
   - 依据各算法的 `error_mapping.yaml` 映射统一错误码（证据不足时归为 `UNKNOWN_ERROR`）；
   - 生成统一 JSON 任务报告，并**透传非零退出码**给 Nextflow。
3. **运行追溯与状态桥接**：记录 `run_id`、`task_id`、`sample_id`、`attempt` 及诊断日志路径，与工作流编排成员共同设计失败重试与断点续跑策略。
