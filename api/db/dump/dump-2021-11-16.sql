BEGIN TRANSACTION;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('utilisateur',1);
CREATE TABLE utilisateur ( 
	idutilisateur        integer PRIMARY KEY AUTOINCREMENT   ,
	nom                  text     ,
	prenom               text     ,
	adresse              text     ,
	codepostal           integer     ,
	ville                text     ,
	pays                 text     ,
	telephone            text     ,
	mail                 text     ,
	username             text     ,
	password             text     ,
	disabled             boolean     
 );
INSERT INTO "utilisateur" VALUES(1,'TEST','Test','Mon adresse',21000,'Dijon','France','06 xx xx xx xx','test@test.fr','test','$2b$12$shMakvd5DrblXem29/oiaOiG4MwnKGVOwJDfoL0SChuS31LYycG0S',0);
COMMIT;
