"""
Page object för Lägg till bok-sidan i Läslistan.
"""
from pages.base_page import BasePage


class AddBookPage(BasePage):
    """Page object för Lägg till bok-sidan."""

    def __init__(self, page):
        super().__init__(page)
        self.title_input_selector = "add-input-title"
        self.author_input_selector = "add-input-author"

    async def has_form_inputs(self):
        """
        Kontrollerar om formuläret har de förväntade inmatningsfälten.
        Returns:
            bool: True om alla förväntade fält finns, False annars
        """
        title_input = await self.page.query_selector(self.title_input_selector)
        author_input = await self.page.query_selector(self.author_input_selector)

        return title_input and author_input

    def fill_book_form(self, title, author):
        """Fyller i formuläret med titel och författare."""
        title_input = self.page.get_by_test_id("add-input-title")
        title_input.fill(title)

        author_input = self.page.get_by_test_id("add-input-author")
        author_input.fill(author)
