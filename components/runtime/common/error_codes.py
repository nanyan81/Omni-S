"""Omni-S 统一错误码定义（v1.0）。

对应规范见：
- contracts/error/error_schema.json
- docs/architecture/工作流平台与3D重构_协作方案.md
"""

from enum import Enum


class ErrorCode(str, Enum):
    INPUT_ERROR = "INPUT_ERROR"              # 输入错误：文件不存在、无法读取
    DATA_ERROR = "DATA_ERROR"                # 数据错误：数据结构或格式异常
    PARAMETER_ERROR = "PARAMETER_ERROR"      # 参数错误：参数缺失或不合法
    ENVIRONMENT_ERROR = "ENVIRONMENT_ERROR"  # 环境错误：缺少依赖、环境不兼容
    RESOURCE_ERROR = "RESOURCE_ERROR"        # 资源错误：内存、显存、磁盘不足
    ALGORITHM_ERROR = "ALGORITHM_ERROR"      # 算法错误：算法内部计算失败
    OUTPUT_ERROR = "OUTPUT_ERROR"            # 输出错误：输出文件缺失、损坏或不完整
    EXECUTION_ERROR = "EXECUTION_ERROR"      # 执行错误：进程启动失败、异常终止
    UNKNOWN_ERROR = "UNKNOWN_ERROR"          # 未知错误：证据不足，无法可靠判断


DEFAULT_RETRYABLE = {
    ErrorCode.INPUT_ERROR: False,
    ErrorCode.DATA_ERROR: False,
    ErrorCode.PARAMETER_ERROR: False,
    ErrorCode.ENVIRONMENT_ERROR: False,
    ErrorCode.RESOURCE_ERROR: True,
    ErrorCode.ALGORITHM_ERROR: False,
    ErrorCode.OUTPUT_ERROR: False,
    ErrorCode.EXECUTION_ERROR: False,
    ErrorCode.UNKNOWN_ERROR: False,
}
