# TensorFlow external dependencies that can be loaded in WORKSPACE files.

load("@io_bazel_rules_closure//closure:defs.bzl", "filegroup_external")
load("@io_bazel_rules_closure//closure:defs.bzl", "webfiles_external")
load("//third_party/gpus:cuda_configure.bzl", "cuda_configure")
load("//third_party/sycl:sycl_configure.bzl", "sycl_configure")


# Parse the bazel version string from `native.bazel_version`.
def _parse_bazel_version(bazel_version):
  # Remove commit from version.
  version = bazel_version.split(" ", 1)[0]

  # Split into (release, date) parts and only return the release
  # as a tuple of integers.
  parts = version.split('-', 1)

  # Turn "release" into a tuple of strings
  version_tuple = ()
  for number in parts[0].split('.'):
    version_tuple += (str(number),)
  return version_tuple

# Check that a specific bazel version is being used.
def check_version(bazel_version):
  if "bazel_version" not in dir(native):
    fail("\nCurrent Bazel version is lower than 0.2.1, expected at least %s\n" % bazel_version)
  elif not native.bazel_version:
    print("\nCurrent Bazel is not a release version, cannot check for compatibility.")
    print("Make sure that you are running at least Bazel %s.\n" % bazel_version)
  else:
    current_bazel_version = _parse_bazel_version(native.bazel_version)
    minimum_bazel_version = _parse_bazel_version(bazel_version)
    if minimum_bazel_version > current_bazel_version:
      fail("\nCurrent Bazel version is {}, expected at least {}\n".format(
          native.bazel_version, bazel_version))
  pass

def _repos_are_siblings():
  return Label("@foo//bar").workspace_root.startswith("../")

# Temporary workaround to support including TensorFlow as a submodule until this
# use-case is supported in the next Bazel release.
def _temp_workaround_http_archive_impl(repo_ctx):
   repo_ctx.template("BUILD", repo_ctx.attr.build_file,
                     {
                         "%prefix%" : ".." if _repos_are_siblings() else "external",
                         "%ws%": repo_ctx.attr.repository
                     }, False)
   repo_ctx.download_and_extract(repo_ctx.attr.urls, "", repo_ctx.attr.sha256,
                                 "", repo_ctx.attr.strip_prefix)

temp_workaround_http_archive = repository_rule(
   implementation=_temp_workaround_http_archive_impl,
   attrs = {
      "build_file": attr.label(),
      "repository": attr.string(),
      "urls": attr.string_list(default = []),
      "sha256": attr.string(default = ""),
      "strip_prefix": attr.string(default = ""),
   })

