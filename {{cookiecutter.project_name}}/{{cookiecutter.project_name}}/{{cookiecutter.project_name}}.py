#!/usr/bin/env python3
"""
{{cookiecutter.project_name}}.py

{{cookiecutter.project_title}}
"""
from .log_init import setup_logging

logger = setup_logging()


def main():
    logger.debug("Entering main.")
    logger.info("Printing default message")
    print(f"Successfully installed your project file: {{cookiecutter.project_name}}")


if __name__ == "__main__":
    logger.debug("Running as a module.")
    main()
