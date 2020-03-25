:title: PyQt5 - Einstieg
:data-transition-duration: 1500
:css: hovercraft.css


----

PyQT5
=====
(My) Best Practices

Robert Lieback - Element-Digital / Euratel

----

Was ist PyQt?
=============
* Pythonwrapper für Qt5
* Qt5:
    * Mehr als nur GUI-Framework
    * Komplette crossplattform Anwendungsentwicklung
    * GUI, Network, Multimedia, SQL, ...
    * Für Windows, Linux, Mac, Android, iOS, ...
    * Entwickelt in C++
    * Wrapper für alle relevanten Sprachen

----

GUI-Design-Beispiel
===================

1. Installation von benötigten Tools
2. Erstellen eines UI-Files in Qt-Creator
3. Wandeln des UI-Files in Python-Code
4. Eventhandling erstellen
5. Executable erstellen

----

Installation von benötigten Tools
=================================

    > pip install PyQt5 PyInstaller

Empfohlen:

    Qt Creator als GUI-Editor https://www.qt.io/download

Optional:

    > pip install PyInstaller

    # Derzeit pip install https://github.com/pyinstaller/pyinstaller/tarball/develop

Zur Hand haben:

    http://doc.qt.io/qt-5/qtwidgets-index.html

----

Erstellen eines UI-Files in Qt-Creator
======================================

* Neu > Qt > Qt-Designerformular
* Widget in Layout ziehen und Layouts eine Ausrichtung verpassen
* Python-Code generieren:

    pyuic5 -x -o file.py file.ui

    -x: Erstellen eines Eventloops zur Vorschau

----

Eventhandling erstellen
=======================

* Klasse die von dem generierten Fenster erbt
    * im __init__ wird setupUI aufgerufen
* QApplication erstellen und starten. Qt übernimmt von hier aus komplett.

.. code:: python

    sys.exit(app.exec_())


* Signals und Slots:
    * Widgets emitieren Signals
    * Slots empfangen diese
* PyQt: Slots über Funktionsnamen zuordnen

.. code:: python

    @pyqtSlot()  # Als Slot definieren
    def on_pushButton_clicked(self):  # Funktion nach Muster: on_Wigetname_event(self):
        print("Button 1 clicked")

----

Erstellen von Executables mit PyInstaller
=========================================

    > pyinstaller --onefile app.py

--onefile: Packt alles in eine Executable statt vieler Files

Erstellt eine Executable in ./dist/app.exe

----

Smartscreenfilter
=================

* Wird bei unsignierten und unbekannten Anwendungen/Installern gezeigt
* Codesigning:
    * EV Code Signing Zertifikate
    * 300 - 500 € im Jahr
    * https://www.globalsign.com/de-de/code-signing/ev-code-signing-zertifikate/

----

Lizenz
======

* Qt: LGPL3 - Closed Source möglich
* PyQt: GPL3 oder proprietät - (veröffentlichte) Closed Source Software muss Lizenz kaufen.
    * 450€ pro Developer

----

ENDE
====
