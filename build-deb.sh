#!/bin/bash
# Скрипт сборки DEB пакета
echo "Сборка DEB пакета..."
dpkg-deb --build deb-package
echo "Пакет собран: deb-package.deb"
