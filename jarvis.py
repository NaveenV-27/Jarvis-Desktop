from core.commands import process_command
from core.listener import take_command
from features.assistant import wish_me


def main():
    wish_me()

    while True:
        query = take_command()

        if not query:
            continue

        should_exit = process_command(query)

        if should_exit:
            break


if __name__ == "__main__":
    main()