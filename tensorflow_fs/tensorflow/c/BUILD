# Description:
# C API for TensorFlow, for use by client language bindings.

licenses(["notice"])  # Apache 2.0

load(
    "//tensorflow:tensorflow.bzl",
    "tf_cc_test",
    "tf_copts",
    "tf_cuda_library",
    "tf_custom_op_library",
)

# For platform specific build config
load(
    "//tensorflow/core:platform/default/build_config.bzl",
    "tf_kernel_tests_linkstatic",
)

# -----------------------------------------------------------------------------
# Public targets

filegroup(
    name = "headers",
    srcs = ["c_api.h"],
    visibility = ["//tensorflow:__subpackages__"],
)

cc_library(
    name = "c_api",
    srcs = [
        "c_api.cc",
        "version.h",
    ],
    hdrs = ["c_api.h"],
    copts = tf_copts(),
    visibility = ["//visibility:public"],
    deps = select({
        "//tensorflow:android": [
        ],
        "//conditions:default": [
            "//tensorflow/core:lib",
        ],
    }),
)

cc_library(
    name = "tf_status_helper",
    srcs = ["tf_status_helper.cc"],
    hdrs = ["tf_status_helper.h"],
    visibility = ["//visibility:public"],
    deps = [
        ":c_api",
        "//tensorflow/core:lib",
    ],
)


# -----------------------------------------------------------------------------
# Tests


# -----------------------------------------------------------------------------
# Google-internal targets.

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
