# Gouvernance

## Rôles

| Rôle | Qui | Ce qu'il fait |
|---|---|---|
| Décideur | à compléter | Tranche les propositions ; valide les versions du codebook et les livrables |
| Contributeur | à compléter | Rédige des propositions, des analyses, des fichiers ; peut coder au pilote |
| Relecteur | à compléter | Relit les pull requests et les propositions ; signale les incohérences |
| Claude (analyste) | assistant IA | Propose des options argumentées avec une recommandation, prépare les consignes, scripts et analyses ; ne décide pas et ne code pas au pilote |

## Passer d'une proposition à une décision

1. **Proposer** : une *issue* GitHub avec l'étiquette `proposition` : contexte, options (au moins deux, illustrées), recommandation.
2. **Discuter** : les relecteurs commentent dans l'issue.
3. **Décider** : un décideur tranche dans l'issue.
4. **Consigner** : une fiche `decisions/D-xxx.md` et une ligne dans `decisions/journal.md`, par pull request.
5. **Appliquer** : les fichiers concernés sont modifiés dans la même pull request ou une suivante, qui renvoie à la décision.

## Modifications

- Toute modification passe par une *pull request* relue par au moins un relecteur, puis fusionnée dans `main`.
- Une branche par sujet : `section/…`, `decision/D-xxx-…`, `codebook/v3.1`, `pilote/tour2`.
- Le codebook ne change de version qu'après une décision (v3 → v3.1 → v4). Le `CHANGELOG.md` renvoie aux décisions.

## Indépendance des codeurs pendant un tour de pilote

Pendant un tour de codage, chaque codeur travaille seul : il ne voit que son paquet (consigne, codebook, unités à coder), ni le travail de l'autre codeur, ni les analyses en cours. Au tour 2, les codeurs sont des humains sans accès au dépôt : paquets et retours passent par Dropbox (une demande de fichiers par codeur). La règle prend fin à la clôture du tour.

## Conventions

- Langue : français.
- Noms : minuscules, tirets, sans accents ni espaces ; dates AAAA-MM-JJ.
- Données tabulaires en CSV UTF-8 (une modification apparaît ligne par ligne) ; textes en markdown.
- Fichiers de plus de 5 Mo, PDF de tiers et archives : Dropbox, référencés par chemin et sha256 dans `corpus/references.md`.
- Chaque fichier a un statut dans `INDEX.md` : brouillon, validé, archivé (trace d'une étape close).
