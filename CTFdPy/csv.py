import csv
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class CSVHandler:
    csv_path_str: str
    required_fields: list[str] = field(default_factory=lambda: ['username', 'email'])
    optional_fields: list[str] = field(default_factory=lambda: ['password'])
    # TODO: These are the only optional fields that our wrapper accepts for now.

    def __post_init__(self):
        self.csv_path = Path(self.csv_path_str)

    def _check_csv_exists(self) -> bool:
        return self.csv_path.is_file()

    def _get_missing_fields(self, headers: list[str]) -> list[str]:
        stripped_headers = [field.strip() for field in headers]
        missing_fields = [
            field for field in self.required_fields if field not in stripped_headers]
        return missing_fields

    def _get_unexpected_fields(self, headers: list[str]) -> list[str]:
        stripped_headers = [field.strip() for field in headers if field != ""]
        unexpected_fields = []
        for field in stripped_headers:
            if field not in self.required_fields and field not in self.optional_fields:
                unexpected_fields.append(field)
        return unexpected_fields

    def _strip_values(self, row: dict[str, str]) -> dict[str]:
        stripped_row = {key.strip(): value.strip()
                        for key, value in row.items()}
        return stripped_row

    def read_csv(self) -> list[dict[str, str]]:
        if not self._check_csv_exists():
            raise FileNotFoundError("CSV file does not exist.")

        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames

            missing_fields = self._get_missing_fields(headers)
            if missing_fields:
                raise MissingFieldsError(missing_fields)

            unexpected_fields = self._get_unexpected_fields(headers)
            if unexpected_fields:
                raise UnexpectedFieldsError(unexpected_fields)
            users = [self._strip_values(row) for row in reader]

        return users

    # TODO: write_csv method


class MissingFieldsError(Exception):
    def __init__(self, missing_fields: list[str]):
        self.missing_fields = missing_fields

    def __str__(self):
        missing_fields_str = ', '.join(self.missing_fields)
        return f"Required fields are missing in the CSV file: {missing_fields_str}"


class UnexpectedFieldsError(Exception):
    def __init__(self, unexpected_fields: list[str]):
        self.unexpected_fields = unexpected_fields

    def __str__(self):
        if all(field == "" for field in self.unexpected_fields):
           return "Trailing commas found in the CSV file. Please ensure there are no empty fields or trailing commas."
        else: 
            unexpected_fields_str = ', '.join(self.unexpected_fields)
            return f"Unexpected fields found in the CSV file: {unexpected_fields_str}"
