# tests/test_cipher.py
import pytest
from caesar_tool.cipher import caesar, brute_force, normalize_shifts

def test_normalize_shifts():
    assert normalize_shifts([0, 26, 52]) == [0, 0, 0]
    with pytest.raises(ValueError):
        normalize_shifts([])

def test_encrypt_decrypt_roundtrip():
    text = "Hello, World!"
    shifts = [3]
    enc = caesar(text, shifts, encrypt=True)
    dec = caesar(enc, shifts, encrypt=False)
    assert dec == text

def test_multiple_shifts_cycle():
    text = "abcdef"
    out = caesar(text, [1,2], encrypt=True)  # shifts: 1,2,1,2,1,2
    assert out == "bdfdgh"

def test_ignore_nonalpha_default():
    text = "a-b-c"
    out = caesar(text, [1], encrypt=True, ignore_nonalpha=True)
    assert out == "b-c-d"

def test_advance_on_nonalpha():
    text = "ab-cd"
    out = caesar(text, [1,2], encrypt=True, ignore_nonalpha=False, advance_on_nonalpha=True)
    # positions: a(+1)->b, b(+2)->d, '-' consumes 3rd shift(=1), c(+2)->e, d(+1)->e
    assert out == "bd-ee"

def test_bruteforce_returns_26():
    assert len(brute_force("uryyb")) == 26
