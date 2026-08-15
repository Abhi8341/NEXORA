[app]

# --------------------------------
# NEXORA APP
# --------------------------------

title = NEXORA

package.name = nexora

package.domain = org.nexora

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,xml

source.exclude_dirs = .buildozer,bin,venv,__pycache__,.git

version = 1.0.0


# --------------------------------
# PYTHON REQUIREMENTS
# --------------------------------

requirements = python3,kivy,requests


# --------------------------------
# SCREEN
# --------------------------------

orientation = portrait

fullscreen = 0


# --------------------------------
# ANDROID
# --------------------------------

android.accept_sdk_license = True

android.api = 35

android.minapi = 23

android.ndk = 28c

android.ndk_api = 23

android.archs = arm64-v8a,armeabi-v7a

android.private_storage = True


# --------------------------------
# INTERNET
# --------------------------------

android.permissions = INTERNET


# --------------------------------
# ANDROID ENTRY POINT
# --------------------------------

android.entrypoint = org.kivy.android.PythonActivity


# --------------------------------
# ANDROID BACKGROUND
# --------------------------------

android.allow_backup = True


# --------------------------------
# BUILD SETTINGS
# --------------------------------

android.skip_update = False

android.copy_libs = 1


# --------------------------------
# VERSION
# --------------------------------

# If main.py contains:
# __version__ = "1.0.0"
# you can use automatic version detection instead.
#
# For now, the fixed version above is used.


# --------------------------------
# BUILD DIRECTORY
# --------------------------------

[buildozer]

log_level = 2

warn_on_root = 0

build_dir = ./.buildozer

bin_dir = ./bin