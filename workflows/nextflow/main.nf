#!/usr/bin/env nextflow
nextflow.enable.dsl = 2

/*
 * Omni-S 空间组学工作流主入口（骨架）
 * 后续按阶段接入：DATA_PREPROCESS -> DATA_VALIDATION -> ALGORITHM -> DOWNSTREAM
 */

workflow {
    log.info """
    ========================================
    Omni-S Spatial Omics Workflow
    run_id     : ${params.run_id}
    dataset_id : ${params.dataset_id}
    outdir     : ${params.outdir}
    ========================================
    """.stripIndent()
}
