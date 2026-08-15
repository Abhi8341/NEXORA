[app]

title = NEXORA Public
package.name = nexora
package.domain = org.nexora

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0.0

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23

android.ndk = 28c
android.ndk_api = 23

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

android.private_storage = True

android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 0
