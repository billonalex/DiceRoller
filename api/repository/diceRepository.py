import random

from models.dice import Dice
from models.user import User
from models.response import Response
from db.db import connect

class DiceRepository():
    def get_dices(self):
        conn = connect()
        cursor = conn.cursor();

        cursor.execute("""
        SELECT
            iddice,
            idutilisateur,
            valeur
        FROM dice""")

        res = cursor.fetchall()
        liste = [Dice(**element) for element in res]
        dices = {
            "dices": liste,
            "nb_row": len(liste),
        }

        return dices

    def get_dice_by_id(self, iddice):
        conn = connect()
        cursor = conn.cursor();

        cursor.execute("""
        SELECT
            iddice,
            idutilisateur,
            valeur
        FROM dice
        WHERE iddice = :iddice""", {"iddice": iddice})

        res = cursor.fetchone()
        return res

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

        return self.get_dice_by_id(cursor.lastrowid)
