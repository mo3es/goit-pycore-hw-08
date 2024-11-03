from colorama import Fore

pattern_quit = {"exit", "quit", "close", "вихід", "вийти", "stop", "закрити"}
pattern_add = {"add", "plus", "append", "adding", "додати", "плюс"}
pattern_change = {"change", "змінити", "замінити"}
pattern_show = {
    "phone",
    "show",
    "look",
    "find",
    "give",
    "contact",
    "номер",
    "покажи",
    "показати",
    "знайти",
    "знайди",
    "дай",
    "контакт",
}
pattern_all = {
    "all",
    "show-all",
    "print-all",
    "print",
    "phone-book",
    "contacts",
    "list",
    "усі",
    "всі",
    "друк",
    "друкуй",
    "роздрукуй",
    "список",
    "перелік",
    "телефонна-книга",
    "контакти",
}
pattern_hello = {"hello", "hi", "привіт"}
pattern_add_birthday = {"add_birthday", "add-birthday", "додати_народження"}
pattern_show_birthday = {"show_birthday", "show-birthday", "день_народження"}
pattern_birthdays = {"birthdays", "all_birthdays", "усі_дні"}
pattern_add_phone = {'add_phone', 'another_phone', 'додати_номер'}

USAGE = f"""
    Usage:
    # {Fore.BLUE}For quit - {Fore.GREEN}"exit", 'quit', 'close', 'вихід', "вийти", 'stop', 'закрити'
    # {Fore.BLUE}For adding contact - {Fore.GREEN}<'add', 'plus', 'append', 'adding', 'додати', "плюс"> {Fore.LIGHTGREEN_EX}[optional - ' ' <contact name> ' ' <contact number>]
    # {Fore.BLUE}For contact changing -  {Fore.GREEN}<'change', 'змінити', 'замінити'> {Fore.LIGHTGREEN_EX}[optional -  ' ' <contact name> ' ' <new contact number>]
    # {Fore.BLUE}For adding another phone number to contact -  {Fore.GREEN}<'add_phone', 'another_phone', 'додати_номер'> {Fore.LIGHTGREEN_EX}[<contact name> ' ' <new contact number>]
    # {Fore.BLUE}For getting contact info - {Fore.GREEN}<'phone', 'show', 'look', 'find', 'give', 'contact', 'номер', 'покажи','показати', 'знайти', 'знайди', 'дай', 'контакт'> {Fore.LIGHTGREEN_EX}[optional - ' ' <contact name>]
    # {Fore.BLUE}For getting all contacts - {Fore.GREEN}'all', 'show-all', 'print-all', 'print', 'phone-book', 'contacts', 'list', 'усі', 'всі', 'друк', 'друкуй', 'роздрукуй', 'список', 'перелік', 'телефонна-книга','контакти'{Fore.RESET}
    # {Fore.BLUE}For getting contact`s birthday - {Fore.GREEN}'show_birthday', 'show-birthday', 'день_народження'{Fore.RESET}
    # {Fore.BLUE}For adding contact`s birthday - {Fore.GREEN}'add_birthday', 'birthday', 'додати_народження'{Fore.RESET}
    # {Fore.BLUE}For show contacts, whose birthdays are next week - {Fore.GREEN}'birthdays', 'all_birthdays', 'усі_дні'{Fore.RESET}
"""

INCORRECT_MESSAGE = (
    f"{Fore.RED}Sorry, but I don`t recognize your input, try again, please{Fore.RESET}"
)
