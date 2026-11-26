# Mission 3 – Changement d'approche : du corpus complet au tirage des segments du pilote

17 novembre 2026

Tu as livré les lots 1 et 2, l'annexe Singapour, puis la consolidation et son contrôle qualité. Ce travail est accepté tel quel : le corpus est complet, ses limites sont documentées, et tu n'as rien à refaire. Cette mission change la façon dont on utilise ce corpus. Lis d'abord les sections 1 et 2 : elles expliquent pourquoi, et sur quelles données.

## 1. Pourquoi on change d'approche

Jusqu'ici, la règle était : texte intégral de chaque document, découpé en segments par une règle mécanique. Elle a bien fonctionné, mais ton contrôle qualité montre qu'elle produit des volumes que personne ne peut coder, et surtout un corpus déséquilibré :

- **Volumes :** 347 476 segments au lot 1, 212 769 au lot 2, 45 671 pour l'annexe Singapour.
- **Déséquilibre entre types de documents :** au lot 1, un KID donne environ 25 segments, une factsheet environ 20, un avis environ 9, alors qu'un rapport donne environ 4 400 segments et un prospectus environ 4 900. Les KID et les factsheets ne représentent qu'environ 1 % des segments : un tirage au hasard sur l'ensemble ne tomberait presque jamais dessus.
- **Doublons :** 17 lignes du lot 1 et 52 du lot 2 pointent vers un fichier identique (même sha256). Un même rapport Vanguard est listé 15 fois, un même prospectus 14 fois. Les décomptes de segments sont gonflés d'autant. Il y a en réalité 152 textes uniques au lot 1 et 116 au lot 2.
- **Périmètre imparfait :** dans les dix documents que tu as détaillés, des titres de compartiments coupés sur deux lignes sont classés « partie générale », des annexes SFDR de prospectus restent « oui », des lignes de rapport sont classées « frais » à cause d'un mot-clé alors qu'elles n'en sont pas, et des listes de titres en portefeuille (des données, pas du texte d'information) restent « oui ».
- **Mise en page :** 80 documents ont des colonnes mélangées, et des segments dépassent 1 700 mots.
- **Mentions professionnelles :** 15 documents portent eux-mêmes la mention « réservé aux professionnels ».

Ce n'est pas une erreur de ta part : tu as appliqué les règles à la lettre. C'est la règle qui doit changer.

**Ce que fait le projet avec le corpus.** Une équipe de codeurs lira un petit échantillon de segments, environ 80 au lot 1 et 96 au lot 2, pour tester une grille de lecture. Cet échantillon doit être tiré au hasard, de façon reproductible, et équilibré entre les types de documents. Tu ne connais pas cette grille et tu ne dois pas la connaître : tu ne choisis, ne retires ni ne remplaces aucun segment à la main.

## 2. Ce qui ne change pas

- Les archives livrées, le manifeste, le texte intégral et les segments existants restent inchangés. Tu ne modifies, ne supprimes et n'écrases rien.
- Pas de nouvelle collecte, pas de site, pas de traduction. Tu travailles uniquement sur ce qui est déjà livré.
- La neutralité : aucun segment n'est choisi selon son sens.

## 3. Ce qui change, en une phrase

On ne tire plus parmi tous les segments : on construit d'abord un cadre de tirage propre (textes uniques, périmètre resserré), puis on tire en deux temps (d'abord des documents, ensuite des segments dans ces documents), avec une liste de réserve ordonnée pour les remplacements.

## 4. Construire le cadre de tirage

### 4.1 Textes uniques

Regroupe les lignes du manifeste qui partagent le même sha256. Chaque groupe est une **unité documentaire** : tu gardes une seule ligne de référence (le plus petit `doc_id` dans l'ordre alphabétique) et tu notes dans `lignes_manifeste` toutes les lignes du groupe, ainsi que la liste de leurs ISIN dans `fonds_concernes`. Les segments d'une unité documentaire sont générés une seule fois.

### 4.2 Documents exclus du cadre (ils restent dans le corpus)

Un document sort du cadre de tirage dans les cas suivants. Tu enregistres le motif dans `motif_exclusion_cadre` :

- fichier tronqué ou texte absent (`tronque = oui`) ;
- document qui porte lui-même une mention de réserve aux professionnels (`reserve_professionnels = oui`) ;
- document de l'annexe Singapour (`annexe_SG`, qui n'a pas été tiré au hasard) ;
- avis et paires (flux séparé, non tirés dans ce pilote).

