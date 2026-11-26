# Mission 3 – Additif v2 du tirage (17 novembre 2026)

Arbitrages : lot 1 incomplet accepté (1A) ; fichier composite Colville traité par une règle explicite (2B) ; contrôle de la règle des « 5 espaces » (3A).

1. Lot 1 incomplet : accepté tel quel. La règle « un document par fonds et par strate » ne change pas.
2. Règle « fichier composite » : quand un même fichier (même sha256) est listé sous plusieurs types de document, il est découpé par pages : les pages du KID de la classe tirée forment une unité de type KID (S1) ; les pages des KID d'autres classes sortent du cadre ; les pages du prospectus forment une unité de type Prospectus (S3). Pour Colville : KID de la part C aux pages 1 à 3, autres KID pages 4 à 9, prospectus à partir de la page 10. Identifiants `<doc_id>-KID` et `<doc_id>-PROSPECTUS`. Le script est relancé avec ce seul changement.
3. Contrôle de la règle « 5 espaces consécutifs ou plus » : 20 segments exclus par cette règle tirés au hasard (5 par couple lot × KID/factsheet), graine "2026-controle-5espaces", avec leur texte complet.

Livrables dans tirage_v2/ : mêmes fichiers que la v1, `controle_5espaces.csv` et un compte rendu des changements.
