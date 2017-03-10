# Description:
# TensorFlow is a computational framework, primarily for use in machine
# learning applications.
#
# Public targets:
#
# ":protos_all" - exports all core TensorFlow protos
#     ":protos_all_py" - py_proto_library version (Google-internal)
# ":lib" - exports the public non-test headers for:
#     platform/: Platform-specific code and external dependencies
#     lib/: Low-level libraries that are not TensorFlow-specific
# ":test" - test equivalent of ":lib".
#     This is currently public, but may be made internal in the
#     future.  Try to avoid depending on it.
# ":framework" - exports the public non-test headers for:
#     util/: General low-level TensorFlow-specific libraries
#     framework/: Support for adding new ops & kernels
#     example/: Wrappers to simplify access to Example proto
# ":ops" - defines TensorFlow ops, but no implementations / kernels
#     ops/: Standard ops
#     user_ops/: User-supplied ops
#     This aggregates a number of smaller op libraries (":*_op_lib")
# ":core_cpu" - exports the public non-test headers for:
#     graph/: Support for graphs made up of ops
#     common_runtime/: Common code for execution of graphs
#     public/: Public APIs for running graphs
# ":core" - The code for ":core_cpu" plus a GPU runtime
# ":all_kernels" - The cpu-specific kernels, plus gpu kernels if
#     built with Cuda
# ":tensorflow_opensource" - The complete open-source package, including
#      ":all_kernels", ":core", and a Session implementation.
# ":tensorflow" - "tensorflow_opensource" plus some Google-internal libraries.
# ":testlib" - TensorFlow-specific test support, e.g. utilities for testing
#      kernels.
# ":direct_session" - An implementation of the Session interface that
#      directly runs Graphs via the internal TensorFlow executor.
#  "framework_lite" - Intended to be used by operator implementations
#      (kernels) that can also be run outside the tensorflow runtime. This
#      contains a small set of headers and utilities that can be used for core
#      kernels, without bringing in libraries that can bloat code size (e.g.,
#      logging is not included because using it will bring in a large amount of
#      ostream code).
#
# ":example_parser_configuration" -- A library for extracting the
#      tensorflow.Example proto configuration from a Graph.
#
# Public Android targets:
#
# filegroup ":android_proto_srcs" - Protos
# filegroup ":android_srcs" - Core sources
# cc_library ":android_tensorflow_lib" - Native library
# cc_library ":android_tensorflow_lib_selective_registration" - Native library
#   supporting SELECTIVE_REGISTRATION feature.
# portable_proto_library ":android_proto_lib" (Google-internal)

package(default_visibility = [
    "//tensorflow:internal",
    "//tensorflow_models:__subpackages__",
])

licenses(["notice"])  # Apache 2.0

load(
    "//tensorflow:tensorflow.bzl",
    "if_android",
    "if_ios",
    "if_x86",
    "if_not_mobile",
    "if_not_windows",
    "tf_copts",
    "tf_cc_test",
    "tf_cc_tests",
    "tf_cuda_library",
    "tf_gen_op_libs",
    "tf_generate_proto_text_sources",
    "tf_genrule_cmd_append_to_srcs",
    "tf_opts_nortti_if_android",
    "cc_header_only_library",
)
load("//tensorflow:tensorflow.bzl", "tf_cc_test_mkl")
load("//tensorflow:tensorflow.bzl", "tf_cc_test_gpu")
load("//tensorflow:tensorflow.bzl", "tf_cc_tests_gpu")
load("//tensorflow:tensorflow.bzl", "tf_version_info_genrule")

