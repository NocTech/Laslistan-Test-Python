Feature: Katalogfunktionalitet
Som användare
Vill jag kunna utforska och interagera med katalogen
Så att jag kan hitta och välja böcker jag är intresserad av

Background:
Given användaren har öppnat Läslistan
# And användaren har navigerat till Katalog

@smoke
Scenario: Visa katalogen med böcker
Then ska användaren se en lista med böcker
# And ska varje bok visa titel, författare

Scenario: Användaren favoritmarkerar en bok och den visas i fliken "Mina böcker"
  Given att användaren är på startsidan
  And användaren klickar på hjärtikonen för boken "100 sätt att undvika måndagar"
  Then ska boken "100 sätt att undvika måndagar" visas i fliken "Mina böcker"
