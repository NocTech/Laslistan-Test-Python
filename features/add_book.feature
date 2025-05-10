Feature: Lägg till bok funktionalitet
  Som användare
  Vill jag kunna lägga till egna böcker
  Så att jag kan inkludera böcker som inte redan finns i katalogen

  Background:
    Given användaren har öppnat Läslistan
    And användaren har navigerat till Lägg till bok

  @smoke
  Scenario: Visa formulär för att lägga till bok
    Given användaren har öppnat Läslistan
    And användaren har navigerat till Lägg till bok
    Then ska användaren se ett formulär med fält för titel, författare

  Scenario: Lägga till en ny bok
    When användaren fyller i följande bokuppgifter:
      | titel       | författare      |
      | Min Testbok | Test Författare | 
    And användaren klickar på knappen " Lägg till ny bok "
    When användaren navigerar till " Katalog "
    Then ska boken "Min Testbok" finnas i katalogen

  Scenario: Försöka lägga till en bok utan titel
    When användaren fyller i följande bokuppgifter:
      | titel | författare      | 
      |       | Test Författare |
    Then ska knappen vara inaktiv " Lägg till ny bok "

  Scenario: Försöka lägga till en bok utan författare
    When användaren fyller i följande bokuppgifter:
      | titel       | författare | 
      | Min Testbok |            | 
   Then ska knappen vara inaktiv " Lägg till ny bok "


