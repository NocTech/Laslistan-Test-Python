# Läslistan - Testprojekt

Detta projekt innehåller automatiserade tester för webbapplikationen "Läslistan", en webbsida där användare kan välja och organisera böcker från en katalog samt lägga till egna böcker.

## Vad som testas

Följande funktionalitet testas i detta projekt:

1. **Grundläggande navigering**
   - Ladda startsidan
   - Navigera mellan olika vyer (Katalog, Min Läslista, Lägg till bok)

2. **Katalogfunktionalitet**
   - Visa katalog med böcker
   - Lägga till böcker från katalogen till Min Läslista

3. **Min Läslista-funktionalitet**
   - Visa böcker i Min Läslista

4. **Lägg till bok-funktionalitet**
   - Lägga till en ny bok med titel, författare och genre
   - Validering av formulärinmatning

## Projektstruktur

```
läslistan-testprojekt/
│
├── .github/Workflow/behave.yml  # Githib Action
├── features/              # Behave feature-filer
│   ├── add_book.feature
│   ├── catalog.feature
│   └── navigation.feature
│
├── steps/                 # Behave step-definitioner
│   └── booksteps.py
│
├── pages/                 # Page Objects
│   ├── add_book_page.py
│   └──  base_page.py
│
├── environment.py           # konfiguration
├── requirements.txt       # Projektberoenden
├── STORIES.md             # User stories
└── README.md              # Denna fil
```

## Hur man startar projektet

### Förutsättningar

- Python 3.8 eller senare
- pip (Pythons pakethanterare)

### Installation

1. Klona detta repository:
   ```bash
   git clone https://github.com/NocTech/Laslistan-Test-Python.git
   cd Laslistan-Test-Python
   ```

2. Skapa och aktivera en virtuell miljö (valfritt men rekommenderas):
   ```bash
   python -m venv venv
   
   # På Windows
   venv\Scripts\activate
   
   # På macOS/Linux
   source venv/bin/activate
   ```

3. Installera beroenden:
   ```bash
   pip install -r requirements.txt
   ```

4. Installera Playwright-webbläsare:
   ```bash
   playwright install
   ```

### Kör testerna

För att köra alla Behave-tester:
```bash
python -m behave
```

För att köra en specifik feature-fil:
```bash
behave features/catalog.feature
```

För att köra tester med tagg:
```bash
behave --tags=@smoke
```