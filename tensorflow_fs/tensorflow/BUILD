# Description:
# TensorFlow is a computational framework, primarily for use in machine
# learning applications.

package(default_visibility = [":internal"])

licenses(["notice"])  # Apache 2.0

exports_files([
    "LICENSE",
    "ACKNOWLEDGMENTS",
])

# Config setting for determining if we are building for Android.
config_setting(
    name = "android",
    values = {
        "crosstool_top": "//external:android/crosstool",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "android_x86",
    values = {
        "crosstool_top": "//external:android/crosstool",
        "cpu": "x86",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "android_x86_64",
    values = {
        "crosstool_top": "//external:android/crosstool",
        "cpu": "x86_64",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "android_arm",
    values = {
        "crosstool_top": "//external:android/crosstool",
        "cpu": "armeabi-v7a",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "android_arm64",
    values = {
        "crosstool_top": "//external:android/crosstool",
        "cpu": "arm64-v8a",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "darwin",
    values = {"cpu": "darwin"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "windows",
    values = {"cpu": "x64_windows_msvc"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "no_tensorflow_py_deps",
    values = {"define": "no_tensorflow_py_deps=true"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "ios",
    values = {
        "crosstool_top": "//tools/osx/crosstool:crosstool",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "linux_x86_64",
    values = {"cpu": "k8"},
    visibility = ["//visibility:public"],
)

config_setting(
    name = "debug",
    values = {
        "compilation_mode": "dbg",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "optimized",
    values = {
        "compilation_mode": "opt",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "freebsd",
    values = {"cpu": "freebsd"},
    visibility = ["//visibility:public"],
)

package_group(
    name = "internal",
    packages = ["//tensorflow/..."],
)

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
            "g3doc/sitemap.md",
        ],
    ),
    visibility = ["//tensorflow:__subpackages__"],
)

filegroup(
    name = "all_opensource_files",
    data = [
        ":all_files",
        "//tensorflow/c:all_files",
        "//tensorflow/core:all_files",
        "//tensorflow/core/platform/default/build_config:all_files",
        "//tensorflow/core/platform/hadoop:all_files",
        "//tensorflow/python:all_files",
        "//third_party/hadoop:all_files",
        "//third_party/sycl:all_files",
        "//third_party/sycl/sycl:all_files",
    ],
    visibility = [":__subpackages__"],
)

load(
    "//third_party/mkl:build_defs.bzl",
    "if_mkl",
)

filegroup(
    name = "intel_binary_blob",
    data = if_mkl(
        [
            "//third_party/mkl:intel_binary_blob",
        ],
    ),
)

# -------------------------------------------
# New rules should be added above this target.
# -------------------------------------------