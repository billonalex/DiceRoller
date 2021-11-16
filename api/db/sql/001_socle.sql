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
 
CREATE TABLE dice ( 
	iddice   		     integer PRIMARY KEY AUTOINCREMENT   ,
	idutilisateur        integer     ,
	valeur               integer     ,
	FOREIGN KEY ( idutilisateur ) REFERENCES utilisateur( idutilisateur )  
 );