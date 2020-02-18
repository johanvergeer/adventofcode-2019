import math
from dataclasses import dataclass
from typing import List


@dataclass
class SpacecraftComponent:
    weight: int

    @property
    def fuel_requirements(self):
        return math.floor(self.weight / 3) - 2


class Spacecraft:
    def __init__(self, components: List[SpacecraftComponent]):
        self.components = components

    @property
    def fuel_requirements(self) -> int:
        return sum(component.fuel_requirements for component in self.components)
