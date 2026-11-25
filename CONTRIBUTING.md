# Omni-S 团队协作规范

本规范旨在保证 6 人团队并行开发时代码清晰、接口对齐、互不冲突。

---

## 1. 四条基本底线

1. **禁止直接向 `main` 分支推送代码**：所有改动必须通过 Pull Request (PR) 合并。
2. **禁止提交原始数据、模型权重和运行结果**：大数据统一存放在服务器 `/Dataset/spatial-project/`，仓库只保留代码、契约、文档和极小体积的测试样例（建议单文件 < 5 MB）。
3. **接口先行，契约对齐**：修改任何跨模块数据格式、字段名、错误码或命令行参数前，先在 `contracts/` 中更新文档并通知上下游成员。
4. **不在非负责目录随意改动**：跨模块修改请先与对应目录负责人沟通，或在 PR 中 @ 对应负责人审核。

---

## 2. 分支命名规范

统一从最新的 `main` 分支切出工作分支，格式为 `<模块或类型>/<简短描述>`：

- `research/<topic>`：科研平台/算法调研文档（如 `research/xenium-platform-mapping`）
- `data/<topic>`：数据读取、标准化、基础检查（如 `data/xenium-reader`）
- `algo/<name>`：算法复现与封装（如 `algo/stinr-wrapper`）
- `runtime/<topic>`：错误码、Runtime Wrapper、回溯（如 `runtime/error-schema-v1`）
- `workflow/<topic>`：Nextflow Pipeline 开发（如 `workflow/segmentation-module`）
- `docker/<name>`：Dockerfile 与镜像构建（如 `docker/stinr-env`）
- `recon3d/<topic>`：3D 重构与数据分析（如 `recon3d/gene-color-mapping`）
- `docs/<topic>`：纯文档修改

示例：
```bash
git checkout main
git pull origin main
git checkout -b algo/stinr-wrapper
```

---

## 3. 提交信息（Commit Message）规范

使用简洁的 `<type>: <简短中文或英文说明>` 格式：

- `feat:` 新增功能或新算法接入
- `fix:` 修复 Bug
- `docs:` 文档或调研报告更新
- `refactor:` 代码重构（不改变外部接口）
- `chore:` 配置、目录整理、CI、Docker 构建等
- `test:` 测试样例或测试脚本

示例：
- `feat: 添加 Xenium 原始数据读取器`
- `docs: 补充 Stereo-seq 平台字段映射表`
- `fix: 修复 Runtime Wrapper 退出码透传问题`

---

## 4. 算法接入三方交付检查清单

算法层提交新算法 PR 时，必须同时包含三类交付物（详见 `components/algorithms/_template/`）：

1. **给工作流编排成员**：`run.py`、`input_spec.yaml`、`output_spec.yaml`、`config.yaml`、`runtime.md`
2. **给项目负责人（Docker 构建）**：`requirements.txt` / `environment.yml`、`system_dependencies.md`（含 CUDA/PyTorch 与权重说明）
3. **给异常捕获成员**：`error_mapping.yaml`（原生异常、退出码、日志特征与故障测试说明）

---

## 5. Pull Request 合并流程

1. 本地确认没有误提交大文件（`git status` 检查）。
2. 在 GitHub 上创建 PR，按 PR 模板填写改动内容、影响模块与验证方式。
3. 指定项目负责人（以及受影响的上下游成员）为 Reviewer。
4. 评审通过后合并至 `main`，合并后可删除已完成的临时功能分支。
