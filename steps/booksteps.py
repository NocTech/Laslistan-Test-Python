from pages.base_page import BasePage
from pages.add_book_page import AddBookPage
from behave import then, given, when


@then('ska användaren se välkomstmeddelandet "{message}"')
def step_assert_welcome_message(context, message):
    """Verifierar att ett välkomstmeddelande visas."""
    base_page = BasePage(context.page)
    actual_message = base_page.get_text("h1")
    assert message in actual_message, f"Förväntat meddelande '{message}' men fick '{actual_message}'"


@given('användaren har öppnat Läslistan')
def step_open_website(context):
    """Öppnar webbsidan."""
    base_page = BasePage(context.page)
    base_page.navigate()


@then('ska användaren se navigationslänkar för "{link1}", "{link2}" och "{link3}"')
def step_assert_navigation_links(context, link1, link2, link3):
    """
    Verifierar att navigationslänkar visas.
    Args:
        link1, link2, link3 (str): Förväntade navigationslänkar
    """
    base_page = BasePage(context.page)
    for link in [link1, link2, link3]:
        is_visible = base_page.is_visible(f"text={link}")
        assert is_visible, f"Navigationslänken '{link}' är inte synlig"


@given('användaren har navigerat till {page_name}')
def step_navigate_to_page(context, page_name):
    """
    Navigerar till en specifik sida.
    Args:
        page_name (str): Namnet på sidan att navigera till
    """
    print(f"Navigating to {page_name}")
    base_page = BasePage(context.page)
    base_page.navigate_to_menu_item(page_name)
    context.current_page = page_name.lower()


@then('ska användaren se ett formulär med fält för titel, författare')
def step_assert_form_fields_visible(context):
    """Verifierar att formuläret har fält för titel, författare"""
    add_book_page = AddBookPage(context.page)
    has_inputs = add_book_page.has_form_inputs()
    assert has_inputs, "Formuläret har inte alla förväntade fält"


@when('användaren fyller i följande bokuppgifter')
def step_fill_book_form(context):
    """
    Fyller i formuläret för att lägga till en bok baserat på en tabell i feature-filen.
    """
    add_book_page = AddBookPage(context.page)
    row = context.table[0]
    context.book_title = row['titel']
    add_book_page.fill_book_form(
        row['titel'],
        row['författare']
    )


@when('användaren klickar på knappen "{button_text}"')
def step_click_button(context, button_text):
    """
    Klickar på en knapp med specifik text.
    Args:
        button_text (str): Texten på knappen att klicka på
    """
    selector = f"button:has-text('{button_text.strip()}')"  # Ensure proper text matching
    context.page.click(selector)


@when('användaren navigerar till {page_name}')
def step_navigate_to_page_when(context, page_name):
    """
    Navigerar till en specifik sida.
    Args:
        page_name (str): Namnet på sidan att navigera till
    """
    base_page = BasePage(context.page)
    base_page.navigate_to_menu_item(page_name)
    context.current_page = page_name.lower()


@then('ska boken "{book_title}" finnas i katalogen')
def step_assert_book_in_catalog(context, book_title):
    """
    Verifierar att en specifik bok finns i katalogen.
    Args:
        book_title (str): Titeln på boken att leta efter
    """
    base_page = BasePage(context.page)
    is_in_catalog = base_page.is_book_in_catalog(book_title)
    assert is_in_catalog, f"Boken '{book_title}' finns inte i katalogen"


@then('ska knappen vara inaktiv "{button_text}"')
def step_assert_button_disabled(context, button_text):
    """
    Verifierar att en knapp med specifik text är inaktiv (disabled).
    Args:
        button_text (str): Texten på knappen att kontrollera
    """
    selector = f"button:has-text('{button_text.strip()}')"  # Ensure proper text matching
    # Check if the button has the 'disabled' attribute
    is_disabled = context.page.get_attribute(selector, "disabled")
    assert is_disabled is not None, f"Knappen '{button_text}' är inte inaktiv"


@then('ska användaren se en lista med böcker')
def step_assert_books_visible(context):
    """
    Verifierar att en lista med böcker visas.
    """
    catalog_page = BasePage(context.page)
    books = catalog_page.get_list_of_books()
    assert books, "Inga böcker visas i listan"


@then('ska boken "{BOOK_TITLE}" inte längre visas i fliken "Mina böcker"')
def steg_ska_boken_inte_visas_i_minabocker(context, BOOK_TITLE):
    """
    Verifierar att en specifik bok inte längre visas i fliken "Mina böcker".
    """
    catalog_page = BasePage(context.page)
    is_in_catalog = catalog_page.is_book_in_catalog(BOOK_TITLE)
    assert not is_in_catalog, f"Boken '{BOOK_TITLE}' finns fortfarande i katalogen"


@given(u'att användaren är på startsidan')
def step_impl(context):
    """Verifierar att användaren är på startsidan."""
    base_page = BasePage(context.page)
    base_page.navigate_to_home_page()


@given(u'användaren för muspekaren över boken "{book_title}"')
def step_impl(context, book_title):
    """För muspekaren över en specifik bok."""
    catalog_page = BasePage(context.page)
    catalog_page.hover_over_book(book_title)


@given(u'användaren klickar på hjärtikonen för boken "{book_title}"')
def step_impl(context, book_title):
    """Klickar på hjärtikonen för en specifik bok."""
    catalog_page = BasePage(context.page)
    catalog_page.click_favorite_icon(book_title)


@then(u'ska boken "{book_title}" visas i fliken "Mina böcker"')
def step_impl(context, book_title):
    """Verifierar att en specifik bok visas i fliken 'Mina böcker'."""
    my_books_page = BasePage(context.page)
    is_in_my_books = my_books_page.is_book_in_my_books(book_title)
    assert is_in_my_books, f"Boken '{book_title}' visas inte i fliken 'Mina böcker'"


@given(u'boken "{book_title}" redan finns i fliken "Mina böcker"')
def step_impl(context, book_title):
    """Verifierar att en specifik bok redan finns i fliken 'Mina böcker'."""
    my_books_page = BasePage(context.page)
    is_in_my_books = my_books_page.is_book_in_my_books(book_title)
    assert is_in_my_books, f"Boken '{book_title}' finns inte i fliken 'Mina böcker'"


@when(u'användaren går till fliken "{navigate}"')
def step_impl(context, navigate):
    """Navigerar till en specifik flik."""
    base_page = BasePage(context.page)
    base_page.navigate_to_menu_item(navigate)


