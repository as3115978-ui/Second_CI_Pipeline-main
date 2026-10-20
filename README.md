# Second_CI_Pipeline

Assignment 6: ten Python programs (31-40), pytest tests, and a GitHub Actions
workflow. Each program and its test must be committed on its own feature branch,
then merged into main through a pull request after CI passes.

## Folder structure

```text
Second_CI_Pipeline/
|-- code/
|   |-- 31_pangram.py
|   `-- ... programs 32 to 40
|-- testcase/
|   |-- __init__.py
|   |-- test_31_pangram.py
|   `-- ... tests 32 to 40
|-- .github/workflows/ci.yml
|-- __init__.py
|-- pytest.ini
|-- requirements.txt
|-- .gitignore
`-- README.md
```

`pytest.ini` discovers tests in `testcase` and adds `code` to the Python import
path, so the numbered modules can still be loaded with `importlib`.
`code` stays a plain folder without `__init__.py` to avoid shadowing Python's
standard-library `code` module, which pytest's debugger uses.

## Program behavior

- Pangram checks all 26 English letters, ignoring case.
- Word counting splits on whitespace; punctuation stays attached to words.
- First non-repeating character is case-sensitive and includes whitespace;
  returns `None` when no unique character exists.
- Sorted means ascending, allowing duplicates; an empty list is sorted.
- Moving zeros returns a new numeric list, preserving nonzero order.
- Most frequent accepts hashable items, resolves ties by first appearance,
  and returns `None` for an empty list.
- Rotation is to the left; negative positions rotate right.
- Missing number uses XOR and assumes distinct integers from `1..n` with exactly
  one missing, where `n = len(numbers) + 1`.
- Transpose requires rectangular rows; unequal row lengths raise `ValueError`.
- GCD is nonnegative and handles negative numbers and zero; `gcd(0, 0) = 0`.

## Local checks

Run these commands in PowerShell, one line at a time. Stop if a command fails.

```powershell
cd "C:\Users\ADMIN\Second_CI_Pipeline"
python -m pip install -r requirements.txt
python -m pytest -v
```

## 1. Create the repository and push only the base files

No repository was created while preparing these files. Run the commands below
yourself. Git and GitHub CLI (`gh`) must be installed. Check `gh auth status`;
if necessary, sign in with `gh auth login` before continuing.

The `--public` flag below creates a public GitHub repository. You can replace it
with `--private` if your course allows a private submission.

Do not use `git add .` or `git add -A`: all ten programs already exist locally,
but must not be included in the initial main commit.

```powershell
cd "C:\Users\ADMIN\Second_CI_Pipeline"
git init -b main
git add __init__.py testcase/__init__.py pytest.ini requirements.txt .gitignore README.md .github/workflows/ci.yml
git commit -m "Initial setup: package, requirements, and CI workflow"
gh repo create Second_CI_Pipeline --public --source=. --remote=origin
git push -u origin main
```

The workflow runs on pull requests targeting main, as in the PDF. The initial
main push and feature branch pushes alone do not trigger it. Opening each pull
request below starts CI.

## 2. Push and merge one program at a time

Complete each program's push, CI check, and merge before starting the next.
Each new branch adds exactly one program and its test to the updated main.
Earlier merged programs will also be present on later branches.

If `gh pr checks --watch` says no checks are reported yet, wait a few seconds
and run that line again. Only merge after `Validate Program and Test Cases`
passes. If any check fails, stop and fix it before merging.

Keep the ten remote branches for the PDF's final checklist. In the repository
settings, leave automatic deletion of head branches disabled, and do not select
Delete branch after merging. You can also use GitHub's Pull requests page to
open each PR and merge it after the green check appears.

### Program 31: pangram check

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 31-pangram
git add code/31_pangram.py testcase/test_31_pangram.py
git commit -m "Add pangram check program and tests"
git push -u origin 31-pangram
gh pr create --base main --head 31-pangram --fill
gh pr checks 31-pangram --watch
```

After the CI check passes:

```powershell
gh pr merge 31-pangram --merge
git checkout main
git pull --ff-only origin main
```

