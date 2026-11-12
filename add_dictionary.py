"""Resident records stored in the project's JSON data file."""

import json
from pathlib import Path


RESIDENTS_FILE = Path(__file__).with_name("residents.json")


def load_people():
    """Load and validate resident records from JSON."""
    with RESIDENTS_FILE.open(encoding="utf-8") as data_file:
        loaded_people = json.load(data_file)

    if not isinstance(loaded_people, dict):
        raise ValueError("Resident JSON must contain an object of resident records.")

    assigned_tech_ids = set()
    normalized_names = set()
    for resident_name, resident_data in loaded_people.items():
        if not isinstance(resident_name, str) or not resident_name.strip():
            raise ValueError("Resident names in JSON must be non-empty strings.")
        normalized_name = resident_name.casefold()
        if normalized_name in normalized_names:
            raise ValueError(f"Resident name {resident_name} is listed more than once.")
        normalized_names.add(normalized_name)
        if not isinstance(resident_data, dict):
            raise ValueError(f"Resident record for {resident_name} must be an object.")
        if "tech_id" not in resident_data or "key_access" not in resident_data:
            raise ValueError(
                f"Resident record for {resident_name} needs tech_id and key_access."
            )

        tech_id = resident_data["tech_id"]
        if tech_id is not None and (
            isinstance(tech_id, bool) or not isinstance(tech_id, int) or tech_id <= 0
        ):
            raise ValueError(
                f"Tech ID for {resident_name} must be null or a positive integer."
            )
        if tech_id is not None:
            if tech_id in assigned_tech_ids:
                raise ValueError(f"Tech ID {tech_id} is assigned more than once.")
            assigned_tech_ids.add(tech_id)
        if not isinstance(resident_data["key_access"], bool):
            raise ValueError(f"Key access for {resident_name} must be true or false.")

    return loaded_people


people = load_people()


def find_person(name):
    """Return a resident's record, matching names without case sensitivity."""
    normalized_name = name.strip().casefold()
    for resident_name, resident_data in people.items():
        if resident_name.casefold() == normalized_name:
            return resident_data
    return None


def add_to_dictionary(name, tech_id):
    """Add or update a resident and save the complete dictionary to JSON."""
    resident_name = name.strip()
    if not resident_name:
        raise ValueError("Resident name cannot be empty.")
    if isinstance(tech_id, bool) or not isinstance(tech_id, int) or tech_id <= 0:
        raise ValueError("Tech ID must be a positive whole number.")

    existing_name = next(
        (
            current_name
            for current_name in people
            if current_name.casefold() == resident_name.casefold()
        ),
        None,
    )
    if any(
        current_name != existing_name and data["tech_id"] == tech_id
        for current_name, data in people.items()
    ):
        raise ValueError("Tech ID is already assigned to another resident.")

    saved_name = existing_name or resident_name
    key_access = people[existing_name]["key_access"] if existing_name else False
    updated_people = {
        current_name: data.copy() for current_name, data in people.items()
    }
    updated_people[saved_name] = {
        "tech_id": tech_id,
        "key_access": key_access,
    }

    temporary_file = RESIDENTS_FILE.with_name(RESIDENTS_FILE.name + ".tmp")
    with temporary_file.open("w", encoding="utf-8") as data_file:
        json.dump(updated_people, data_file, indent=4)
        data_file.write("\n")
    temporary_file.replace(RESIDENTS_FILE)

    people.clear()
    people.update(updated_people)
