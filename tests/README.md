# 最小测试样例与联调脚本（Tests）

本目录用于存放**极小体积（KB ~ 几 MB）的模拟或脱敏测试样例**以及跨模块端到端联调脚本，用于验证：
- 数据读取与基础有效性检查；
- 算法封装结果与原算法一致性；
- Runtime Wrapper 故障注入（缺失文件、非法参数、输出缺失）与 JSON 错误报告；
- Nextflow 最小 Pipeline 跑通与 `-resume` 断点续跑。

> **注意**：真实大规模空间组学样本存放在服务器 `/Dataset/spatial-project/datasets/`，严禁提交到本目录。
