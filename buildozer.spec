[app]

title = NEXORA Public
package.name = nexorapublic
package.domain = org.nexora

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 3.3

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1