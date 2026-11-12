import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import add_dictionary
from add_dictionary import add_to_dictionary, find_person, people
from check_key_access import check_key_access
from person_list import check_people


class ResidentDictionaryTests(unittest.TestCase):
    def setUp(self):
        self.original_people = copy.deepcopy(people)
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.residents_file = Path(self.temporary_directory.name) / "residents.json"
        self.residents_file.write_text(
            json.dumps(self.original_people), encoding="utf-8"
        )
        self.residents_file_patch = patch.object(
            add_dictionary, "RESIDENTS_FILE", self.residents_file
        )
        self.residents_file_patch.start()

    def tearDown(self):
        people.clear()
        people.update(self.original_people)
        self.residents_file_patch.stop()
        self.temporary_directory.cleanup()

    def test_existing_residents_are_available_to_both_lookups(self):
        self.assertEqual(check_people("sAyHaN"), "known person")
        self.assertEqual(check_people("unknown"), "unknown person")
        self.assertTrue(check_key_access("kento"))
        self.assertFalse(check_key_access("Marco"))

    def test_adding_resident_updates_shared_dictionary(self):
        add_to_dictionary(" New Resident ", 12345)

        self.assertEqual(find_person("new resident")["tech_id"], 12345)
        self.assertEqual(check_people("NEW RESIDENT"), "known person")
        self.assertFalse(check_key_access("New Resident"))
        stored_people = json.loads(self.residents_file.read_text(encoding="utf-8"))
        self.assertEqual(stored_people["New Resident"]["tech_id"], 12345)
        self.assertFalse(stored_people["New Resident"]["key_access"])
        self.assertEqual(add_dictionary.load_people(), stored_people)

    def test_duplicate_tech_id_is_rejected(self):
        add_to_dictionary("First Resident", 12345)

        with self.assertRaisesRegex(ValueError, "already assigned"):
            add_to_dictionary("Second Resident", 12345)

    def test_invalid_name_or_tech_id_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "name cannot be empty"):
            add_to_dictionary("  ", 12345)
        with self.assertRaisesRegex(ValueError, "positive whole number"):
            add_to_dictionary("New Resident", 0)

    def test_updating_resident_preserves_key_access(self):
        add_to_dictionary("kento", 54321)

        self.assertTrue(check_key_access("Kento"))
        self.assertEqual(find_person("KENTO")["tech_id"], 54321)


if __name__ == "__main__":
    unittest.main()
