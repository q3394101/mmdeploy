_base_ = ['../_base_/base_tensorrt-fp16_dynamic-320x320-1344x1344.py']
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
# 0: mmdeploy::BatchedNMSop
# 1: TRT:EfficientNMSop
# 2: TRT:BatchedNMSop
nms_method = 2
