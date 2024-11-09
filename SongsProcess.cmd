@echo off
setlocal enabledelayedexpansion

for %%F in (*_*_*.mp3) do (
    set "filename=%%~nF"
    set "extension=%%~xF"
    for /f "tokens=2 delims=_" %%a in ("!filename!") do set "foldername=%%a"
    for /f "tokens=3 delims=_" %%b in ("!filename!") do set "instrument=%%b"
    set "instrument=!instrument:~1,-1!"

    :: Convert to lowercase
    for %%i in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
        set "instrument=!instrument:%%i=%%i!"
    )

    :: Replace specific words
    set "instrument=!instrument:drums=drum!"
    set "instrument=!instrument:vocals=vocal!"
    
    set "newfilename=!instrument!!extension!"

    if not exist "!foldername!" (
        mkdir "!foldername!"
    )

    move "%%F" "!foldername!\!newfilename!"
)