### Program 32: count words

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 32-count-words
git add code/32_count_words.py testcase/test_32_count_words.py
git commit -m "Add count words program and tests"
git push -u origin 32-count-words
gh pr create --base main --head 32-count-words --fill
gh pr checks 32-count-words --watch
```

After the CI check passes:

```powershell
gh pr merge 32-count-words --merge
git checkout main
git pull --ff-only origin main
```

### Program 33: first non-repeating character

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 33-first-non-repeating
git add code/33_first_non_repeating.py testcase/test_33_first_non_repeating.py
git commit -m "Add first non-repeating character program and tests"
git push -u origin 33-first-non-repeating
gh pr create --base main --head 33-first-non-repeating --fill
gh pr checks 33-first-non-repeating --watch
```

After the CI check passes:

```powershell
gh pr merge 33-first-non-repeating --merge
git checkout main
git pull --ff-only origin main
```

### Program 34: check sorted list

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 34-check-sorted
git add code/34_check_sorted.py testcase/test_34_check_sorted.py
git commit -m "Add check sorted list program and tests"
git push -u origin 34-check-sorted
gh pr create --base main --head 34-check-sorted --fill
gh pr checks 34-check-sorted --watch
```

After the CI check passes:

```powershell
gh pr merge 34-check-sorted --merge
git checkout main
git pull --ff-only origin main
```

### Program 35: move zeros

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 35-move-zeros
git add code/35_move_zeros.py testcase/test_35_move_zeros.py
git commit -m "Add move zeros program and tests"
git push -u origin 35-move-zeros
gh pr create --base main --head 35-move-zeros --fill
gh pr checks 35-move-zeros --watch
```

After the CI check passes:

```powershell
gh pr merge 35-move-zeros --merge
git checkout main
git pull --ff-only origin main
```

### Program 36: most frequent element

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 36-most-frequent
git add code/36_most_frequent.py testcase/test_36_most_frequent.py
git commit -m "Add most frequent element program and tests"
git push -u origin 36-most-frequent
gh pr create --base main --head 36-most-frequent --fill
gh pr checks 36-most-frequent --watch
```

After the CI check passes:

```powershell
gh pr merge 36-most-frequent --merge
git checkout main
git pull --ff-only origin main
```

### Program 37: rotate string

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 37-rotate-string
git add code/37_rotate_string.py testcase/test_37_rotate_string.py
git commit -m "Add rotate string program and tests"
git push -u origin 37-rotate-string
gh pr create --base main --head 37-rotate-string --fill
gh pr checks 37-rotate-string --watch
```

After the CI check passes:

```powershell
gh pr merge 37-rotate-string --merge
git checkout main
git pull --ff-only origin main
```

### Program 38: missing number XOR

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 38-missing-number-xor
git add code/38_missing_number_xor.py testcase/test_38_missing_number_xor.py
git commit -m "Add missing number XOR program and tests"
git push -u origin 38-missing-number-xor
gh pr create --base main --head 38-missing-number-xor --fill
gh pr checks 38-missing-number-xor --watch
```

After the CI check passes:

```powershell
gh pr merge 38-missing-number-xor --merge
git checkout main
git pull --ff-only origin main
```

### Program 39: transpose matrix

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 39-transpose-matrix
git add code/39_transpose_matrix.py testcase/test_39_transpose_matrix.py
git commit -m "Add transpose matrix program and tests"
git push -u origin 39-transpose-matrix
gh pr create --base main --head 39-transpose-matrix --fill
gh pr checks 39-transpose-matrix --watch
```

After the CI check passes:

```powershell
gh pr merge 39-transpose-matrix --merge
git checkout main
git pull --ff-only origin main
```

### Program 40: GCD

```powershell
git checkout main
git pull --ff-only origin main
git checkout -b 40-gcd
git add code/40_gcd.py testcase/test_40_gcd.py
git commit -m "Add GCD program and tests"
git push -u origin 40-gcd
gh pr create --base main --head 40-gcd --fill
gh pr checks 40-gcd --watch
```

After the CI check passes:

```powershell
gh pr merge 40-gcd --merge
git checkout main
git pull --ff-only origin main
```

## 3. Final verification

```powershell
python -m pytest -v
git branch -a
gh pr list --state merged --base main --limit 10
git status
```

Confirm all tests pass, all ten feature branches exist remotely, all ten pull
requests were merged, and main contains the workflow and all program/test files.
Collect any screenshots or other submission evidence your instructor requests
from your actual GitHub runs.

The setup uses the requested `code` and `testcase` folders and explicitly stages
the package files, `pytest.ini`, and `.github/workflows/ci.yml` so every feature
branch inherits the package setup, test configuration, and CI.
