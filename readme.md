project for cis121

# RA Support System

A simple Python project to help Resident Assistants (RAs).

## Features

- **Noise Detector (**`loop.py`**)**: Checks entered noise levels and duration
- **Resident Check (**`person_list.py`**)**: Checks names against the resident dictionary
- **Access Check (**`check_key_access.py`**)**: Checks a resident's key-access setting
- **Resident Dictionary (**`residents.json`**)**: Stores resident names, tech IDs, and key access
- **Planned**: Remote access key and report form for Residential Life

The resident dictionary is loaded from `residents.json` when the app starts.
Kento is the only starter record with key access. Use menu option 4 to add or
update a resident; new residents do not receive key access automatically.
Changes are saved to the JSON file and remain available between runs.

## Run

Start the full support system from the project folder:

```bash
python main.py
```

The menu provides noise detection, resident lookup, and key-access checks. The
individual scripts can also still be run separately:

```bash
python loop.py
python person_list.py
python check_key_access.py
```

Run the resident dictionary tests with:

```bash
python -m unittest -v test_add_dictionary
```
