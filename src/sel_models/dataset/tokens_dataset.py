from typing import Any, List
import os
from .dataset import Dataset


class TokensDataset(Dataset):
    def __init__(self, base_path: str):
        super().__init__(base_path)

    def get_vocab_path(self) -> str:
        return os.path.join(self.base_path, 'vocab.txt')

    def get_vocab(self) -> List[str]:
        with open(self.get_vocab_path(), 'r', encoding='utf-8') as f:
            return f.readline().split(' ')
