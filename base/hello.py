def greet(name="World"):
    return f"Hello {name}!"


if __name__ == "__main__":
    name = input("Enter your name (or press Enter for 'World'): ").strip()
    print(greet(name if name else "World"))
