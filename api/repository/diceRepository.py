import random

from models.user import User
from models.response import Response
from db.db import connect

class DiceRepository():
    def get_dices(self):
        return True

    def throw_new_dice(self, idutilisateur):
        conn = connect()
        valeur = random.randint(1,20)

        cursor = conn.cursor();

        cursor.execute("""
        INSERT INTO dice ( idutilisateur, valeur )
        VALUES ( :idutilisateur, :valeur )""", {
            "idutilisateur": idutilisateur,
            "valeur": valeur
        })

        conn.commit()
