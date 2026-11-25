# 数据读取与标准化（Data Layer）

**负责人**：数据层成员

## 职责范围

- 根据科研1提供的平台清单（`docs/research/platforms/`），读取 Xenium、Stereo-seq、Visium HD、CosMx、MERFISH 等平台原始数据。
- 解析 TIFF、CSV、Parquet、H5AD 等格式，统一字段名称、数据类型、坐标单位与元数据。
- 将原始数据转换为符合 `contracts/data/spatial_data_schema.md` 的标准化数据。

## 建议子目录

- `readers/`：按平台拆分读取器（如 `xenium.py`、`stereoseq.py`）。
- `converters/`：统一格式转换（如转标准 `AnnData` / `.h5ad`）。

## 协作边界

- 前期输入数据已做过筛选，本模块不负责空间组学科学 QC（由项目负责人在 `components/qc/` 统筹）。
- 原始大型数据存放在服务器 `/Dataset/spatial-project/datasets/`，严禁提交到本仓库。
