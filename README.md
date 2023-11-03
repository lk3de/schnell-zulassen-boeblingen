# schnell-zulassen-boeblingen

## Ausgangslage

Termine bei den Kfz-Zulassungsstellen in Böblingen sind sehr rar. Die Vergabe läuft über ein Online-Terminsystem des Dienstleisters [SMART CJM GmbH](https://smart-cjm.com/), bei dem es nur mit viel Geduld und ständigem Aktualisieren der Seite möglich ist, einen Termin zu ergattern. Einen recht guten Eindruck der aktuellen Situation bieten die Rezensionen des [Google Maps Eintrags](https://maps.app.goo.gl/zZtAXxmqx4MxUcCi9) der Zulassungsstelle Böblingen.

## Die Lösung

Um schneller an einen Termin zu gelangen, suchen wir mithilfe von Selenium automatisiert nach freien Terminen und schlagen Alarm, sobald es einen freien Termin gibt.

## Setup

- Dependencies installieren: `pip3 install -r requirements.txt`
- Script starten: `python3 checker.py`

## Credits

- [schnell-zulassen-guetersloh](https://github.com/thoughtgap/schnell-zulassen-guetersloh) für die Inspiration beim Naming