# For platform specific build config
load(
    "//tensorflow/core:platform/default/build_config.bzl",
    "tf_proto_library",
    "tf_proto_library_cc",
    "tf_additional_core_deps",
    "tf_additional_lib_defines",
    "tf_additional_lib_deps",
    "tf_additional_lib_hdrs",
    "tf_additional_lib_srcs",
    "tf_additional_minimal_lib_srcs",
    "tf_additional_proto_hdrs",
    "tf_additional_proto_srcs",
    "tf_additional_stream_executor_srcs",
    "tf_additional_cupti_wrapper_deps",
    "tf_additional_libdevice_data",
    "tf_additional_libdevice_deps",
    "tf_additional_libdevice_srcs",
    "tf_additional_test_deps",
    "tf_additional_test_srcs",
    "tf_env_time_hdrs",
    "tf_env_time_srcs",
    "tf_kernel_tests_linkstatic",
    "tf_additional_cloud_op_deps",
    "tf_additional_cloud_kernel_deps",
)
load(
    "//tensorflow/core:platform/default/build_config_root.bzl",
    "tf_cuda_tests_tags",
)
load(
    "//third_party/mkl:build_defs.bzl",
    "if_mkl",
)
load("@local_config_sycl//sycl:build_defs.bzl", "if_sycl")

# -----------------------------------------------------------------------------
# Public targets

# Protos which are needed for core tensorflow, including on mobile builds.
#
# Note that some protos are in neither additional_core_proto_srcs nor this
# filegroup; e.g.  ones with individual proto_library targets.
CORE_PROTO_SRCS = [
    "framework/resource_handle.proto",
    "framework/summary.proto",
    "framework/tensor.proto",
    "framework/tensor_shape.proto",
    "framework/types.proto",
    "lib/core/error_codes.proto",
    "util/event.proto",
]

# Protos which are not needed on mobile builds, but should be included in
# protos_all.
#
# Note that some protos are in neither core_proto_srcs nor this filegroup; e.g.
# ones with individual proto_library targets.
ADDITIONAL_CORE_PROTO_SRCS = [
]

tf_proto_library(
    name = "reader_base_proto",
    srcs = ["framework/reader_base.proto"],
    cc_api_version = 2,
    go_api_version = 2,
    java_api_version = 2,
    visibility = ["//visibility:public"],
)

tf_proto_library(
    name = "protos_all",
    srcs = CORE_PROTO_SRCS + ADDITIONAL_CORE_PROTO_SRCS,
    cc_api_version = 2,
    go_api_version = 2,
    java_api_version = 2,
    js_api_version = 2,
    js_codegen = "jspb",
    visibility = ["//visibility:public"],
)

tf_proto_library(
    name = "protos_test",
    srcs = ["util/example_proto_fast_parsing_test.proto"],
    cc_api_version = 2,
    protodeps = [":protos_all"],
    visibility = ["//visibility:public"],
)

# Minimal lib so that tools used for mobile compilation
# don't have to depend on lib/platformlib.
cc_library(
    name = "lib_proto_parsing",
    srcs = glob(tf_additional_proto_srcs()) + tf_env_time_srcs(),
    hdrs = [
        "lib/core/errors.h",
        "lib/core/status.h",
        "lib/core/stringpiece.h",
        "lib/strings/numbers.h",
        "lib/strings/strcat.h",
        "platform/init_main.h",
        "platform/logging.h",
        "platform/macros.h",
        "platform/platform.h",
        "platform/protobuf.h",
        "platform/types.h",
    ] + glob(tf_additional_proto_hdrs()) + glob(tf_env_time_hdrs()),
    copts = tf_copts(),
    deps = [
        ":protos_all_cc",
        "//tensorflow/core/platform/default/build_config:proto_parsing",
    ],
)

