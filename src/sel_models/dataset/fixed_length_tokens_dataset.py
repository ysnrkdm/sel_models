from typing import Any, List
import os
from .tokens_dataset import TokensDataset


class FixedLengthTokensDataset(TokensDataset):
    def __init__(self, base_path: str):
        super().__init__(base_path)

    def get_dataset_name(self) -> str:
        return 'FixedLengthTokensDataset'
