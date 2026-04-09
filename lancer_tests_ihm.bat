@echo off
rem ============================================
rem Script pour lancer les tests IHM avec Robot
rem ============================================

echo =============================================
echo        LANCEMENT DES TESTS IHM
echo =============================================

echo =============================
echo CONTENU DU PROJET :
dir
echo =============================

rem Vérifie que le dossier tests_ihm existe
if not exist "tests_ihm" (
    echo ERREUR : le dossier tests_ihm est introuvable !
    exit /b 1
)

echo =============================
echo CONTENU tests_ihm :
dir tests_ihm
echo =============================

rem Crée un dossier reports si nécessaire
if not exist "reports" (
    mkdir reports
)

echo Execution des tests Robot Framework...

rem Lancement des tests (UNE SEULE FOIS)
robot -d reports tests_ihm

rem Sauvegarde du code retour
set RESULT=%ERRORLEVEL%

rem Analyse du résultat
if %RESULT% neq 0 (
    echo.
    echo CERTAINS TESTS IHM ONT ECHOUE !
    echo Consultez reports\log.html et reports\report.html
    exit /b %RESULT%
) else (
    echo.
    echo TOUS LES TESTS IHM SONT PASSES AVEC SUCCES !
    echo Consultez reports\log.html et reports\report.html
)
