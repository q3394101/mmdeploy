_base_ = ['../_base_/base_tensorrt_static-800x1344.py']
onnx_config = dict(input_shape=(640, 640))

backend_config = dict(
    common_config=dict(max_workspace_size=8 << 30),
    model_inputs=[
        dict(
            input_shapes=dict(
                input=dict(
                    min_shape=[1, 3, 640, 640],
                    opt_shape=[1, 3, 640, 640],
                    max_shape=[1, 3, 640, 640])))
    ])

no_customop = True
nms_method = 1
