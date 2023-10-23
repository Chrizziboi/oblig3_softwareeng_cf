# oblig3_softwareeng_cf
For denne obligen gikk jeg inn i oblig2 på pycharm, satt opp en versionskontroll på github, 
pushet deretter opp hele oblig2 på et nytt repository.

Når det kom til å sette opp workflow actions, tok jeg å brukte python package workflow'en 
for å slippe å sette det opp helt fra bunnen.

i workflow filen byttet jeg et par ting:
 
 runs-on: windows-latest fra ubuntu.
 
tok dermed å byttet python-version: ["3.9"], fra flere, som var en feil jeg hadde gjort ved å 
velge package, for den er for flere versioner av python mens jeg trengte barefor en.

tok vekk if setning for om man skal installere avhengigheter eller ikke basert på 
om man har requirements.txt og endret den til å bare installere via requirements.txt uansett.
    
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest
        pip install -r requirements.txt

la til denne bulken med "kode":

    - name: Display Python version
      run: python -c "import sys; print(sys.version)"
    - name: Test with pytest
      run: echo " now testing all tests from the ${{ github.oblig3_softwareeng_cf }} repository"
    - run: pytest isLeapYear_tester.py
    
hvor det sjekker python sin version og printer versionen, og printer deretter at testen
er i ferd med å starte, som da til sist starter pytest på isLeapYear_tester.py og kjører
testene.

klarte å få til en rar ting der jeg hadde lagd en workflow først på main, og deretter pushet
oblig2 repo til det nye på github, som medførte til at jeg hadde fått en main branch og 
en master branch som jeg ikke kunne merge sammen, så koden min på master og workflow på main.

kopierte all kode fra master til main, og brukte checkout og rebase for å få alt sammen på
main branchen og slettet master. 
dermed fungerte alt som det skulle.
