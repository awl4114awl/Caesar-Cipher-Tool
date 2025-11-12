# caesar_tool/cli.py
import argparse
import sys
from .cipher import caesar, brute_force

def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Caesar Cipher CLI")
    p.add_argument("text", nargs="?", help="Input text (omit to read from stdin)")
    p.add_argument("-s", "--shift", help="Comma-separated shift(s) 0-25", default="13")
    p.add_argument("-d", "--decrypt", action="store_true", help="Use decrypt mode (default: encrypt)")
    p.add_argument("--no-ignore", action="store_true", help="Do not ignore non-letters")
    p.add_argument("--advance", action="store_true", help="Advance shift index on non-letters")
    p.add_argument("--bruteforce", action="store_true", help="Show all 26 decrypt possibilities")
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    text = args.text if args.text is not None else sys.stdin.read()
    if args.bruteforce:
        for k, out in enumerate(brute_force(text)):
            print(f"Shift {k:2d}: {out}")
        return 0
    shifts = [int(x.strip()) for x in args.shift.split(",") if x.strip()]
    out = caesar(
        text,
        shifts,
        encrypt=not args.decrypt,
        ignore_nonalpha=not args.no_ignore,
        advance_on_nonalpha=args.advance,
    )
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
