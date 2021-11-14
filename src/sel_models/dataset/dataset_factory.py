from typing import Any

from .dataset import Dataset
from .tokens_dataset import TokensDataset


def get_dataset(base_path: str, metadata: dict[str, Any]) -> Dataset:
    ds_type = metadata['dataset_type']
    if ds_type == 'TokensDataset':
        return TokensDataset(base_path)

    return Dataset(base_path)

