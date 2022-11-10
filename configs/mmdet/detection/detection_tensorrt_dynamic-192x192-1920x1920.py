_base_ = ['../_base_/base_dynamic.py', '../../_base_/backends/tensorrt.py']
backend_config = dict(
    common_config=dict(max_workspace_size=8 << 30),
    model_inputs=[
        dict(
            input_shapes=dict(
                input=dict(
                    min_shape=[1, 3, 192, 192],
                    opt_shape=[1, 3, 640, 640],
                    max_shape=[1, 3, 1920, 1920])))
    ])

codebase_config = dict(
    post_processing=dict(
        score_threshold=0.1,
        confidence_threshold=0.1,  # for YOLOv3
        iou_threshold=0.65,
        max_output_boxes_per_class=4096,
        pre_top_k=1000,
        keep_top_k=100,
    ))
# 0: mmdeploy::BatchedNMSop
# 1: TRT:EfficientNMSop
# 2: TRT:BatchedNMSop
nms_method = 2