cc_library(
    name = "lib",
    hdrs = [
        "lib/core/coding.h",
        "lib/core/errors.h",
        "lib/core/raw_coding.h",
        "lib/core/status.h",
        "lib/core/stringpiece.h",
        "lib/core/threadpool.h",
        "lib/gtl/array_slice.h",
        "lib/gtl/flatmap.h",
        "lib/gtl/inlined_vector.h",
        "lib/hash/crc32c.h",
        "lib/io/buffered_inputstream.h",
        "lib/io/compression.h",
        "lib/io/inputstream_interface.h",
        "lib/io/path.h",
        "lib/io/random_inputstream.h",
        "lib/io/record_reader.h",
        "lib/io/record_writer.h",
        "lib/strings/numbers.h",
        "lib/strings/str_util.h",
        "lib/strings/strcat.h",
        "lib/strings/stringprintf.h",
        "platform/cpu_info.h",
        "platform/dynamic_annotations.h",
        "platform/env.h",
        "platform/env_time.h",
        "platform/file_system.h",
        "platform/init_main.h",
        "platform/logging.h",
        "platform/macros.h",
        "platform/mem.h",
        "platform/mutex.h",
        "platform/net.h",
        "platform/notification.h",
        "platform/prefetch.h",
        "platform/profile_utils/clock_cycle_profiler.h",
        "platform/profile_utils/cpu_utils.h",
        "platform/protobuf.h",
        "platform/strong_hash.h",
        "platform/subprocess.h",
        "platform/thread_annotations.h",
        "platform/types.h",
        "platform/windows/cpu_info.h",
        "util/events_writer.h",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":lib_internal",
    ],
)

# Test support library needed for all tests
# This is currently public, but may be made internal in the
# future.  Try to avoid depending on it.
cc_library(
    name = "test",
    testonly = 1,
    srcs = [
        "platform/test.cc",
        "util/reporter.cc",
    ] + tf_additional_test_srcs(),
    hdrs = [
        "lib/core/status_test_util.h",
        "platform/test.h",
        "platform/test_benchmark.h",
        "util/reporter.h",
    ],
    copts = tf_copts(),
    linkopts = ["-lm"],
    visibility = ["//visibility:public"],
    deps = [
        ":lib",
        ":lib_internal",
        "//tensorflow/core/platform/default/build_config:gtest",
    ] + tf_additional_test_deps(),
)




# And one for all user ops







# Test support library needed for higher-level (TensorFlow-specific) tests

# This is a link-only library to provide a DirectSession
# implementation of the Session interface.

# -----------------------------------------------------------------------------
# Public Android targets

# Android-specific BUILD targets

# List of protos we want on android


# -----------------------------------------------------------------------------
# Libraries with GPU facilities that are useful for writing kernels.

# -----------------------------------------------------------------------------
# Internal targets


cc_library(
    name = "lib_internal",
    srcs = select({
        "//tensorflow:windows": glob(
            [
                "lib/**/*.h",
                "lib/**/*.cc",
                "platform/*.h",
                "platform/*.cc",
                "util/*.h",
                "util/*.cc",
            ],
            exclude = [
                "**/*test*",
                "lib/hash/crc32c_accelerate.cc",
                "lib/gif/**/*",
                "lib/jpeg/**/*",
                "platform/gif.h",
                "platform/jpeg.h",
                "platform/**/env_time.cc",
                "platform/**/cuda.h",
                "platform/**/cuda_libdevice_path.cc",
                "platform/**/stream_executor.h",
                "platform/load_library.cc",
            ],
        ),
        "//conditions:default": glob(
            [
                "lib/**/*.h",
                "lib/**/*.cc",
                "platform/*.h",
                "platform/*.cc",
                "platform/profile_utils/**/*.h",
                "platform/profile_utils/**/*.cc",
                "util/*.h",
                "util/*.cc",
            ],
            exclude = [
                "**/*test*",
                "lib/hash/crc32c_accelerate.cc",
                "lib/gif/**/*",
                "lib/jpeg/**/*",
                "platform/gif.h",
                "platform/jpeg.h",
                "platform/**/env_time.cc",
                "platform/**/cuda.h",
                "platform/**/cuda_libdevice_path.cc",
                "platform/**/stream_executor.h",
            ],
        ),
    }) + tf_additional_lib_srcs(
        exclude = [
            "**/*test*",
            "platform/**/cuda.h",
            "platform/**/cuda_libdevice_path.cc",
            "platform/**/stream_executor.h",
            "platform/**/env_time.cc",
        ] +
        # Protobuf deps already included through the ":lib_proto_parsing"
        # dependency.
        tf_additional_proto_srcs(),
    ),
    hdrs = tf_additional_lib_hdrs() + [
        "lib/gtl/manual_constructor.h",
        "lib/gtl/map_util.h",
        "lib/gtl/stl_util.h",
        "lib/hash/hash.h",
        "lib/io/snappy/snappy_outputbuffer.h",
        "lib/io/zlib_compression_options.h",
        "lib/io/zlib_inputstream.h",
        "lib/io/zlib_outputbuffer.h",
        "lib/strings/scanner.h",
        "lib/random/random.h",
        "platform/demangle.h",
        "platform/denormal.h",
        "platform/host_info.h",
        "platform/platform.h",
        "platform/protobuf_internal.h",
        "platform/setround.h",
        "platform/tracing.h",
    ],
    copts = tf_copts(),
    defines = tf_additional_lib_defines(),
    linkopts = select({
        "//tensorflow:freebsd": [],
        "//conditions:default": ["-ldl"],
    }),
    deps = tf_additional_lib_deps() + [
        ":lib_hash_crc32c_accelerate_internal",
        ":lib_proto_parsing",
        ":protos_all_cc",
        "//third_party/eigen3",
        "//tensorflow/core/platform/default/build_config:platformlib",
        "@zlib_archive//:zlib",
    ],
)

