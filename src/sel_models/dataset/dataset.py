from typing import Any, Dict
from abc import ABC
import os
import json


class Dataset(ABC):
    base_path: str

    def __init__(self, base_path: str):
        self.base_path = base_path

    def get_dataset_name(self) -> str:
        raise NotImplementedError()

    def get_dataset_path(self) -> str:
        return os.path.join(self.base_path, 'dataset.txt.gz')

    def get_metadata_path(self) -> str:
        return os.path.join(self.base_path, 'metadata.json')

    def get_metadata(self) -> Dict[str, Any]:
        with open(self.get_metadata_path(), 'r', encoding='utf-8') as f:
            return json.load(f)
