# Description:
#  Tools for building the TensorFlow pip package.

package(default_visibility = ["//visibility:private"])

load("//tensorflow:tensorflow.bzl", "transitive_hdrs")
load("//third_party/mkl:build_defs.bzl", "if_mkl")
load("//tensorflow/core:platform/default/build_config_root.bzl", "tf_additional_license_deps")

# This returns a list of headers of all public header libraries (e.g.,
# framework, lib), and all of the transitive dependencies of those
# public headers.  Not all of the headers returned by the filegroup
# are public (e.g., internal headers that are included by public
# headers), but the internal headers need to be packaged in the
# pip_package for the public headers to be properly included.
#
# Public headers are therefore defined by those that are both:
#
# 1) "publicly visible" as defined by bazel
# 2) Have documentation.
#
# This matches the policy of "public" for our python API.
transitive_hdrs(
    name = "included_headers",
    deps = [
        "//tensorflow/core:lib",
        "//tensorflow/core:protos_all_cc",
        "//third_party/eigen3",
    ],
)

filegroup(
    name = "licenses",
    data = [
        "//:LICENSE",
        "//third_party/eigen3:LICENSE",
        "//third_party/hadoop:LICENSE.txt",
        "@eigen_archive//:COPYING.MPL2",
        "@jemalloc//:COPYING",
        "@protobuf//:LICENSE",
        "@six_archive//:LICENSE",
        "@zlib_archive//:zlib.h",
    ] + tf_additional_license_deps(),
)
