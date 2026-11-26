# Mission 4 – Contrôle de lisibilité et paquet de codage

17 novembre 2026

Le tirage v3 (`tirage_v3_2026-11-17.zip`) est accepté. Cette mission prépare les segments pour les codeurs. Tu travailles uniquement sur `tirage_v3/tirage_pilote.csv` (478 lignes : tirage principal et réserves). Tu ne modifies aucun fichier livré : tout ce que tu produis va dans un nouveau dossier `lisibilite/`.

## 1. Pourquoi cette étape

À la lecture du tirage v3, une partie des segments ne peut pas être codée : en-têtes seuls, colonnes de texte entremêlées, listes de chiffres sans libellé. Si chaque codeur écartait ces segments de son côté, ils ne coderaient plus les mêmes textes et la mesure d'accord deviendrait fausse. Le tri doit donc être fait **une seule fois, avant le codage, par toi**, avec des critères de forme écrits.

Tu ne connais pas la grille de codage et tu n'as pas à la connaître. Tu juges uniquement **la forme** du segment, jamais son sujet, son intérêt, sa qualité ou sa pertinence. Un avertissement juridique répétitif, une phrase publicitaire ou une mention de copyright sont des segments lisibles : ils sont retenus.

## 2. Critères de lisibilité

Tu évalues **les 478 lignes**, tirage principal et réserves. Tu lis `texte_affichage`, et `texte_original` en cas de doute sur la mise en page. Les champs `segment_precedent` et `segment_suivant` t'aident à comprendre le découpage, mais ta décision porte uniquement sur le segment lui-même.

**Étape 1 – Écart immédiat**

- **E1 – Colonnes entremêlées :** le segment juxtapose, sur les mêmes lignes, deux colonnes de texte rédigé, qu'elles appartiennent ou non au même passage. Lu ligne par ligne, il mélange deux textes. C'est un cas E1 même si une phrase courte reste lisible dans l'une des colonnes. Un tableau dont chaque ligne associe un libellé et des valeurs n'est pas un cas E1.

**Étape 2 – Retenu si au moins une de ces conditions est remplie**

- **R1 – Phrase :** au moins une suite de mots qui forme un énoncé ou une question compréhensible, même courte et même sans verbe principal (par exemple « Coûts de sortie : nous ne facturons pas de coût de sortie »). Un élément de liste rédigé compte comme une phrase.
- **R2 – Libellé et valeur :** une ligne de tableau ou une mention où une valeur est rattachée à son libellé (par exemple « Incidence des coûts annuels | 7,5 % | 3,6 % », « Ausgabeaufschlag | bis zu 5 % », « Période de détention recommandée : 5 ans »).
- **R3 – Identification :** une ligne qui identifie le produit ou le document : nom du fonds, classe de parts, ISIN, type de document, date du document, émetteur (par exemple « Fact Sheet | 31 October 2026 »).

**Étape 3 – Sinon, écarté, avec le premier motif qui s'applique**

- **E2 – En-tête seul :** titre de section ou en-têtes de colonnes sans aucune valeur (par exemple « OBJECTIF », « 1M | 3M | 6M | YTD | 1A »).
- **E3 – Mobilier de page :** entrée de sommaire, titre courant, numéro de page, adresse ou coordonnées qui ne nomment pas l'entité concernée, date isolée qui n'identifie pas le document.
- **E4 – Données sans libellé :** liste de positions ou de titres en portefeuille, suite de chiffres dont on ne peut pas dire à quoi ils se rapportent.
- **E5 – Fragment :** bout de phrase coupé au début et à la fin, de moins de cinq mots lisibles d'un seul tenant.

**En cas de doute, le segment est retenu**, et tu notes le doute en dix à vingt mots.

## 3. Remplacement

Pour chaque lot et chaque strate, tu reconstitues le jeu final ainsi :

1. Chaque segment du tirage principal retenu reste en place.
2. Un segment principal écarté est remplacé par le premier segment de réserve **du même document** (rangs 3, 4, puis 5) qui est retenu.
3. Si un document ne peut plus fournir de segment retenu, le manque est pris dans le **premier document de réserve de la même strate** (rangs N+1, N+2, etc.), en suivant l'ordre de ses segments (rangs 1 à 5) et en ne prenant que des segments retenus. Un document de réserve entamé est épuisé avant de passer au suivant.
4. Si la strate n'a plus de réserve, le manque reste un manque : tu le consignes et tu ne complètes rien.

