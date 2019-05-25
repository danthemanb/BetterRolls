workspace(name = "BetterRollsBot")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "fdbb17a4118a1728d19e638a5291b4c4266ea5b8",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")

pip_import(
   name = "pip",
   requirements = "//:requirements.txt",
)

load("@pip//:requirements.bzl", "pip_install")
pip_install()

http_archive(
    name = "python_version",
    urls = ["https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz"],
    strip_prefix = "Python-3.7.3",
    build_file_content = """
genrule(
    name = "build_python",
    srcs = glob(["**"]),
    outs = ["python"],
    cmd = "./external/python_version/configure --enable-optimizations " +
	      "&& make " +
		  "&& cp python $@",
    visibility = ["//visibility:public"],
)""",
)
