# Returns a greeting string for the given name
def greet(name="World"):
    return f"Hello {name}!"


if __name__ == "__main__":
    # Prompt the user for their name; default to "World" if blank
    name = input("Enter your name (or press Enter for 'World'): ").strip()
    print(greet(name if name else "World"))