### 4.3 Périmètre resserré des segments (`perimetre_v2`)

Tu recalcules un champ `perimetre_v2` (« oui » ou « non ») pour chaque segment, sans écraser `perimetre`. La règle reste mécanique, fondée sur la structure du document et jamais sur le sens du texte. Avant de comparer les titres, tu recolles les lignes de titre consécutives qui forment un seul intitulé coupé par la mise en page.

- **KID, factsheets, fiches locales, bulletins trimestriels :** « oui », sauf les exclusions générales ci-dessous.
- **Prospectus :** « oui » pour la partie générale et pour la section propre au fonds (titre contenant le nom du fonds ou son ISIN). « non » pour les sections des autres compartiments, les annexes qui sont de simples listes (adresses, sous-dépositaires, liste des fonds) et les annexes SFDR (titres ou textes contenant par exemple « Legal entity identifier », « Product name », « Sustainability indicators », « Annexe II », « Annexe III », « Règlement délégué (UE) 2022/1288 »). Cette liste d'exemples n'est pas limitative : tu consignes chaque motif réellement utilisé.
- **Rapports annuels et semestriels :** « oui » pour le commentaire de gestion, la performance et les frais effectifs. « non » pour les états financiers et leurs notes, le rapport d'audit, et toutes les listes de positions et de titres en portefeuille. Pour classer en « frais », tu utilises le titre de section complet, pas un mot isolé : un titre comme « Contributions à la performance de l'exercice (hors frais) » n'est pas un titre de frais.
- **Exclusions générales pour tous les types :**
  - segment où les chiffres représentent plus de la moitié des caractères non blancs (tableau chiffré, liste de valeurs) ;
  - segment qui contient cinq espaces consécutifs ou plus (colonnes mélangées par la mise en page) ;
  - segment de moins de 4 mots (déjà fusionné autant que possible) ;
  - segment dont le texte est identique à un segment déjà retenu dans la même unité documentaire (répétition de bas de page, mentions identiques).
- **Cas non tranché :** tu le classes « oui » et tu le consignes, sauf pour les trois situations suivantes, où le doute vaut « non » : liste de positions, annexe SFDR, rapport d'audit.

Tu enregistres pour chaque segment la règle appliquée dans `regle_perimetre_v2`.

### 4.4 Cadre documentaire (`cadre_documents.csv`)

Une ligne par unité documentaire, avec : `doc_id`, `sha256`, `lot`, `strate`, `type_document`, `fonds_concernes`, `maison_gestion`, `pays_distribution`, `langue_origine`, `statut_en`, `n_segments_total`, `n_segments_perimetre_v2_oui`, `exclu_du_cadre` (oui ou non) et `motif_exclusion_cadre`. Ce fichier est léger : il me sert à vérifier que le cadre est cohérent avant le tirage.

## 5. Le tirage en deux temps

### 5.1 Paramètres (à écrire en tête du script, pas à modifier)

- **Graine :** 2026. Pour chaque couple (lot, strate), le générateur aléatoire est initialisé avec la chaîne `"2026-<lot>-<strate>"` (par exemple `"2026-lot1-S3"`). Avant tout tirage, tu tries la liste des unités documentaires par `doc_id` dans l'ordre alphabétique, pour que le résultat ne dépende pas de l'ordre des fichiers.
- **Lots :** le tirage se fait séparément pour le lot 1 et pour le lot 2.
- **Strates (par type de document) :**
  - S1 : KID et fiches locales
  - S2 : factsheets
  - S3 : prospectus
  - S4 : rapports annuels, rapports semestriels et bulletins trimestriels
- **Segments à tirer par strate :** 20 au lot 1, 24 au lot 2. Total : 80 au lot 1 et 96 au lot 2.
- **Segments par document tiré :** 2. Le nombre de documents à tirer par strate est donc de 10 au lot 1 et de 12 au lot 2.
- **Réserve :** 5 documents de réserve par strate, et 3 segments de réserve par document tiré.

### 5.2 Temps 1 : tirer les documents

Pour chaque (lot, strate) :

1. Prends les unités documentaires de la strate qui ne sont pas exclues du cadre et qui ont au moins 2 segments `perimetre_v2 = oui`.
2. Mélange-les avec le générateur initialisé comme en 5.1.
3. Parcours la liste mélangée dans l'ordre et accepte une unité si **les deux conditions** sont vérifiées :
   - aucun de ses fonds (`fonds_concernes`) n'est déjà couvert par une unité acceptée dans cette strate ;
   - sa maison de gestion n'a pas déjà fourni plus de `ceil(0,4 × nombre de documents à tirer)` unités acceptées dans cette strate.
