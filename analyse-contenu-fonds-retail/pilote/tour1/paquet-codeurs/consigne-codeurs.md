# Consigne de codage – pilote, tour 1 (lot 1)

Version du 17 novembre 2026. La même consigne est donnée à chaque codeur.

## 1. Ton rôle

Tu es l'un des deux codeurs d'un pilote d'analyse de contenu. Le pilote porte sur des documents d'information destinés aux investisseurs de détail dans des fonds européens : documents d'informations clés (KID), factsheets, prospectus, rapports.

Ta tâche : **classer chaque segment de texte dans un code du codebook**, et le décrire avec quatre facettes. Tu ne juges pas si le document est bon, clair, complet ou conforme. Tu dis seulement de quoi parle le segment.

Un autre codeur fait le même travail, sur les mêmes segments, sans que vous vous voyiez. On compare ensuite vos codes pour savoir si le codebook est assez clair pour que deux codeurs classent de la même façon. Ce qu'on teste, c'est le codebook, pas toi : code honnêtement, même quand tu hésites, et signale tes hésitations.

## 2. Ce que tu reçois

1. **`consigne_codeurs.md`** : la présente consigne.
2. **`codebook_codeurs.md`** : les 52 codes, les 23 règles de frontière et les facettes. C'est ta seule référence.
3. **`segments_a_coder_lot1.csv`** : 63 segments, une ligne par segment.

Colonnes du fichier de segments :

| Colonne | Contenu | Usage |
|---|---|---|
| `id_codage` | identifiant neutre (L1-001…) | à recopier dans ta sortie |
| `type_document` | KID, Factsheet, Prospectus, Rapport, Fiche_locale | contexte |
| `langue_origine` | de, fr, en… | contexte |
| `titre_section` | titre de la section où se trouve le segment | contexte |
| `texte_original` | **le texte à coder**, dans sa langue | **à coder** |
| `texte_affichage` | le même texte, où les grands blancs de mise en page sont remplacés par « \| » | aide à la lecture des tableaux |
| `segment_precedent`, `segment_suivant` | les segments voisins dans le document | contexte seulement, **à ne pas coder** |
| `texte_en`, `statut_en` | une traduction automatique en anglais, non révisée, quand elle existe | aide seulement, peut être fausse |

## 3. Comment coder un segment

1. **Lis le codebook en entier** avant de commencer.
2. Pour chaque segment, dans l'ordre du fichier :
   - lis `texte_original` (et `texte_affichage` pour les tableaux) ;
   - lis le titre de section et les segments voisins seulement pour comprendre de quoi il s'agit ;
   - choisis le **code principal** ;
   - ajoute, si besoin, jusqu'à **deux codes secondaires** ;
   - remplis les quatre facettes ;
   - si tu hésites entre deux codes pour le code principal, indique ton **code alternatif** ;
   - écris une justification courte.
3. À la fin, relis tes codes une fois pour vérifier que tu as traité de la même façon des segments semblables. Tu peux corriger ta propre décision ; tu ne consultes jamais l'autre codeur.

## 4. Règles de codage

**R1 – Un seul code principal.** Chaque segment reçoit exactement un code principal. Si le segment contient plusieurs propositions de codes différents, le code principal est celui de la proposition qui occupe **le plus de texte**. En cas d'égalité, c'est celui de la première proposition.

**R2 – Codes secondaires.** Les autres propositions du segment, si elles relèvent d'un autre code, vont en codes secondaires : deux au plus, par ordre d'importance dans le segment. Ne découpe jamais le segment. Cette règle remplace, pour ce pilote, la mention « segment mixte découpé en deux » de la règle de frontière 3.

**R3 – Coder le segment, pas son contexte.** Le code porte sur ce que dit le segment. Le titre de section et les voisins servent seulement à comprendre le segment, et en particulier à compléter un libellé absent. Exemple : un segment « 0,3 % du montant investi par an » sous le titre « Frais courants » se code F1, car le titre dit de quoi est la valeur. En revanche, le contexte ne change jamais le sujet d'un segment qui a son propre contenu : un paragraphe sur la politique d'investissement placé sous un titre « Frais » reste en B2.

**R4 – Lignes de tableau.** Une ligne libellé-valeur se code selon le sens du libellé. « Incidence des coûts annuels | 7,5 % » → F2. « Coûts de sortie | 0 EUR » → F1. « Scénario défavorable | … » → E1. Si le segment contient plusieurs lignes de tableau qui relèvent de codes différents, applique R1 et R2 : le code principal est celui des lignes qui occupent le plus de texte, les autres vont en codes secondaires.

