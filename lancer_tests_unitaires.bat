@echo off
echo =============================================
echo      LANCEMENT DES TESTS UNITAIRES
echo =============================================

rem Vérifie que le dossier existe
if not exist "tests_unitaires" (
    echo ERREUR : dossier tests_unitaires introuvable !
    exit /b 1
)

echo Execution des tests unitaires...

python -m unittest discover -v tests_unitaires

rem Sauvegarde du code retour
set RESULT=%ERRORLEVEL%

if %RESULT% neq 0 (
    echo.
    echo CERTAINS TESTS UNITAIRES ONT ECHOUE !
    exit /b %RESULT%
) else (
    echo.
    echo TOUS LES TESTS UNITAIRES SONT PASSES AVEC SUCCES !
)