# If TensorFlow is linked as a submodule.
# path_prefix and tf_repo_name are no longer used.
def tf_workspace(path_prefix = "", tf_repo_name = ""):
  cuda_configure(name = "local_config_cuda")
  sycl_configure(name = "local_config_sycl")
  if path_prefix:
    print("path_prefix was specified to tf_workspace but is no longer used and will be removed in the future.")
  if tf_repo_name:
    print("tf_repo_name was specified to tf_workspace but is no longer used and will be removed in the future.")

  native.new_http_archive(
      name = "eigen_archive",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/bitbucket.org/eigen/eigen/get/174e09eed96c.tar.gz",
          "https://bitbucket.org/eigen/eigen/get/174e09eed96c.tar.gz",
      ],
      sha256 = "38d4bda36435cd40e5235887cca8f108f8125d5a28eac471555efdf9d259020f",
      strip_prefix = "eigen-eigen-174e09eed96c",
      build_file = str(Label("//third_party:eigen.BUILD")),
  )
  
  native.new_http_archive(
      name = "pcre",
      sha256 = "ccdf7e788769838f8285b3ee672ed573358202305ee361cfec7a4a4fb005bbc7",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/ftp.exim.org/pub/pcre/pcre-8.39.tar.gz",
          "http://ftp.exim.org/pub/pcre/pcre-8.39.tar.gz",
      ],
      strip_prefix = "pcre-8.39",
      build_file = str(Label("//third_party:pcre.BUILD")),
  )

  native.new_http_archive(
      name = "six_archive",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz",
          "http://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz",
      ],
      sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
      strip_prefix = "six-1.10.0",
      build_file = str(Label("//third_party:six.BUILD")),
  )

  native.bind(
      name = "six",
      actual = "@six_archive//:six",
  )

  native.http_archive(
      name = "protobuf",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/github.com/google/protobuf/archive/ef927cc428db7bf41d3a593a16a8f1a0fe6306c5.tar.gz",
          "https://github.com/google/protobuf/archive/ef927cc428db7bf41d3a593a16a8f1a0fe6306c5.tar.gz",
      ],
      sha256 = "8813a4ab27f7c61565d0db17d69236b4ec0b1404371efc728f15079b85e457ca",
      strip_prefix = "protobuf-ef927cc428db7bf41d3a593a16a8f1a0fe6306c5",
  )

  native.new_http_archive(
      name = "gmock_archive",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/pkgs.fedoraproject.org/repo/pkgs/gmock/gmock-1.7.0.zip/073b984d8798ea1594f5e44d85b20d66/gmock-1.7.0.zip",
          "http://pkgs.fedoraproject.org/repo/pkgs/gmock/gmock-1.7.0.zip/073b984d8798ea1594f5e44d85b20d66/gmock-1.7.0.zip",
      ],
      sha256 = "26fcbb5925b74ad5fc8c26b0495dfc96353f4d553492eb97e85a8a6d2f43095b",
      strip_prefix = "gmock-1.7.0",
      build_file = str(Label("//third_party:gmock.BUILD")),
  )

  native.bind(
      name = "gtest",
      actual = "@gmock_archive//:gtest",
  )

  native.bind(
      name = "gtest_main",
      actual = "@gmock_archive//:gtest_main",
  )

  native.bind(
      name = "python_headers",
      actual = str(Label("//util/python:python_headers")),
  )

  native.new_http_archive(
      name = "swig",
      sha256 = "58a475dbbd4a4d7075e5fe86d4e54c9edde39847cdb96a3053d87cb64a23a453",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/ufpr.dl.sourceforge.net/project/swig/swig/swig-3.0.8/swig-3.0.8.tar.gz",
          "http://ufpr.dl.sourceforge.net/project/swig/swig/swig-3.0.8/swig-3.0.8.tar.gz",
          "http://pilotfiber.dl.sourceforge.net/project/swig/swig/swig-3.0.8/swig-3.0.8.tar.gz",
      ],
      strip_prefix = "swig-3.0.8",
      build_file = str(Label("//third_party:swig.BUILD")),
  )


  # grpc expects //external:protobuf_clib and //external:protobuf_compiler
  # to point to the protobuf's compiler library.
  native.bind(
      name = "protobuf_clib",
      actual = "@protobuf//:protoc_lib",
  )

  native.bind(
      name = "protobuf_compiler",
      actual = "@protobuf//:protoc_lib",
  )


  # TODO(phawkins): currently, this rule uses an unofficial LLVM mirror.
  # Switch to an official source of snapshots if/when possible.

  native.new_http_archive(
      name = "zlib_archive",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/zlib.net/zlib-1.2.8.tar.gz",
          "http://zlib.net/fossils/zlib-1.2.8.tar.gz",
      ],
      sha256 = "36658cb768a54c1d4dec43c3116c27ed893e88b02ecfcb44f2166f9c0b7f2a0d",
      strip_prefix = "zlib-1.2.8",
      build_file = str(Label("//third_party:zlib.BUILD")),
  )

  native.bind(
      name = "zlib",
      actual = "@zlib_archive//:zlib",
  )

  temp_workaround_http_archive(
      name = "jemalloc",
      urls = [
          "http://bazel-mirror.storage.googleapis.com/github.com/jemalloc/jemalloc/archive/4.4.0.tar.gz",
          "https://github.com/jemalloc/jemalloc/archive/4.4.0.tar.gz",
      ],
      sha256 = "3c8f25c02e806c3ce0ab5fb7da1817f89fc9732709024e2a81b6b82f7cc792a8",
      strip_prefix = "jemalloc-4.4.0",
      build_file = str(Label("//third_party:jemalloc.BUILD")),
      repository = tf_repo_name,
  )

  ##############################################################################
  # TensorBoard Build Tools
