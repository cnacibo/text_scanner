# app/domain/entities.py
from dataclasses import dataclass

@dataclass
class TextStatistics:
    word_count: int
    char_count: int
    paragraph_count: int
