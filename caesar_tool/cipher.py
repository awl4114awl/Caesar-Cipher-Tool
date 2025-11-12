# caesar_tool/cipher.py
from typing import Iterable, List

ALPHA_LOW = ord("a")
ALPHA_UP = ord("A")
ALPHABET = 26

def _shift_char(ch: str, shift: int) -> str:
    """Shift a single ASCII letter by shift, preserving case."""
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ALPHA_UP + shift) % ALPHABET + ALPHA_UP)
    if "a" <= ch <= "z":
        return chr((ord(ch) - ALPHA_LOW + shift) % ALPHABET + ALPHA_LOW)
    return ch  # non-letters returned unchanged

def normalize_shifts(shifts: Iterable[int]) -> List[int]:
    s = [int(x) % ALPHABET for x in shifts]
    if not s:
        raise ValueError("At least one shift value is required.")
    return s

def caesar(
    text: str,
    shifts: Iterable[int],
    *,
    encrypt: bool = True,
    ignore_nonalpha: bool = True,
    advance_on_nonalpha: bool = False
) -> str:
    """
    Caesar cipher with support for multiple shifts (cycled).
    - If encrypt=False, uses negative shifts.
    - ignore_nonalpha=True => non-letters are left unchanged AND do not consume a shift.
    - advance_on_nonalpha=True => non-letters still do NOT change, but do consume a shift.
    """
    seq = normalize_shifts(shifts)
    if not encrypt:
        seq = [(-n) % ALPHABET for n in seq]

    out = []
    i = 0  # index into shift sequence

    for ch in text:
        if ch.isalpha():
            shift = seq[i % len(seq)]
            out.append(_shift_char(ch, shift))
            i += 1
        else:
            out.append(ch)
            if not ignore_nonalpha and advance_on_nonalpha:
                # consume shift position even on non-letters (optional behavior)
                i += 1

    return "".join(out)

def brute_force(text: str) -> List[str]:
    """Return all 26 possibilities (shift 0..25) for convenience."""
    return [caesar(text, [k], encrypt=False) for k in range(ALPHABET)]

def detect_by_frequency(text: str) -> int:
    """
    (Optional) Naive frequency heuristic: guess the best shift for English.
    Returns an integer 0..25 (best 'decrypt' shift).
    """
    from collections import Counter
    # English ETAOIN SHRDLU heuristic
    target_order = "etaoinshrdlucmfwypvbgkjqxz"
    letters = [c.lower() for c in text if c.isalpha()]
    if not letters:
        return 0
    counts = Counter(letters)
    most = counts.most_common(1)[0][0]
    # assume 'e' is most common -> find shift mapping 'most' -> 'e'
    guessed = (ord(most) - ord('e')) % ALPHABET
    return guessed
