# Mission complémentaire – consolidation du corpus (lots 1 et 2)

15 novembre 2026

Tu as livré les lots 1 et 2. Cette mission ne recommence pas la collecte : elle prépare le corpus pour le codage. Tu travailles uniquement sur les fichiers que tu as déjà produits (archives `lot1_2026-11-15.zip` et `lot2_2026-11-15.zip`, annexe Singapour comprise). Tu n'ouvres aucun site, tu ne télécharges rien, tu ne traduis rien. Tu écris en français dans le journal et les notes, et tu ne modifies jamais un fichier existant : tout ce que tu produis est nouveau.

## 1. Principes

- **Neutralité :** tu ne juges pas les contenus. Aucun segment, aucun document n'est retiré, favorisé ou classé selon son sens.
- **Fidélité :** le texte original est la référence. Tu ne le corriges pas, tu ne le nettoies pas.
- **Honnêteté sur les trous :** ce que tu ne peux pas faire (structure illisible, fichier tronqué, alignement impossible), tu le consignes dans le contrôle qualité, sans le combler.
- **Reproductibilité :** les règles ci-dessous sont les seules règles de segmentation. Tu les appliques de la même façon à tous les documents.

## 2. Ce que tu produis

À la racine d'un nouveau dossier `consolidation/` :

