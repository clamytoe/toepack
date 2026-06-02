#!/usr/bin/env python3
def cli():
    try:
        main()
    except KeyboardInterrupt:
        print("\nTerminated by user.")


def main():
    message = (
        "{{ cookiecutter.__project_slug }} installed successfully!\n"
        "You're ready to start building."
    )
    print(message)


if __name__ == "__main__":
    main()
