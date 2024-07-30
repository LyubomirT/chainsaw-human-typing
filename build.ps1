$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

pyinstaller --noconfirm --onedir --windowed --icon "$scriptDir\src\img.ico" --add-data "$scriptDir\src\logo.png;." --add-data "$scriptDir\src\style.css;."  "$scriptDir\src\main.py"



# Copy the logo.png and style.css to the dist/main folder
Copy-Item -Path "$scriptDir\src\logo.png" -Destination "$scriptDir\dist\main"
Copy-Item -Path "$scriptDir\src\style.css" -Destination "$scriptDir\dist\main"
Copy-Item -Path "$scriptDir\src\darkmode.css" -Destination "$scriptDir\dist\main"

# Copy the translations folder to the dist/main folder
Copy-Item -Path "$scriptDir\src\translations" -Destination "$scriptDir\dist\main" -Recurse

# Delete the build folder
Remove-Item -Path "$scriptDir\build" -Recurse

# Delete the spec file
Remove-Item -Path "$scriptDir\main.spec"