4. Les unités acceptées jusqu'au nombre cible forment le tirage principal. Les 5 suivantes, dans l'ordre, forment la réserve de documents.
5. Si le cadre ne permet pas d'atteindre le nombre cible, tu t'arrêtes là et tu le consignes : tu ne complètes pas à la main.

### 5.3 Temps 2 : tirer les segments dans chaque document

Pour chaque document du tirage principal et de la réserve :

1. Prends les segments `perimetre_v2 = oui` de l'unité documentaire.
2. Mélange-les avec un générateur initialisé par la chaîne `"2026-<lot>-<strate>-<doc_id>"`.
3. Retiens les segments dans l'ordre du mélange, en écartant tout segment dont la position (`ordre`) est adjacente à celle d'un segment déjà retenu.
4. Les 2 premiers segments sont le tirage principal. Les 3 suivants sont la réserve ordonnée de ce document.

### 5.4 Règle de remplacement (appliquée plus tard, pas par toi)

Si un codeur juge un segment hors périmètre ou inutilisable, il passe au premier segment de réserve du même document. S'il n'en reste plus, il passe au premier document de réserve de la même strate. Tu fournis donc les rangs de réserve, mais tu ne remplaces rien toi-même.

## 6. Ce que tu livres

Dans un dossier `tirage/` :

1. **`tirage_pilote.csv`** : une ligne par segment (tirage principal et réserve), avec : `lot`, `strate`, `rang_document` (1 à N pour le tirage principal, N+1 et suivants pour la réserve), `reserve_document` (oui ou non), `doc_id`, `sha256`, `fonds_concernes`, `maison_gestion`, `pays_distribution`, `type_document`, `langue_origine`, `rang_segment` (1 et 2 pour le tirage principal, 3 à 5 pour la réserve), `reserve_segment` (oui ou non), `segment_id`, `titre_section`, `page`, `n_mots`, `texte_original`, `texte_en` (seulement s'il est déjà aligné, sinon vide), `statut_en`, `regle_perimetre_v2`. Aucune traduction à ajouter.
2. **`cadre_documents.csv`** (section 4.4).
3. **`entonnoir.md`** : pour chaque lot et chaque strate, les effectifs à chaque étape du filtrage : unités documentaires totales, exclues du cadre par motif, segments totaux, `perimetre` (ancien) « oui », `perimetre_v2` « oui », segments exclus par chaque règle de la section 4.3.
4. **`tirage_script.py`** (ou équivalent) : le script complet qui reconstruit tout à partir des fichiers livrés, avec les paramètres de la section 5.1 écrits en clair en tête. En relançant ce script sur les mêmes fichiers, j'obtiens exactement le même `tirage_pilote.csv`.
5. **`journal_tirage.md`** : les règles de périmètre réellement utilisées (liste des motifs), les cas non tranchés, les documents où le cadre n'a pas permis d'atteindre la cible, et les anomalies.

## 7. Auto-contrôle avant de livrer

- Exécute le script deux fois de suite et vérifie que les deux `tirage_pilote.csv` sont identiques. Indique leur sha256.
- Vérifie qu'aucun `segment_id` n'apparaît deux fois, qu'aucune unité documentaire n'est tirée deux fois dans une strate, et qu'aucun document exclu du cadre n'apparaît dans le tirage.
- Compte pour chaque strate le nombre de documents et de segments du tirage principal et vérifie qu'il correspond à la section 5.1, sinon explique l'écart.

## 8. Ce que tu ne fais pas

- Tu ne choisis, ne retires, ne remplaces ni ne réordonnes aucun segment ou document à la main.
- Tu ne modifies aucun fichier déjà livré.
- Tu ne traduis rien, tu ne collectes rien.
- Tu ne cherches jamais à améliorer l'échantillon selon ce qu'il contient.

## 9. Livraison

Livre le dossier `tirage/` en une archive `tirage_2026-11-17.zip` avec son empreinte sha256, et un compte rendu court : nombre de documents et de segments tirés par lot et par strate, écarts à la cible, règles de périmètre les plus déclenchées, cas non tranchés, anomalies.

Si une règle ne couvre pas un cas, applique les principes de la section 2, consigne le cas dans le journal et continue.