1. **`corpus.jsonl`** : une ligne par document (lot 1, lot 2 et annexe Singapour). Champs : `doc_id`, `lot` (`lot1`, `lot2` ou `annexe_SG`), les métadonnées du manifeste (ISIN, fonds, maison de gestion, famille, type, pays, langue d'origine, date du document, URL, sha256), `texte_original` (texte intégral) et `texte_en` (texte intégral anglais quand il existe, sinon `null`).
2. **`segments.jsonl`** : une ligne par segment, selon la règle de la section 3.
3. **`manifeste_complete.csv`** : le manifeste existant avec les colonnes ajoutées de la section 4.
4. **`controle_qualite.md`** : le rapport de la section 5.
5. **`journal_consolidation.md`** : ce que tu as fait, document par document en cas d'anomalie.

Le corpus doit rester léger : pas de PDF dans ces fichiers.

## 3. Règle de segmentation

Tu segmentes `texte_original.txt`, dans la langue d'origine. La règle est mécanique et identique pour tous les documents :

- Un segment = un paragraphe, un élément de liste ou une ligne de tableau (cellules séparées par « | »). Dans le fichier texte, un paragraphe est un bloc séparé par une ligne vide ; une ligne de tableau est une ligne qui contient « | ».
- Un titre n'est pas un segment : c'est une ligne de douze mots ou moins, sans point final, suivie d'un paragraphe, ou une ligne que l'extraction a marquée comme titre. Un titre alimente `titre_section` pour les segments qui suivent.
- Les numéros de page et les en-têtes ou pieds de page répétés ne sont pas des segments. Ils restent dans le texte intégral.
- Un segment de moins de quatre mots est fusionné avec le suivant.
- Les avertissements répétitifs et les mentions légales sont segmentés comme le reste. Tu ne cherches jamais à découper ou regrouper selon le sens.
- Si la structure du fichier texte est trop pauvre pour appliquer la règle, tu peux réextraire ce document depuis son PDF avec la mise en page conservée, sans modifier `texte_original.txt`. Tu consignes ce cas dans le contrôle qualité.

Champs de `segments.jsonl` :

| Champ | Contenu |
|---|---|
| `segment_id` | identifiant stable : `doc_id` + numéro d'ordre |
| `doc_id` | document d'origine |
| `ordre` | position dans le document |
| `titre_section` | titre le plus récent, ou `null` |
| `page` | numéro de page si connu, sinon `null` |
| `texte_original` | le segment dans sa langue |
| `langue_origine` | code de langue |
| `texte_en` | le segment en anglais **uniquement** s'il est directement aligné (voir ci-dessous), sinon `null` |
| `statut_en` | `original_anglais`, `traduit_automatique_aligne` ou `absent` |
| `n_mots` | nombre de mots du texte original |
| `fonds_concernes` | liste des ISIN couverts par ce document (plusieurs si prospectus parapluie) |

Règle pour `texte_en` : si le document est en anglais, `texte_en` est identique au texte original et `statut_en` vaut `original_anglais`. Si le document a déjà une version traduite, tu remplis `texte_en` seulement quand l'alignement avec le segment est évident (même nombre de phrases ou de lignes de tableau). Sinon tu laisses `null` avec `statut_en = absent`. Tu n'essaies pas d'améliorer ni de compléter une traduction.

## 4. Colonnes à ajouter au manifeste

- **`lot`** : `lot1`, `lot2` ou `annexe_SG`.
- **`reserve_professionnels`** : `oui` si le document porte lui-même une mention qui le réserve aux professionnels ou aux investisseurs institutionnels (par exemple « nur für professionelle Anleger », « for professional investors only »), `non` si le document n'en porte aucune, `inconnu` si le texte n'est pas disponible. Tu recopies la mention dans la colonne `mention_reserve`. Tu ne juges pas : tu notes ce que le document dit.
- **`tronque`** : `oui` si le fichier source est tronqué ou si l'extraction est incomplète (par exemple le PDF Ossiam LU0599613147), `non` sinon.
- **`statut_traduction`** : `original_anglais`, `traduit_automatique` ou `non_traduit`, d'après l'état actuel.
- **`doc_partage`** : `oui` si un même fichier sert plusieurs fonds (prospectus parapluie), avec la liste des ISIN dans `fonds_concernes`.

## 5. Contrôle qualité (`controle_qualite.md`)

Pour chaque lot et pour l'annexe, tu rapportes :

1. **Identité des fonds :** préfixe ISIN de chaque fonds (UE, hors GB et CH), une seule classe de parts par fonds, document en dehors de la fenêtre de dates (novembre 2024 à novembre 2026 pour les documents).
2. **Intégrité :** sha256 recalculé de chaque fichier original, comparé à la valeur du manifeste ; écarts éventuels.
3. **Textes :** documents dont le texte est vide, très court (moins de 200 mots), issu d'un scan ou tronqué ; doublons exacts (même sha256).
4. **Effectifs :** nombre de fonds, de documents et de segments par lot, par pays, par type de document, par famille de produit et par maison de gestion, avec la part de chaque maison dans le total des documents du lot.
5. **Écart aux cibles :** comparaison avec les cibles de la consigne (21 fonds et environ 85 documents au lot 1 ; 28 fonds et environ 110 documents au lot 2), sans chercher à les combler.
6. **Traduction :** nombre de documents et de segments par `statut_traduction` ; liste des documents non traduits, avec leur langue.
7. **Documents partagés :** liste des fichiers qui couvrent plusieurs fonds.
8. **Segmentation :** nombre moyen et nombre maximal de mots par segment ; liste des documents où la règle n'a pu s'appliquer qu'en mode dégradé (paragraphes séparés par lignes vides seulement, ou réextraction depuis le PDF).

## 6. Ce que tu ne fais pas

- Tu ne collectes aucun nouveau document et tu n'ouvres aucun site.
- Tu ne traduis rien et tu n'améliores aucune traduction existante.
- Tu ne retires, ne regroupes et n'ordonnes aucun segment selon son contenu.
- Tu n'écrases aucun fichier existant des archives livrées.
- Tu ne tires aucun échantillon de segments : le tirage est fait ensuite par l'analyste, avec la graine 2026.

## 7. Livraison

Tu livres, pour chaque lot et pour l'annexe, dans l'ordre : lot 1, lot 2, annexe Singapour. Si le temps manque, tu livres d'abord ce qui est terminé et tu précises ce qui reste.

Livrables :

- Une archive `consolidation_2026-11-15.zip` qui contient le dossier `consolidation/`, avec son empreinte sha256.
- Un compte rendu court : nombre de documents et de segments produits, anomalies du contrôle qualité qui demandent une décision, documents non traités.

Si une règle ne couvre pas un cas, applique les principes de la section 1, consigne le cas dans le journal et continue.
