cd elevenclock
rmdir /Q /S build
rmdir /Q /S dist
python -m PyInstaller __init__.py --icon "resources/icon.ico" --add-binary "*.py;." --add-data "resources;resources" --add-data "lang;lang" --onefile --windowed --clean --version-file ../elevenclock-version-info
rem --add-data "%homedrive%%homepath%\AppData\Local\Programs\Python\Python39\Lib\site-packages\PySide6\plugins;PySide6/plugins"
cd dist
move __init__.exe ../../
cd ..
rmdir /Q /S build
rmdir /Q /S dist
del __init__.spec
cd ..
taskkill /im ElevenClock.exe /f
del ElevenClock.exe
rename __init__.exe ElevenClock.exe
ElevenClock.exe
pause
