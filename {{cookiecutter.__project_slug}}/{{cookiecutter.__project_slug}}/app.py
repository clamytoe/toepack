#!/usr/bin/env python3
"""
app.py

{{cookiecutter.project_title}}
"""


def cli():
    try:
        main()
    except KeyboardInterrupt:
        print("\nTerminated by user.")


def main():
    print("Successfully installed your project file: {{cookiecutter.__project_slug}}")


if __name__ == "__main__":
    main()