# File compiled with extra flags to get cpu-specific acceleration.
cc_library(
    name = "lib_hash_crc32c_accelerate_internal",
    srcs = ["lib/hash/crc32c_accelerate.cc"],
    # -msse4.2 enables the use of crc32c compiler builtins.
    copts = tf_copts() + if_x86(["-msse4.2"]),
)


tf_version_info_genrule()

cc_library(
    name = "version_lib",
    srcs = ["util/version_info.cc"],
    hdrs = ["public/version.h"],
    copts = tf_copts(),
)

# TODO(josh11b): Is this needed, or can we just use ":protos_all"?
cc_library(
    name = "protos_cc",
    deps = ["//tensorflow/core/platform/default/build_config:protos_cc"],
)


# This library is deprecated and no longer publicly available.
# Do not add more uses of it.
# -----------------------------------------------------------------------------
# Tests

# cc_library(
#     name = "lib_test_internal",
#     testonly = 1,
#     hdrs = [
#         "lib/gtl/manual_constructor.h",
#         "lib/io/block.h",
#         "lib/io/block_builder.h",
#         "lib/io/format.h",
#         "lib/random/philox_random_test_utils.h",
#         "platform/snappy.h",
#     ],
#     deps = [":lib_internal"],
# )



# # Main program for tests
# cc_library(
#     name = "test_main",
#     testonly = 1,
#     srcs = ["platform/test_main.cc"],
#     copts = tf_copts(),
#     linkopts = ["-lm"],
#     visibility = ["//tensorflow:internal"],
#     deps = [
#         ":lib",
#         ":lib_internal",
#         ":test",
#         "//tensorflow/core/platform/default/build_config:test_main",
#     ],
#     alwayslink = 1,
# )

