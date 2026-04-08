@echo off
echo =============================================
echo        LANCEMENT DES TESTS API
echo =============================================

rem Vérifie que le dossier tests_API existe
if not exist "tests_API" (
    echo ERREUR : le dossier tests_API est introuvable !
    exit /b 1
)

rem Crée le dossier reports si nécessaire
if not exist "reports" (
    mkdir reports
)

cd tests_API

rem Lance tous les tests dans le dossier et ses sous-dossiers
robot -d ../reports .

rem Retour au dossier racine
cd ..

rem Gestion du code retour
if %ERRORLEVEL% neq 0 (
    echo.
    echo CERTAINS TESTS API ONT ECHOUE !
    exit /b 1
) else (
    echo.
    echo TOUS LES TESTS API SONT PASSES AVEC SUCCES !
)