**R5 – Facettes.** La temporalité et la fonction décrivent la proposition du code principal. Les marqueurs durabilité et gouvernance portent sur tout le segment. Pour un segment codé Z2, mets par convention `temporalite = sans_objet` et `fonction = informer`.

**R6 – Langue.** Tu codes le texte original. La traduction anglaise n'est qu'une aide : en cas d'écart, l'original fait foi.

**R7 – Type de document.** Le code ne dépend pas du type de document. Une même phrase reçoit le même code dans un KID ou dans une factsheet.

**R8 – Frontières.** Quand deux codes sont possibles, applique la règle de frontière du codebook (section 2). Si aucune règle ne tranche, choisis le code dont la définition correspond le mieux, mets l'autre en code alternatif et explique-le.

**R9 – Z1 et Z2.** Z1 : le segment apporte une information à l'investisseur mais aucun code ne convient (dis pourquoi dans la remarque). Z2 : le segment n'apporte aucune information à l'investisseur (mise en page, élément technique). Ne te sers pas de Z1 pour éviter un choix difficile entre deux codes : dans ce cas, choisis et indique le code alternatif.

**R10 – Rien d'extérieur.** Tu ne cherches aucune information sur le fonds, la société ou le document en dehors du fichier. Tu ne fais aucune recherche sur internet. Tu ne déduis rien qui ne soit pas dans le segment ou dans son contexte (titre, voisins).

**R11 – Autonomie.** Tu travailles seul, du début à la fin, sans poser de question. Si un cas n'est pas couvert, décide selon la définition la plus proche, mets ta confiance à `basse` et explique le cas dans `remarque_codebook`.

## 5. Ce que tu livres

**Fichier 1 : `codage_<ta lettre>_lot1.csv`** (A ou B, la lettre t'est donnée par l'utilisateur), encodé en UTF-8, séparateur virgule, une ligne d'en-tête puis une ligne par segment (**63 lignes**, autant que dans le fichier reçu), dans l'ordre du fichier reçu. Les champs qui contiennent une virgule ou un guillemet sont mis entre guillemets (CSV standard). Colonnes, dans cet ordre :

| Colonne | Valeurs |
|---|---|
| `id_codage` | recopié du fichier reçu |
| `code_principal` | un code du codebook (A1 à Z2) |
| `codes_secondaires` | 0 à 2 codes, séparés par « ; », vide sinon |
| `code_alternatif` | un code différent du code principal si tu as hésité, vide sinon |
| `temporalite` | `regle`, `observe`, `projete` ou `sans_objet` |
| `fonction` | `informer`, `avertir`, `promouvoir` ou `orienter` |
| `durabilite` | `oui` ou `non` |
| `gouvernance` | `oui` ou `non` |
| `confiance` | `haute` (aucune hésitation), `moyenne` (hésitation tranchée par une règle de frontière ou une définition), `basse` (choix incertain, cas non couvert) |
| `justification` | 25 mots au plus, en français : pourquoi ce code principal |
| `remarque_codebook` | vide, ou une difficulté du codebook (définition floue, frontière manquante, code absent) |

**Fichier 2 : `compte_rendu_codage_<ta lettre>_lot1.md`**, court :

- nombre de segments par code principal ;
- nombre de segments par niveau de confiance ;
- les cinq difficultés les plus fréquentes du codebook, avec les `id_codage` concernés ;
- les codes que tu as trouvés les plus difficiles à distinguer, et pourquoi.

## 6. Auto-contrôle avant de livrer

- 63 lignes, chaque `id_codage` présent une fois et un seul.
- Chaque code est un code existant du codebook. Seuls `codes_secondaires`, `code_alternatif` et `remarque_codebook` peuvent être vides.
- Aucun code secondaire ni code alternatif identique au code principal ; pas plus de deux codes secondaires.
- Les valeurs des facettes sont exactement celles de la section 5.

## 7. Ce que tu ne fais pas

- Tu ne modifies, ne corriges, ne traduis ni ne découpes aucun segment.
- Tu ne crées pas de nouveau code : si aucun code ne convient, utilise Z1 et explique-le dans `remarque_codebook`.
- Tu ne cherches pas à savoir comment l'autre codeur a codé, et tu ne demandes pas de corrigé.
- Tu n'utilises aucune source extérieure.