# tf_cc_tests(
#     name = "low_level_library_tests",
#     size = "small",
#     srcs = [
#         "lib/core/arena_test.cc",
#         "lib/core/bit_cast_test.cc",
#         "lib/core/bitmap_test.cc",
#         "lib/core/blocking_counter_test.cc",
#         "lib/core/coding_test.cc",
#         "lib/core/notification_test.cc",
#         "lib/core/refcount_test.cc",
#         "lib/core/status_test.cc",
#         "lib/core/stringpiece_test.cc",
#         "lib/core/threadpool_test.cc",
#         "lib/gtl/array_slice_test.cc",
#         "lib/gtl/cleanup_test.cc",
#         "lib/gtl/edit_distance_test.cc",
#         "lib/gtl/flatmap_test.cc",
#         "lib/gtl/flatset_test.cc",
#         "lib/gtl/inlined_vector_test.cc",
#         "lib/gtl/int_type_test.cc",
#         "lib/gtl/iterator_range_test.cc",
#         "lib/gtl/manual_constructor_test.cc",
#         "lib/gtl/map_util_test.cc",
#         "lib/gtl/top_n_test.cc",
#         "lib/hash/crc32c_test.cc",
#         "lib/hash/hash_test.cc",
#         "lib/histogram/histogram_test.cc",
#         "lib/io/buffered_inputstream_test.cc",
#         "lib/io/inputbuffer_test.cc",
#         "lib/io/inputstream_interface_test.cc",
#         "lib/io/path_test.cc",
#         "lib/io/random_inputstream_test.cc",
#         "lib/io/record_reader_writer_test.cc",
#         "lib/io/recordio_test.cc",
#         "lib/io/snappy/snappy_buffers_test.cc",
#         "lib/io/table_test.cc",
#         "lib/io/zlib_buffers_test.cc",
#         "lib/math/math_util_test.cc",
#         "lib/monitoring/collection_registry_test.cc",
#         "lib/monitoring/counter_test.cc",
#         "lib/monitoring/metric_def_test.cc",
#         "lib/monitoring/sampler_test.cc",
#         "lib/random/distribution_sampler_test.cc",
#         "lib/random/philox_random_test.cc",
#         "lib/random/random_distributions_test.cc",
#         "lib/random/random_test.cc",
#         "lib/random/simple_philox_test.cc",
#         "lib/strings/base64_test.cc",
#         "lib/strings/numbers_test.cc",
#         "lib/strings/scanner_test.cc",
#         "lib/strings/str_util_test.cc",
#         "lib/strings/strcat_test.cc",
#         "lib/strings/stringprintf_test.cc",
#         "lib/wav/wav_io_test.cc",
#         "platform/fingerprint_test.cc",
#         "platform/integral_types_test.cc",
#         "platform/logging_test.cc",
#         "platform/net_test.cc",
#         "platform/port_test.cc",
#         "platform/profile_utils/cpu_utils_test.cc",
#         "platform/subprocess_test.cc",
#     ],
#     deps = [
#         ":lib",
#         ":lib_internal",
#         ":lib_test_internal",
#         ":protos_all_cc",
#         ":test",
#         ":test_main",
#         "//third_party/eigen3",
#     ],
# )

# tf_cc_test(
#     name = "platform_env_test",
#     size = "small",
#     srcs = ["platform/env_test.cc"],
#     deps = [
#         ":lib",
#         ":lib_internal",
#         ":lib_test_internal",
#         ":protos_all_cc",
#         ":test",
#         ":test_main",
#         "//third_party/eigen3",
#     ],
# )

# tf_cc_test(
#     name = "platform_setround_test",
#     size = "small",
#     srcs = ["platform/setround_test.cc"],
#     tags = [
#         "noasan",
#         "nomsan",
#         "notsan",
#     ],
#     deps = [
#         ":lib",
#         ":lib_internal",
#         ":lib_test_internal",
#         ":test",
#         ":test_main",
#     ],
# )

# tf_cc_test(
#     name = "platform_file_system_test",
#     size = "small",
#     srcs = ["platform/file_system_test.cc"],
#     deps = [
#         ":lib",
#         ":lib_internal",
#         ":lib_test_internal",
#         ":protos_all_cc",
#         ":test",
#         ":test_main",
#     ],
# )



# cc_test(
#     name = "lib_strings_ordered_code_test",
#     srcs = ["lib/strings/ordered_code_test.cc"],
#     copts = ["$(STACK_FRAME_UNLIMITED)"],  # Tests initialize large vectors
#     deps = [
#         ":lib",
#         ":lib_internal",
#         ":test",
#         ":test_main",
#     ],
# )







# -----------------------------------------------------------------------------
# Google-internal targets go here (must be at the end).

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
