# Игра «Виселица»

[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/AndruRus/E1_HW_gallows/master.png?style=flat-square

[build]: https://travis-ci.org/AndruRus/E1_HW_gallows


Приложение «загадывает» одно из следующих слов: skillfactory, testing, blackbox, pytest, unittest, coverage. И показывает количество букв в нём.

Игрок пытается угадать слово буква за буквой. Если человек называет букву, которой нет в слове, у него появляется штрафное очко. А если букву, которая есть в слове, то она открывается (и все её вхождения).

Реализованы тесты pytest, интегрированы с "Travis CI".

Запуск приложения

* Склонировать репозиторий:        

git clone https://github.com/AndruRus/E1_HW_gallows.git

* Активировать виртуальное окружение:  virtualenv venv

* Установить зависимости:  pip install -r requirements.txt

* Запустить приложение:  python .\gallows.py

* Запустить тесты:  python -m pytest

