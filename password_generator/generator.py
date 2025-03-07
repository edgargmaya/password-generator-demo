# password_generator/generator.py
import time

def generate_password_with_random(
    length=12,
    use_upper=True,
    use_lower=True,
    use_digits=True,
    special_chars="!@#$%",
    special_count=2
):
    """
    Generates a random password using the `random` module.
    Ensures to include at least one character of each required type.
    """
    import random  # Local import to show we use the standard lib

    if not any([use_upper, use_lower, use_digits, special_count > 0]):
        raise ValueError("At least one character category must be enabled.")

    # Define character sets
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    digit_chars = "0123456789"

    # Build initial pool and force inclusion of one of each type, if applicable
    pool = ""
    password = []

    if use_upper:
        pool += upper_chars
        password.append(random.choice(upper_chars))
    if use_lower:
        pool += lower_chars
        password.append(random.choice(lower_chars))
    if use_digits:
        pool += digit_chars
        password.append(random.choice(digit_chars))
    if special_count > 0 and special_chars:
        pool += special_chars
        # Force the inclusion of at least one
        password.append(random.choice(special_chars))

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(pool))

    # Mix the characters
    random.shuffle(password)
    return "".join(password)


def generate_password_custom(
    length=12,
    use_upper=True,
    use_lower=True,
    use_digits=True,
    special_chars="!@#$%",
    special_count=2
):
    """
    Generates a random password using a 'from scratch' pseudo-random generator.
    This is merely demonstrative; it is not recommended for production.
    """

    if not any([use_upper, use_lower, use_digits, special_count > 0]):
        raise ValueError("At least one character category must be enabled.")

    # Define character sets
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    digit_chars = "0123456789"

    # Assemble the character 'pool'
    pool = ""
    if use_upper:
        pool += upper_chars
    if use_lower:
        pool += lower_chars
    if use_digits:
        pool += digit_chars
    if special_count > 0 and special_chars:
        pool += special_chars

    # Minimalist linear congruential generator (LCG)
    # seed using time
    seed = int(time.time() * 1000000) & 0xffffffff

    def lcg_rand():
        # typical LCG parameters: 1664525, 1013904223
        nonlocal seed
        seed = (1664525 * seed + 1013904223) & 0xffffffff
        return seed

    def lcg_choice(sequence):
        index = lcg_rand() % len(sequence)
        return sequence[index]

    # Assemble the password, forcing at least one of each type
    password = []

    if use_upper:
        password.append(lcg_choice(upper_chars))
    if use_lower:
        password.append(lcg_choice(lower_chars))
    if use_digits:
        password.append(lcg_choice(digit_chars))
    if special_count > 0 and special_chars:
        password.append(lcg_choice(special_chars))

    while len(password) < length:
        password.append(lcg_choice(pool))

    # Mix the password "by hand"
    for i in range(len(password) - 1, 0, -1):
        j = lcg_rand() % (i + 1)
        password[i], password[j] = password[j], password[i]

    return "".join(password)
