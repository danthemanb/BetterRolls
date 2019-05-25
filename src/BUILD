# src package
package(default_visibility = ["//visibility:public"])

load("@pip//:requirements.bzl", "requirement")

py_binary(
	name = "BetterRollsBot",
	srcs = ["BetterRollsBot.py"],
	deps = [
		"//src/BetterRolls:GodlikeRoll",
		requirement("discord.py"),
		requirement("aiohttp"),
		requirement("websockets"),
		requirement("yarl"),
		requirement("async-timeout"),
		requirement("attrs"),
		requirement("chardet"),
		requirement("multidict"),
		requirement("idna"),
	],
	srcs_version = "PY3",
	default_python_version = "PY3",
)
