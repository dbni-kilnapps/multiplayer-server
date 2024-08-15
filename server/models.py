from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Player:
    id: int
    score: int
    position: Tuple[float, float]