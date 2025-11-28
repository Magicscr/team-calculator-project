# Инструкция сборки DEB пакета
# Практическая работа 4

## Сборка пакета:
dpkg-deb --build deb-package

## Установка:
sudo dpkg -i deb-package.deb

## Запуск:
py-calculator-team

## Структура пакета:
deb-package/
├── DEBIAN/
│   ├── control
│   ├── postinst
│   └── prerm
└── usr/
   ├── local/bin/py-calculator-team
 └── share/py-calculator-team/README.md
