pyinstaller -F --onefile main.pyw --noconsole -i main.ico

md dist\qml
xcopy qml dist\qml /y /e