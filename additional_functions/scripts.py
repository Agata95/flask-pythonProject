from secrets import token_hex


def generate_token(long=12):
    if not isinstance(long, int):
        long = 12
    return token_hex(long)


if __name__ == "__main__":
    print("local tests:")
    print(generate_token())
    print(generate_token(20))
    print(generate_token("A"))
