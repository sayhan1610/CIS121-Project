project for cis121

# RA Support System

A simple Python project to help Resident Assistants (RAs).

## Features

- **Noise Detector (**`loop.py`**)**: Checks entered noise levels and duration
- **Resident Check (**`person_list.py`**)**: Checks names against a list
- **Access Check (**`check_key_access.py`**)**: Basic name-based access check
- **Planned**: Remote access key and report form for Residential Life

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
