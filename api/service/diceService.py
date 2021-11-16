from fastapi import APIRouter, Depends
from models.response import Response

from models.user import User
from models.dice import Dice, DiceList

import repository.authRepository as authRepository

from repository.diceRepository import DiceRepository
# Injection des repository
diceRepository = DiceRepository()

dice = APIRouter(
    prefix="/des",
    tags=["Dés"],
    responses={404: {"description": "Not found"}},
)

@dice.get(
    path="/",
    name="Récupération des dés",
    description="Permet la récupération des dés.",
    response_model=DiceList
)
def get_dices(current_user: User = Depends(authRepository.get_current_active_user)):
    return True