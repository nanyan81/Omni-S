# Nextflow 工作流编排（Workflows）

**负责人**：工作流编排成员（与异常捕获与回溯成员协同设计）

## 职责范围

- 依据 `components/algorithms/<algo>/` 下的接口契约编写 Nextflow Process（放 `modules/`）。
- 使用 Channel 传递标准化数据、算法输出与任务元数据（`run_id`、`sample_id` 等）。
- 接入通用 Runtime Wrapper，实现任务失败捕获、重试策略与 `-resume` 断点续跑。
- 严格遵循服务器目录规范：将工作目录指向当前 Run 的 `work/`，输出收集到 `output/`，日志保存到 `logs/`，并生成 `metadata.json`。

## 推荐目录结构

```text
workflows/nextflow/
├── main.nf              # 主流程入口（Workflow 定义）
├── nextflow.config      # 全局配置、执行器（local/docker/slurm）与资源配置
├── modules/             # 独立 Process 定义（data_validation、segmentation 等）
└── conf/                # 不同环境（dev / server / slurm）的配置片段
```
