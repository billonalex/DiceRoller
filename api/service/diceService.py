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
    return diceRepository.get_dices()

@dice.get(
    path="/{iddice}",
    name="Récupération d'un dé",
    description="Permet la récupération d'un dé.",
    response_model=Dice
)
def get_dices(iddice: int, current_user: User = Depends(authRepository.get_current_active_user)):
    return diceRepository.get_dice_by_id(iddice)

@dice.post(
    path="/",
    name="Nouveau lancer de dés",
    description="Permet un nouveau lancer de dés.",
    response_model=Dice
)
def throw_new_dice(current_user: User = Depends(authRepository.get_current_active_user)):
    return diceRepository.throw_new_dice(current_user.idutilisateur)