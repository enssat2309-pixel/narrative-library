# Compte rendu — tirage du pilote, version 2 (ajustement du 17/11/2026)

Rédigé le 17/11/2026 21:48 (heure d'Europe/Luxembourg). La v1 (`tirage/`, `tirage_2026-11-17.zip`) n'est pas modifiée.

## 1. Changements par rapport à la v1, par strate

| Lot | Strate | Documents principaux sortis | Documents principaux entrés | Documents de réserve sortis | Documents de réserve entrés | Segments principaux sortis / entrés | Lignes (principal + réserve) sorties / entrées |
|---|---|---|---|---|---|---|---|
| lot1 | S1 | — | — | — | — | 0 / 0 | 0 / 0 |
| lot1 | S2 | — | — | — | — | 0 / 0 | 0 / 0 |
| lot1 | S3 | — | — | — | — | 0 / 0 | 0 / 0 |
| lot1 | S4 | — | — | — | — | 0 / 0 | 0 / 0 |
| lot2 | S1 | LOT2-FR0013532363-FR-KID-68889a53 | LOT2-FR0013532363-FR-KID-68889a53-KID | — | — | 2 / 2 | 5 / 5 |
| lot2 | S2 | — | — | — | — | 0 / 0 | 0 / 0 |
| lot2 | S3 | LOT2-FR001400R7U7-FR-Prospectus-8c916fe6<br>LOT2-FR0014010344-FR-Prospectus-341a7920<br>LOT2-LU0599613147-FR-Prospectus-665694a8<br>LOT2-LU2423921167-IT-Prospectus-f481d65c | LOT2-FR0013532363-FR-Prospectus-650332b7<br>LOT2-FR001400S0F2-FR-Prospectus-c5531513<br>LOT2-IE00BZ163H91-ES-Prospectus-02d06502<br>LOT2-LU0599613147-DE-Prospectus-11a04632 | LOT2-FR0013532363-FR-Prospectus-650332b7<br>LOT2-IE00BZ163H91-ES-Prospectus-02d06502 | LOT2-FR0013529864-FR-Prospectus-eaccb443<br>LOT2-FR0014010344-FR-Prospectus-341a7920 | 8 / 8 | 15 / 15 |
| lot2 | S4 | — | — | — | — | 0 / 0 | 0 / 0 |

Lot 1, lot 2 S2 et lot 2 S4 : tirage identique à la v1 ligne pour ligne. Lot 2 S1 : l'unité Colville devient LOT2-FR0013532363-FR-KID-68889a53-KID (pages 1-3 seulement), toujours au rang 7 ; son nouveau doc_id change la graine du temps 2, d'où 2 segments principaux et 3 de réserve nouveaux. Lot 2 S3 : l'ajout de l'unité LOT2-FR0013532363-FR-KID-68889a53-PROSPECTUS à la liste triée change le mélange de toute la strate (effet attendu, annoncé par l'ajustement) ; cette unité elle-même est refusée (fonds FR0013532363 déjà couvert par LOT2-FR0013532363-FR-Prospectus-650332b7, accepté avant elle).

## 2. Limites de pages retenues pour Colville (sha256 68889a53…)

- Vérifiées dans le texte (titres « Document d'Informations Clés », ISIN de chaque KID, ligne « PROSPECTUS ») ; conformes aux notes du manifeste.
- KID de la part C (FR0013532363) : pages 1-3 → unité LOT2-FR0013532363-FR-KID-68889a53-KID (S1).
- KID des autres parts : pages 4-6 (part R, FR0014005DN0) et 7-9 (part USD, FR0013532371) → unité LOT2-FR0013532363-FR-KID-68889a53-KID-AUTRES-CLASSES, exclue du cadre (« KID d'une autre classe de parts »).
- Prospectus : pages 10-37 → unité LOT2-FR0013532363-FR-KID-68889a53-PROSPECTUS (S3).

## 3. Autres fichiers composites

- Aucun : dans les lots 1, 2 et l'annexe Singapour, Colville est le seul fichier (même sha256) listé sous plusieurs types de document.

## 4. Contrôle de la règle des 5 espaces

Voir controle_5espaces.csv (20 segments) et journal_tirage.md, section 7 bis.

| Couple | Segments exclus par la règle des 5 espaces (population) | Segments perimetre_v2 « oui » restants | Segments tirés |
|---|---|---|---|
| lot1 KID et fiches locales | 468 | 334 | 5 |
| lot1 factsheets | 153 | 66 | 5 |
| lot2 KID et fiches locales | 425 | 431 | 5 |
| lot2 factsheets | 589 | 339 | 5 |
