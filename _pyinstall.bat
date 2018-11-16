pyinstaller -F --onefile main.pyw --noconsole -i main.ico

md dist\qml
xcopy qml dist\qml /y /e

md dist\force\mode
xcopy force\mode\*.txt dist\force\mode\ /y /e
