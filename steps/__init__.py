"""
BasePage-objekt som alla sidor ärver från.
Innehåller gemensamma funktioner som används av alla sidor.
"""

class BasePage:
    """Basklass för alla page objects."""

    def __init__(self, page):
        """Initierar BasePage med en Playwright-page-instans."""
        self.page = page

    def navigate(self):
        """Navigerar till basadressen för webbapplikationen."""
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
