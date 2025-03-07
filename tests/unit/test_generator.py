# tests/unit/test_generator.py
import re
import pytest
from password_generator.generator import (
    generate_password_with_random,
    generate_password_custom,
)

@pytest.mark.parametrize("func", [generate_password_with_random, generate_password_custom])
def test_generate_password_basic(func):
    password = func(length=10, use_upper=True, use_lower=True, use_digits=True, special_chars="@#$", special_count=2)
    assert len(password) == 10

    # Verify that there is at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character.
    assert re.search(r"[A-Z]", password)
    assert re.search(r"[a-z]", password)
    assert re.search(r"[0-9]", password)
    assert re.search(r"[@#$]", password)
