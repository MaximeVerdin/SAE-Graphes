from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Case:
    x: int
    y: int
    contenu: int | None = None

    motif: "Motif | None" = None

    def __post_init__(self):
        self.fixe = self.contenu is not None

    def getPosition(self) -> tuple[int, int]:
        return self.x, self.y

    def estVoisin(self, autre: "Case") -> bool:
        dx = abs(self.x - autre.x)
        dy = abs(self.y - autre.y)

        return dx <= 1 and dy <= 1 and not (dx == 0 and dy == 0)

    def toList(self) -> list[int]:
        return [
            self.x,
            self.y,
            self.contenu if self.contenu is not None else 0
        ]