Tu traites les remplacements dans l'ordre des documents principaux (`rang_document` croissant), puis, dans chaque document, dans l'ordre des segments principaux (`rang_segment` croissant). Chaque segment ne peut être utilisé qu'une fois. Les règles « un document par fonds et par strate » et le plafond par maison ont déjà été appliqués au tirage : tu ne les recalcules pas.

## 4. Paquet de codage

À partir du jeu final, tu produis un fichier par lot : `segments_a_coder_lot1.csv` et `segments_a_coder_lot2.csv`.

- **Ordre :** les segments sont mélangés avec un générateur initialisé par la chaîne `"2026-codage-<lot>"`, après un tri par `segment_id`, avec la même méthode de mélange que dans `tirage_script.py`. Les codeurs ne doivent pas voir les segments groupés par document ou par strate.
- **Identifiant neutre :** chaque segment reçoit un `id_codage` dans l'ordre du mélange (`L1-001`, `L1-002`… pour le lot 1 ; `L2-001`… pour le lot 2).
- **Colonnes, dans cet ordre :** `id_codage`, `type_document`, `langue_origine`, `titre_section`, `texte_affichage`, `segment_precedent`, `segment_suivant`, `texte_original`, `texte_en` (vide si absent), `statut_en`.
- **Colonnes à ne pas inclure :** maison de gestion, fonds, ISIN, pays, sha256, strate, règle de périmètre, rangs, `segment_id`. Elles ne servent pas au codage.

Tu produis aussi `correspondance.csv` (ce fichier n'est pas transmis aux codeurs) : `id_codage`, `segment_id`, `lot`, `strate`, `doc_id`, `maison_gestion`, `fonds_concernes`, `pays_distribution`, `rang_document`, `rang_segment`, `statut_final`.

## 5. Ce que tu livres dans `lisibilite/`

1. **`controle_lisibilite.csv`**, une ligne pour chacune des 478 lignes du tirage : `segment_id`, `lot`, `strate`, `doc_id`, `rang_document`, `rang_segment`, `reserve_document`, `reserve_segment`, `decision` (retenu ou écarté), `critere` (R1, R2, R3, E1 à E5), `note_doute` (vide sauf en cas de doute), `statut_final` (principal, remplaçant, réserve non utilisée ou écarté) et `remplace` (le `segment_id` remplacé, pour un remplaçant).
2. **`segments_a_coder_lot1.csv`** et **`segments_a_coder_lot2.csv`** (section 4).
3. **`correspondance.csv`** (section 4).
4. **`compte_rendu_lisibilite.md`**, avec :
   - pour chaque lot et chaque strate : segments principaux tirés, segments écartés par motif, segments remplacés et d'où vient le remplaçant, effectif final comparé à la cible (20 par strate au lot 1, 24 au lot 2), et manque éventuel ;
   - le taux de segments écartés par strate et par motif, calculé sur toutes les lignes évaluées ;
   - la liste des cas douteux ;
   - l'auto-contrôle de la section 6.

## 6. Auto-contrôle

- **Constance du tri :** une fois toutes les décisions prises, tire 40 lignes au hasard parmi les 478 (générateur initialisé par `"2026-recontrole-lisibilite"`, après un tri par `segment_id`, même méthode). Réévalue-les **sans regarder ta première décision**. Indique le nombre de décisions identiques et liste les écarts.
- **Contrôles de cohérence :** aucun `segment_id` n'est utilisé deux fois ; aucun segment écarté ne figure dans les paquets de codage ; le nombre de lignes des paquets correspond aux effectifs finaux du compte rendu ; chaque `id_codage` figure dans `correspondance.csv`.

## 7. Ce que tu ne fais pas

- Tu ne juges jamais le sujet, l'intérêt ou la qualité d'un segment, et tu ne cherches pas à équilibrer les thèmes.
- Tu ne modifies, ne corriges, ne traduis et ne redécoupes aucun texte.
- Tu ne complètes pas une strate au-delà des règles de remplacement.
- Tu ne modifies aucun fichier déjà livré.

## 8. Livraison

Une archive `lisibilite_<date du jour>.zip` qui contient le dossier `lisibilite/`, avec son empreinte sha256, et un compte rendu court : effectifs finaux par lot et par strate, taux d'écart par strate, résultat de l'auto-contrôle, anomalies.

Si un cas n'est pas couvert, applique la règle « en cas de doute, retenu », consigne-le et continue.
