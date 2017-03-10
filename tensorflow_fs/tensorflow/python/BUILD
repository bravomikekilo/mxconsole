# Description:
# Python support for TensorFlow.

package(default_visibility = [
    "//engedu/ml/tf_from_scratch:__pkg__",
    "//tensorflow:internal",
    "//tensorflow_models:__subpackages__",
])

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

load("//tensorflow:tensorflow.bzl", "if_not_windows")
load("//tensorflow:tensorflow.bzl", "tf_cuda_library")
load("//tensorflow:tensorflow.bzl", "tf_gen_op_wrapper_py")
load("//tensorflow:tensorflow.bzl", "py_test")
load("//tensorflow:tensorflow.bzl", "tf_py_test")
load("//tensorflow:tensorflow.bzl", "py_tests")
load("//tensorflow:tensorflow.bzl", "tf_py_wrap_cc")
load("//tensorflow:tensorflow.bzl", "cuda_py_test")
load("//tensorflow:tensorflow.bzl", "cuda_py_tests")
load("//tensorflow/core:platform/default/build_config.bzl", "tf_proto_library")
load("//tensorflow/core:platform/default/build_config.bzl", "tf_proto_library_py")
load("//tensorflow/core:platform/default/build_config.bzl", "tf_additional_lib_deps")
load("//tensorflow/core:platform/default/build_config_root.bzl", "tf_additional_plugin_deps")
load("//tensorflow/python:build_defs.bzl", "tf_gen_op_wrapper_private_py")

# py_library(
#     name = "python",
#     srcs = ["__init__.py"],
#     srcs_version = "PY2AND3",
#     visibility = [
#         "//tensorflow:__pkg__",
#         "//tensorflow/compiler/aot/tests:__pkg__",  # TODO(b/34059704): remove when fixed
#         "//tensorflow/contrib/learn:__pkg__",  # TODO(b/34059704): remove when fixed
#         "//tensorflow/contrib/learn/python/learn/datasets:__pkg__",  # TODO(b/34059704): remove when fixed
#         "//tensorflow/python/debug:__pkg__",  # TODO(b/34059704): remove when fixed
#         "//tensorflow/python/tools:__pkg__",  # TODO(b/34059704): remove when fixed
#         "//tensorflow/tensorboard/scripts:__pkg__",  # TODO(b/34059704): remove when fixed
#         "//tensorflow/tools/quantization:__pkg__",  # TODO(b/34059704): remove when fixed
#     ],
#     deps = [
#         ":array_ops",
#         ":check_ops",
#         ":client",
#         ":client_testlib",
#         ":cloud_ops",
#         ":confusion_matrix",
#         ":control_flow_ops",
#         ":errors",
#         ":framework",
#         ":framework_for_generated_wrappers",
#         ":functional_ops",
#         ":gradient_checker",
#         ":histogram_ops",
#         ":image_ops",
#         ":io_ops",
#         ":lib",
#         ":math_ops",
#         ":nn",
#         ":platform",
#         ":script_ops",
#         ":sdca_ops",
#         ":session_ops",
#         ":sets",
#         ":sparse_ops",
#         ":standard_ops",
#         ":state_ops",
#         ":string_ops",
#         ":summary",
#         ":metrics",
#         ":layers",
#         ":tensor_array_ops",
#         ":training",
#         ":ops",
#         ":test_ops",  # TODO: Break testing code out into separate rule.
#         ":util",
#         ":weights_broadcast_ops",
#         "//third_party/py/numpy",
#         "//tensorflow/python/ops/losses",
#         "//tensorflow/python/saved_model",
#     ] + if_not_windows([
#         "//tensorflow/contrib:contrib_py",
#     ]),
# )







cc_library(
    name = "py_record_reader_lib",
    srcs = ["lib/io/py_record_reader.cc"],
    hdrs = ["lib/io/py_record_reader.h"],
    deps = [
        "//tensorflow/c:c_api",
        "//tensorflow/c:tf_status_helper",
        "//tensorflow/core:lib",
    ],
)

cc_library(
    name = "py_record_writer_lib",
    srcs = ["lib/io/py_record_writer.cc"],
    hdrs = ["lib/io/py_record_writer.h"],
    deps = [
        "//tensorflow/c:c_api",
        "//tensorflow/c:tf_status_helper",
        "//tensorflow/core:lib",
    ],
)



tf_proto_library(
    name = "protos_all",
    srcs = glob(
        ["**/*.proto"],
        exclude = [
            "util/protobuf/compare_test.proto",
            "framework/cpp_shape_inference.proto",
        ],
    ),
    go_api_version = 2,
)


tf_py_wrap_cc(
    name = "pywrap_tensorflow_fs",
    srcs = ["tensorflow_fs.i"],
    swig_includes = [
        "lib/io/py_record_reader.i",
        "lib/io/py_record_writer.i",
        "lib/core/strings.i",
        "events_writer.i",
        "platform/base.i",
    ],
    deps = [
        "//tensorflow/core:lib",
        "//tensorflow/c:c_api",
        ":py_record_reader_lib",
        ":py_record_writer_lib",
        "//tensorflow/c:tf_status_helper",
        "//util/python:python_headers",
    ] + tf_additional_lib_deps() + tf_additional_plugin_deps()
)

tf_py_wrap_cc(
    name = "pywrap_file_io",
    srcs = ["lib/io/file_io.i"],
    swig_includes = [
        "lib/core/strings.i",
        "platform/base.i",
    ],
    deps = [
        "//tensorflow/core:lib",
        "//tensorflow/c:c_api",
        "//tensorflow/c:tf_status_helper",
        "//util/python:python_headers",
    ] + tf_additional_lib_deps() + tf_additional_plugin_deps()
)



# py_test(
#     name = "file_io_test",
#     size = "small",
#     srcs = ["lib/io/file_io_test.py"],
#     srcs_version = "PY2AND3",
#     deps = [
#         ":client_testlib",
#         ":errors",
#         ":lib",
#     ],
# )



filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
        ],
    ),
    visibility = ["//tensorflow:__subpackages__"],
)

