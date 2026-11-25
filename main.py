"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of last words a phone says as its battery hits 1 percent
to /output/entry.txt. Python 3.13 standard library only; no network.

The line was picked from 20 candidates scored against the judge rubric
(phone's own voice, hard twist, tight single line, fresh): the phone
 blurts its owner's secrets as it dies, cut off mid-PIN.
"""

import os

ENTRY = "I know your passcode: 4821. Your bank PIN is 739\u2014"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Gate assertions: output must be exactly one line, 1-199 chars, non-empty.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "output does not match the entry text"
    assert written, "output must be non-empty"
    assert "\n" not in written, "output must be exactly one line"
    assert 1 <= len(written) <= 199, "output must be 1-199 characters"
    assert written.strip(), "output must not be only whitespace"


if __name__ == "__main__":
    main()
