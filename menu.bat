@echo off
title PHIDS - Menu Principal
chcp 65001 >nul
cd /d "C:\Users\mathe\Desktop\new version phids"

echo [91m██████╗ ██╗  ██╗██╗██████╗ ███████╗
echo ██╔══██╗██║  ██║██║██╔══██╗██╔════╝
echo ██████╔╝███████║██║██║  ██║███████╗
echo ██╔═══╝ ██╔══██║██║██║  ██║╚════██║
echo ██║     ██║  ██║██║██████╔╝███████║
echo ╚═╝     ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝
echo [0m
echo.

echo 1 - Creer la page HTML
echo 2 - Lancer le serveur
echo 3 - Quitter
echo.

set /p choix="Choisissez une option : "

if "%choix%"=="1" goto creer_html
if "%choix%"=="2" goto lancer_serveur
if "%choix%"=="3" exit

:creer_html
(
echo ^<!DOCTYPE html^>
echo ^<html^>
echo ^<head^>
echo     ^<title^>PHIDS Login^</title^>
echo ^</head^>
echo ^<body^>
echo     ^<h1^>Connexion PHIDS^</h1^>
echo     ^<form^>
echo         ^<label for="username"^>Nom d'utilisateur : ^</label^>
echo         ^<input type="text" id="username" name="username"^>
echo         ^<br^>
echo         ^<label for="password"^>Mot de passe : ^</label^>
echo         ^<input type="password" id="password" name="password"^>
echo         ^<br^>
echo         ^<input type="submit" value="Se connecter"^>
echo     ^</form^>
echo ^</body^>
echo ^</html^>
) > phids_page.html

echo Page HTML cree avec succes !
pause
goto end

:lancer_serveur
echo Lancement du serveur...
python serveur.py
pause
goto end

:end
