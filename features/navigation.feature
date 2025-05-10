Feature: Navigering i applikationen
Som användare
Vill jag kunna navigera mellan olika delar av applikationen
Så att jag enkelt kan ta del av all funktionalitet

Background:
Given användaren har öppnat Läslistan

@smoke
Scenario: Visa startsidan
Then ska användaren se välkomstmeddelandet " Läslistan "
And ska användaren se navigationslänkar för " Katalog ", " Lägg till bok " och " Mina böcker"
