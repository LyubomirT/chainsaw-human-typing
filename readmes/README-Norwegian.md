# chainsaw-human-typing

Velkommen til chainsaw-human-typing-repositoriet! Chainsaw Human Typing er et verktøy som lar deg simulere menneskelig skriving på et tastatur hvis du ikke kan, eller ikke vil, lime inn direkte. Dette er nyttig for å simulere menneskelig skriving i en video, for eksempel.

## Komme i gang 🚀

Bare last ned en binær fra [releases](https://github.com/LyubomirT/chainsaw-human-typing/releases)-siden og kjør den. Du kan også bygge den selv ved å klone repositoriet og kjøre `python main.py`.

## Bruk 🛠

Det er ganske enkelt å bruke, faktisk! Bare skriv inn teksten du vil simulere skriving i inndatafeltet og trykk på "Start skriving"-knappen. Teksten vil bli skrevet ut i inndatafeltet nedenfor. Du kan se fremdriften i fremdriftslinjen.

## Kjør fra kildekode 🏗

For å kjøre prosjektet fra kildekode, må du ha Python 3.6 eller høyere installert. Du må også installere avhengighetene ved å kjøre `pip install -r requirements.txt`. Etter det, flytt til `src`-mappen og kjør `python main.py` for å kjøre prosjektet.

For å bygge prosjektet, kan du bruke PyInstaller. `build.ps1` er et PowerShell-skript som bygger prosjektet ved hjelp av PyInstaller. Du kan kjøre det ved å kjøre `.\build.ps1`. Utdataen vil være i `dist`-mappen, merk at skriptet er konfigurert for å bygge en Windows-eksekverbar fil og at du må ha PyInstaller installert.

## Bidra 🤝

Hvis du vil bidra til dette prosjektet, kan du gjerne forke det og sende en pull-forespørsel. Jeg vil gjerne gjennomgå den! Hvis du har spørsmål, kan du gjerne åpne en issue. Vennligst sjekk [CONTRIBUTING](CONTRIBUTING.md)-filen for mer informasjon.

## Lisens 📝

Dette prosjektet er lisensiert under GPL-3.0-lisensen - se [LICENSE](LICENSE)-filen for detaljer.

<!-- Acknowledgements -->

## Anerkjennelser 🙏

- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyInstaller](https://pypi.org/project/pyinstaller/)
- [PyNput](https://pypi.org/project/pynput/)