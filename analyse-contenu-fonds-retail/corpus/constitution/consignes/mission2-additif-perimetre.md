# Mission 2 – Additif « périmètre » (15 novembre 2026)

Additif envoyé au bot pendant la consolidation (texte tel que transmis).

Ne reprends pas ce que tu as déjà produit si cela est compatible. Ajoute ceci :

1. Nouveau champ `perimetre` dans segments.jsonl : "oui" ou "non". Tu conserves TOUS les segments, tu ne supprimes rien. Règle mécanique, identique pour tous les documents, fondée sur la structure du document et jamais sur le sens du texte :
   - KID, KIID, fiches locales de synthèse (KFS, PHS), factsheets, bulletins trimestriels : "oui" partout.
   - Prospectus (dont prospectus parapluie et enveloppes locales) : "oui" pour la partie générale et pour la section propre au fonds du manifeste, repérée par le nom du fonds ou son ISIN dans les titres. "non" pour les sections consacrées à d'autres compartiments et pour les annexes qui sont de simples listes.
   - Rapports annuels et semestriels : "oui" uniquement pour le commentaire de gestion, la performance, les positions et les frais effectifs. "non" pour les états financiers et leurs notes.
   - Si la règle ne permet pas de trancher, tu mets "oui" et tu consignes le cas.
2. Nouveau champ `regle_perimetre` : courte étiquette qui dit pourquoi le segment a cette valeur.
3. Dans controle_qualite.md, une section « Périmètre » : segments "oui" et "non" par type de document et par lot ; prospectus parapluie où la section propre au fonds n'a pas été repérée ; pour dix documents, les intitulés de section classés "oui" et "non".
4. Ne modifie ni texte_original, ni les identifiants de segments. Tu ne tires aucun échantillon.
5. Dédoublonnage : pour tout fichier identique (même sha256) utilisé par plusieurs lignes du manifeste, génère les segments une seule fois et liste toutes les lignes concernées dans `fonds_concernes` et `lignes_manifeste`.
6. Marque `tronque = oui` les documents dont le fichier source est tronqué ou illisible (par exemple LU0599613147) et exclus-les de perimetre = "oui".
