#!/bin/bash

# Get the directory of the current script
scriptDir="$(dirname "$(readlink -f "$0")")"

# Build the executable using PyInstaller
pyinstaller --noconfirm --onedir --windowed --icon "$scriptDir/src/img.ico" --add-data "$scriptDir/src/logo.png:." --add-data "$scriptDir/src/style.css:." "$scriptDir/src/main.py"

# Copy the logo.png, style.css, and darkmode.css to the dist/main folder
cp "$scriptDir/src/logo.png" "$scriptDir/dist/main/"
cp "$scriptDir/src/style.css" "$scriptDir/dist/main/"
cp "$scriptDir/src/darkmode.css" "$scriptDir/dist/main/"

# Copy the translations folder to the dist/main folder
cp -r "$scriptDir/src/translations" "$scriptDir/dist/main/"

# Delete the build folder
rm -rf "$scriptDir/build"

# Delete the spec file
rm "$scriptDir/main.spec"
