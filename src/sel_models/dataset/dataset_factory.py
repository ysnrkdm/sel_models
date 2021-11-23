from typing import Any, Dict

from .dataset import Dataset
from .fixed_length_tokens_dataset import FixedLengthTokensDataset
from .tokens_dataset import TokensDataset


def get_dataset(base_path: str, metadata: Dict[str, Any]) -> Dataset:
    ds_type = metadata['dataset_type']
    if ds_type == 'TokensDataset':
        return TokensDataset(base_path)
    elif ds_type == 'FixedLengthTokensDataset':
        return FixedLengthTokensDataset(base_path)

    return Dataset(base_path)
