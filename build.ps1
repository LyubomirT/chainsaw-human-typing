$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

pyinstaller --noconfirm --onedir --windowed --icon "$scriptDir\img.ico" --add-data "$scriptDir\logo.png;." --add-data "$scriptDir\style.css;."  "$scriptDir\main.py"

# Copy the logo.png and style.css to the dist/main folder
Copy-Item -Path "$scriptDir\logo.png" -Destination "$scriptDir\dist\main"
Copy-Item -Path "$scriptDir\style.css" -Destination "$scriptDir\dist\main"

# Copy the translations folder to the dist/main folder
Copy-Item -Path "$scriptDir\translations" -Destination "$scriptDir\dist\main" -Recurse

# Delete the build folder
Remove-Item -Path "$scriptDir\build" -Recurse

# Delete the spec file
Remove-Item -Path "$scriptDir\main.spec"