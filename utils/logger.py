import logging

from colorama import Fore, Style, init

init(autoreset=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message):

    print(Fore.GREEN + message)

    logging.info(message)


def log_error(message):

    print(Fore.RED + str(message))

    logging.error(message)


def log_warning(message):

    print(Fore.YELLOW + message)

    logging.warning(message)