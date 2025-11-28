@echo off
echo ================================================
echo CI/CD SCRIPT FOR PYTHON CALCULATOR TEAM
echo Version: %2
echo Directory: %1
echo ================================================

REM 1. Download current state from server
echo 1. DOWNLOADING CURRENT STATE...
git fetch origin
git pull origin main
echo Current state downloaded

REM 2. Project build and unittest build
echo 2. PROJECT BUILD...
py --version
echo Project ready for testing

REM 3. Unittest execution
echo 3. EXECUTING UNITTESTS...
py -m unittest test_calculator.py -v

if %errorlevel% equ 0 (
    echo TESTS PASSED SUCCESSFULLY
) else (
    echo TESTS FAILED
    exit /b 1
)

REM 4. Installer creation
echo 4. CREATING INSTALLER...
echo DEB package structure already created in deb-package/
echo For build: dpkg-deb --build deb-package
echo Archive simulation completed

REM 5. Application installation
echo 5. INSTALLING APPLICATION...
echo Installation completed (simulation)
echo Run: python calculator.py

echo ================================================
echo CI/CD PROCESS COMPLETED SUCCESSFULLY!
echo Version: %2
echo ================================================
