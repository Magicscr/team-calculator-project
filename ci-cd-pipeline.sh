#!/bin/bash
# CI/CD Script for Python Calculator Team
# Practical work 5.1

# Check parameters as in the example
if [ -z "" ]; then
    echo "First parameter not provided - path to source directory";
    exit 1
fi

if [ -z "" ]; then
    echo "Second parameter not provided - project version";
    exit 1
fi

srcdir=;
version=;
inputname=;

echo "================================================"
echo "CI/CD SCRIPT FOR PYTHON CALCULATOR TEAM"
echo "Version: "
echo "Directory: "
echo "================================================"

# 1. Download current state from server
echo "1. DOWNLOADING CURRENT STATE..."
cd ""
git fetch origin
git pull origin main
echo "Current state downloaded"

# 2. Project build and unittest build
echo "2. PROJECT BUILD..."
python --version
echo "Project ready for testing"

# 3. Unittest execution
echo "3. EXECUTING UNITTESTS..."
python -m unittest test_calculator.py -v

if [ True -eq 0 ]; then
    echo "TESTS PASSED SUCCESSFULLY"
else
    echo "TESTS FAILED"
    exit 1
fi

# 4. Installer creation
echo "4. CREATING INSTALLER..."
if command -v dpkg-deb &> /dev/null; then
    dpkg-deb --build deb-package
    echo "DEB package created: deb-package.deb"
else
    echo "dpkg-deb not found, creating archive..."
    tar -czf python-calculator-team-v.tar.gz --exclude-vcs --exclude='__pycache__' .
    echo "Archive created: python-calculator-team-v.tar.gz"
fi

# 5. Application installation
echo "5. INSTALLING APPLICATION..."
if [ -f "deb-package.deb" ] && command -v dpkg &> /dev/null; then
    echo "Installing DEB package..."
    sudo dpkg -i deb-package.deb
    echo "Application installed"
    echo "Run: py-calculator-team"
else
    echo "Installation completed (simulation)"
    echo "Run: python calculator.py"
fi

echo "================================================"
echo "CI/CD PROCESS COMPLETED SUCCESSFULLY!"
echo "Version: "
echo "================================================"
