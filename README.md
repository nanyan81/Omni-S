# Omni-S

面向科研人员的**空间组学工作流平台与 3D 重构分析项目**。

> **核心原则**：工作流平台负责把空间组学分析变成**可重复、可管理、可追溯**的工程流程；3D 重构与科研分析负责把空间组学数据转化成**可分析、可交互**的科研成果。两条路线共享标准化数据与契约，内部实现解耦。

---

## 1. 仓库定位与数据分离原则

- **GitHub（本仓库）**：只管理代码、算法封装、契约规范、Nextflow 工作流、Dockerfile、配置模板、测试脚本和文档。
- **服务器共享目录（`/Dataset/spatial-project/`）**：管理原始空间组学数据、大型模型权重、每次实验运行（`runs/run_xxx/`）的中间/最终结果与日志。
- **严禁提交大文件**：原始数据（`.h5ad` / `.tif` / `.parquet` 等）、模型权重（`.pt` / `.pth` / `.ckpt`）、Docker 镜像归档（`.tar`）、`runs/`、`work/` 均已被 `.gitignore` 拦截，请勿强制提交。

---

## 2. 目录结构与职责分工

```text
Omni-S/
├── .github/                      # PR 模板与 Issue 模板
├── contracts/                    # 项目级统一契约（数据 Schema、错误码 Schema、算法接口契约）
├── docs/                         # 架构设计、目录规范、科研调研交付物
│   ├── architecture/             # 协作方案、服务器目录规范、架构图
│   └── research/                 # 【科研1 & 科研2】平台调研、算法调研清单
├── components/                   # 核心功能模块
│   ├── data/                     # 【数据层】多平台原始数据读取与标准化
│   ├── dataprocess/              # 【数据层】基础有效性检查与约定前置预处理
│   ├── algorithms/               # 【算法层】开源算法复现、封装与标准接口（含 _template）
│   ├── runtime/                  # 【异常捕获与回溯】统一错误码、通用 Runtime Wrapper、错误映射
│   ├── qc/                       # 【项目负责人】空间组学科学 QC（后期按需接入）
│   ├── analysis/                 # 【科研1 & 科研2】需求驱动的直接数据分析
│   └── visualizations/           # 【科研1 & 科研2】3D 重构、基因表达颜色映射与手势交互
├── workflows/
│   └── nextflow/                 # 【工作流编排】Nextflow Pipeline、Process、Channel、配置
├── docker/                       # 【项目负责人】各模块/算法的 Dockerfile 与构建说明
└── tests/                        # 极小体积的模拟/脱敏测试样例与联调脚本
```

### 成员对应关系

| 路线 | 角色 | 主要负责目录 |
|---|---|---|
| 统筹与基础设施 | 项目负责人 | `docker/`、`components/qc/`、`contracts/` 评审、仓库与镜像管理 |
| 路线一：工作流平台 | 数据层成员 | `components/data/`、`components/dataprocess/` |
| 路线一：工作流平台 | 算法层成员 | `components/algorithms/` |
| 路线一：工作流平台 | 异常捕获与回溯成员 | `components/runtime/`、`contracts/error/` |
| 路线一：工作流平台 | 工作流编排成员 | `workflows/nextflow/` |
| 路线二：3D 与科研分析 | 科研1（平台与数据） | `docs/research/platforms/`、`components/analysis/`、`components/visualizations/` |
| 路线二：3D 与科研分析 | 科研2（算法与 3D） | `docs/research/algorithms/`、`components/analysis/`、`components/visualizations/` |

---

## 3. 快速开始（队员上手必读）

1. 先阅读协作规范：[CONTRIBUTING.md](CONTRIBUTING.md)。
2. 阅读项目总体协作方案与目录规范：[docs/architecture/README.md](docs/architecture/README.md)。
3. 进入你负责的模块目录，阅读该目录下的 `README.md`，了解输入输出契约和交付要求。
4. 从 `main` 切出自己的功能分支进行开发，完成后提交 Pull Request（禁止直接 push 到 `main`）。

---

## 4. 项目里程碑

- **M1**：科研调研完成（平台数据对照表、算法清单、3D 初步调研）
- **M2**：数据与算法接口确定（统一数据 Schema、算法输入输出规范、最小测试样例）
- **M3**：算法环境与异常规范完成（依赖清单、Docker 镜像、统一错误码、JSON Schema、Wrapper）
- **M4**：工作流平台打通（Nextflow Pipeline、多算法串联、错误追溯、断点续跑）
- **M5**：科研分析与 3D 原型（需求驱动分析、三维条件验证、基因表达颜色映射/筛选、手势交互）
- **M6**：两条路线集成验收
