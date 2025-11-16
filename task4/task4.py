#!/usr/bin/env python3
from __future__ import annotations

from typing import Dict, Tuple


# -------------------- parser --------------------

def parse_input(user_input: str) -> Tuple[str, ...]:

    if not isinstance(user_input, str):
        return ("",)

    parts = user_input.strip().split()
    if not parts:
        return ("",)

    cmd, *args = parts
    cmd = cmd.strip().lower()
    return (cmd, *args)


# -------------------- handlers --------------------

def add_contact(args: Tuple[str, ...], contacts: Dict[str, str]) -> str:

    if len(args) != 2:
        return "Please provide name and phone: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: Tuple[str, ...], contacts: Dict[str, str]) -> str:

    if len(args) != 2:
        return "Please provide name and new phone: change <name> <phone>"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args: Tuple[str, ...], contacts: Dict[str, str]) -> str:

    if len(args) != 1:
        return "Please provide a name: phone <name>"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all(contacts: Dict[str, str]) -> str:

    if not contacts:
        return "No contacts found."
    # one contact per line, stable by name
    lines = [f"{name}: {contacts[name]}" for name in sorted(contacts.keys(), key=str.lower)]
    return "\n".join(lines)


# -------------------- loop --------------------

def main() -> None:
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(tuple(args), contacts))

        elif command == "change":
            print(change_contact(tuple(args), contacts))

        elif command == "phone":
            print(show_phone(tuple(args), contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":
            # empty input — просто проігноруємо
            continue

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
