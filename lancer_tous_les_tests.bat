@echo off
echo =============================================
echo LANCEMENT DE TOUS LES TESTS
echo =============================================

rem ===== Tests unitaires =====
call lancer_tests_unitaires.bat
if errorlevel 1 (
    echo.
    echo ERREUR : ECHEC DES TESTS UNITAIRES
    exit /b 1
)

rem ===== Tests API =====
call lancer_tests_api.bat
if errorlevel 1 (
    echo.
    echo ERREUR : ECHEC DES TESTS API
    exit /b 1
)

rem ===== Tests IHM =====
call lancer_tests_ihm.bat
if errorlevel 1 (
    echo.
    echo ERREUR : ECHEC DES TESTS IHM
    exit /b 1
)

echo.
echo =============================================
echo TOUS LES TESTS SONT PASSES AVEC SUCCES
echo =============================================

pause