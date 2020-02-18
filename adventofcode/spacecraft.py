import math
from dataclasses import dataclass
from typing import List


@dataclass
class SpacecraftComponent:
    weight: int

    def _calculate_fuel_for_weight(self, weight: int) -> int:
        """Calculates fuel recursively, meaning it will also include fuel required for the fuel."""
        required_fuel = math.floor(weight / 3) - 2

        if required_fuel > 0:
            return required_fuel + self._calculate_fuel_for_weight(required_fuel)
        return 0

    @property
    def fuel_requirements(self):
        return self._calculate_fuel_for_weight(self.weight)


class Spacecraft:
    def __init__(self, components: List[SpacecraftComponent]):
        self.components = components

    @property
    def fuel_requirements(self) -> int:
        return sum(component.fuel_requirements for component in self.components)
