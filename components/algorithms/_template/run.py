"""算法专用 Wrapper 模板（由算法层成员填写）。

职责：
1. 接收工作流传入的统一命令行参数（输入路径、输出路径、配置文件）。
2. 将项目统一输入映射为原始算法所需的输入格式。
3. 调用 src/original_algorithm/ 执行计算。
4. 失败时不要吞噬异常，必须返回非零退出码。
"""

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Omni-S Algorithm Wrapper Template")
    parser.add_argument("--input", required=True, type=Path, help="标准化输入路径")
    parser.add_argument("--output", required=True, type=Path, help="算法输出目录")
    parser.add_argument("--config", required=False, type=Path, help="算法参数 config.yaml")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        print(f"Input path does not exist: {args.input}", file=sys.stderr)
        return 1

    args.output.mkdir(parents=True, exist_ok=True)
    # TODO: 1. 读取 config.yaml
    # TODO: 2. 映射输入并调用原始算法
    # TODO: 3. 写出符合 output_spec.yaml 约定的结果文件
    raise NotImplementedError("请复制 _template 后实现具体算法调用逻辑")


if __name__ == "__main__":
    sys.exit(main())
