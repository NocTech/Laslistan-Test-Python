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

    def navigate_to_menu_item(self, menu_item):
        """
        Navigerar till en specifik menypost.
        Args:
            menu_item (str): Texten på menylänken att klicka på
        """
        self.page.click(f"text={menu_item}")

    def get_text(self, selector):
        """Gets text content from a selector."""
        return self.page.text_content(selector)

    def is_visible(self, selector):
        """Checks if an element is visible on the page."""
        return self.page.is_visible(selector)


    def navigate_to_menu_item(self, menu_item):
        """
        Navigerar till en specifik menypost.
        Args:
            menu_item (str): Texten på menylänken att klicka på
        """
        self.page.click(f"text={menu_item}")

    def get_list_of_books(self):
        """
        Hämtar en lista med böcker från sidan.
        Returnerar en lista med boktitlar count.
        """
        books = self.page.query_selector_all(".book")
        return len(books)

    def is_book_in_catalog(self, book_title):
        """Kontrollerar om en specifik bok finns i katalogen."""
        return self.page.is_visible(f"text={book_title}")
    
    def navigate_to_home_page(self):
        """Navigerar till startsidan."""
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

    def click_favorite_icon(self, book_title):
        """Klickar på hjärtikonen för en specifik bok."""
        page = self.page
        heart = page.get_by_test_id(f"star-{book_title}")
        heart.click()
        



