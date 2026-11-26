# Auto-contrôle avant livraison — mission 3 (section 7)

Rédigé le 17/11/2026 21:28 (heure d'Europe/Luxembourg).

## 1. Deux exécutions successives

- Exécution 1 : `nice python3 tirage/tirage_script.py /workspace/doc-screener/tirage` (PYTHONHASHSEED=1), sortie dans `tirage/`.
- Exécution 2 : même script, mêmes fichiers d'entrée, PYTHONHASHSEED=777, sortie dans un dossier temporaire hors du projet (`/tmp/tirage_run2`).
- sha256 de tirage_pilote.csv, exécution 1 : `96e7de6f76a3bea00eced724c1026730e5d7cb321f3a983c2df2be8ffbaf7975`
- sha256 de tirage_pilote.csv, exécution 2 : `96e7de6f76a3bea00eced724c1026730e5d7cb321f3a983c2df2be8ffbaf7975`
- Résultat : identiques (cadre_documents.csv et segments_perimetre_v2.csv également identiques octet pour octet : True).

## 2. Contrôles

- Aucun segment_id en double : OK (452 lignes, 452 segment_id distincts).
- Aucune unité documentaire tirée deux fois dans une strate : OK (96 unités tirées).
- Aucun document exclu du cadre dans le tirage : OK.

## 3. Effectifs du tirage principal par strate (cible section 5.1)

| Lot | Strate | Documents principal (cible) | Segments principal (cible) | Documents de réserve (cible 5) | Segments de réserve des docs principaux (cible 3 × docs) |
|---|---|---|---|---|---|
| lot1 | S1 | 10 (10) | 20 (20) | 1 | 30 (30) |
| lot1 | S2 | 7 (10) | 13 (20) | 0 | 7 (21) |
| lot1 | S3 | 9 (10) | 18 (20) | 0 | 27 (27) |
| lot1 | S4 | 9 (10) | 18 (20) | 0 | 27 (27) |
| lot2 | S1 | 12 (12) | 24 (24) | 3 | 36 (36) |
| lot2 | S2 | 12 (12) | 24 (24) | 1 | 31 (36) |
| lot2 | S3 | 12 (12) | 24 (24) | 5 | 36 (36) |
| lot2 | S4 | 12 (12) | 24 (24) | 3 | 32 (36) |

## 4. Explication des écarts

- lot1 S2 (7 documents au lieu de 10), S3 et S4 (9 au lieu de 10), réserves incomplètes au lot 1 : le lot 1 ne compte que 14 fonds collectés, et la règle « aucun fonds déjà couvert dans la strate » refuse les autres unités du même fonds (versions de pays ou de langue). S2 a en outre perdu 5 factsheets réservées aux professionnels et 2 factsheets de paires. Le parcours complet, unité par unité, avec le motif de chaque refus, est dans journal_tirage.md (section 6). Aucun complément manuel.
- Plafond par maison : 3 refus seulement, tous au lot 1 et tous pour « BlackRock (iShares) » : 2 KID IE00B3X84Y31 en S1, après que le tirage principal était déjà complet, et 1 prospectus LU2575673467 en S3. Avec la lecture littérale « n'a pas déjà fourni plus de 4 » (une 5e unité permise), lot1 S3 aurait eu ce prospectus au rang 9, puis FR0010241059 au rang 10, soit 10 documents. Lot1 S1 aurait eu un KID IE00B3X84Y31 de plus en réserve. La lecture retenue est « au plus 40 % », soit 4 (voir journal).
- Segments manquants dans un document (1 seul segment principal) : LOT1-LU0297942194-FR-Factsheet-0c9e8b88 et LOT2-LU0599613147-IT-Factsheet-4c6ae5ba n'ont que des segments perimetre_v2 « oui » adjacents ou un seul utilisable après la règle d'adjacence ; réserves de segments incomplètes dans quelques documents courts (liste dans journal_tirage.md). Le cadre ne permettait pas mieux ; rien n'a été complété.

## 5. Anomalie à signaler

- LOT2-FR0013532363-FR-KID-68889a53 : le même fichier (sha256 68889a53…, PDF unique « DIC + Prospectus » Colville, signalé le 16/11 comme « fichier erroné : pointe vers le prospectus ») est listé comme KID et comme prospectus. Par la règle 4.1, la ligne de référence est le plus petit doc_id (la ligne KID) : l'unité est donc en S1 (KID), avec 391 segments dont une grande partie vient du prospectus. Elle est tirée au lot 2, strate S1, rang 7 du tirage principal. Je ne l'ai ni retirée ni remplacée (section 8) ; c'est à toi de décider si elle doit être écartée par le codeur (règle de remplacement 5.4) ou si le cadre doit être relancé avec une règle explicite pour ce cas.
