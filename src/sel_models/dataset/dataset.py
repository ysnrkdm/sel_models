from typing import Any
import os
import json


class Dataset:
    base_path: str

    def __init__(self, base_path: str):
        self.base_path = base_path

    def get_dataset_path(self) -> str:
        return os.path.join(self.base_path, 'dataset.txt')

    def get_metadata_path(self) -> str:
        return os.path.join(self.base_path, 'metadata.json')

    def get_metadata(self) -> dict[str, Any]:
        with open(self.get_metadata_path(), 'r', encoding='utf-8') as f:
            return json.load(f)
