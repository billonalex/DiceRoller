from typing import Optional, List

from pydantic import BaseModel

class Dice(BaseModel):
    iddice: int
    valeur: int
    idutilisateur: int

class DiceList(BaseModel):
    dices: List[Dice]
    nb_row: int