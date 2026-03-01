# Python HTML String Manipulation Challenges

5 Python challenges to build and modify a minimal HTML page using string methods
and concatenation only. No parsers, no libraries — pure string primitives.

## Rules
- Only string methods (.replace, .find, .rfind, .split, .index, .count, etc.) are allowed
- String concatenation with + and += is allowed
- f-strings may be used to build values before insertion
- Converting the string to a list to index elements is NOT allowed
- No imports or external libraries of any kind

## Challenges

| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Update Page Metadata | `challenge/01-metadata` | ✅ Done |
| 2 | Update Stylesheet and Script Sources | `challenge/02-assets` | ✅ Done |
| 3 | Inject Heading Tags | `challenge/03-headings` | ✅ Done |
| 4 | Add Paragraph and Image Tags | `challenge/04-content` | ✅ Done |
| 5 | Full Page Builder | `challenge/05-full-page` | ✅ Done |

## Outputs

### Challenge 1 — Update Page Metadata

**Concepts:** `.replace()`, f-strings, string concatenation

**Solution file:** `challenge_01_metadata.py`

**HTML output file:** `html_outputs/challenge_01_output.html`

**Terminal output:**
![Challenge 1 Terminal](screenshots/challenge_01_terminal.png)

### Challenge 2 — Update Stylesheet and Script Sources

**Concepts:** `.find()`, `.index()`, string slicing

**Solution file:** `challenge_02_stylesheets_and_scripts.py`

**HTML output file:** `html_outputs/challenge_02_output.html`

**Terminal output:**
![Challenge 2 Terminal](screenshots/challenge_02_terminal.png)

### Challenge 3 — Inject Heading Tags

**Concepts:** `.split()`, string concatenation, multi-line string building

**Solution file:** `challenge_03_headings.py`

**HTML output file:** `html_outputs/challenge_03_output.html`

**Terminal output:**
![Challenge 3 Terminal](screenshots/challenge_03_terminal.png)

### Challenge 4 — Add Paragraph and Image Tags

**Concepts:** `.find()`, `.rfind()`, multi-step string reconstruction

**Solution file:** `challenge_04_content.py`

**HTML output file:** `html_outputs/challenge_04_output.html`

**Terminal output:**
![Challenge 4 Terminal](screenshots/challenge_04_terminal.png)

### Challenge 5 — Full Page Builder

**Concepts:** All string methods combined, validation pipeline, dynamic extraction

**Solution file:** `challenge_05_full_page.py`

**HTML output file:** `html_outputs/challenge_05_output.html`

**Terminal output:**
![Challenge 5 Terminal](screenshots/challenge_05_terminal.png)