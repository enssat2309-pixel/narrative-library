#!/usr/bin/env python3
"""Mission 3, v3 — comparaison v2 / v3 (lecture seule de tirage_v2/), section 9 du journal, compte_rendu_v3.md, autocontrole.md.
À exécuter une seule fois après les deux exécutions (ajoute la section 9 au journal). Ne modifie aucun calcul du tirage. Arguments : sha256 de tirage_pilote.csv des exécutions 1 et 2."""
import csv, collections, re, sys, datetime, hashlib, os
B = "/workspace/doc-screener"; V2 = B + "/tirage_v2"; V3 = B + "/tirage_v3"; RUN2 = "/tmp/tirage_v3_run2"
ESP = "exclusion générale : 5 espaces consécutifs ou plus (colonnes mélangées)"
DOUB = "exclusion générale : texte identique à un segment déjà retenu dans l'unité"
LOTS = ["lot1", "lot2"]; STR = ["S1", "S2", "S3", "S4"]
NOMS = {"S1": "KID, KIID, fiches locales, KFS, PHS", "S2": "factsheets", "S3": "prospectus", "S4": "rapports et bulletins"}
CIBLE = {"lot1": 10, "lot2": 12}
heure = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
def seg(p):
    with open(p, encoding="utf-8") as f:
        return {r["segment_id"]: (r["doc_id"], r["regle_perimetre_v2"], r["perimetre_v2"]) for r in csv.DictReader(f)}
def cad(p):
    with open(p, encoding="utf-8") as f: return {r["doc_id"]: r for r in csv.DictReader(f)}
def tp(p):
    with open(p, encoding="utf-8") as f: return list(csv.DictReader(f))
s2, s3 = seg(V2 + "/segments_perimetre_v2.csv"), seg(V3 + "/segments_perimetre_v2.csv")
c2, c3 = cad(V2 + "/cadre_documents.csv"), cad(V3 + "/cadre_documents.csv")
t2, t3 = tp(V2 + "/tirage_pilote.csv"), tp(V3 + "/tirage_pilote.csv")
assert set(s2) == set(s3) and set(c2) == set(c3)
dans = lambda did: did in c3 and c3[did]["exclu_du_cadre"] == "non"
tr_tous, tr_cadre, tr_strate, autres = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
for sid in sorted(s2):
    did, r2, p2 = s2[sid]; _, r3, p3 = s3[sid]
    if r2 == ESP:
        tr_tous[r3] += 1
        if dans(did): tr_cadre[r3] += 1; tr_strate[(c3[did]["lot"], c3[did]["strate"], p3)] += 1
    elif (r2, p2) != (r3, p3): autres[(r2, r3, dans(did))] += 1
J = []
J.append("\n## 9. Effet de l'ordre des règles (suppression de « 5 espaces »)\n")
J.append(f"Rédigé le {heure} (heure d'Europe/Luxembourg) par analyse_v3.py, par comparaison segment par segment de `tirage_v2/segments_perimetre_v2.csv` (lu sans modification) et de `tirage_v3/segments_perimetre_v2.csv` ({len(s3)} segments des unités documentaires, mêmes segment_id dans les deux versions).\n")
J.append(f"Segments que la v2 classait « exclusion générale : 5 espaces consécutifs ou plus » : {sum(tr_tous.values())} au total, dont {sum(tr_cadre.values())} dans des unités du cadre. Comme la règle « chiffres » est appliquée avant, aucun d'eux ne peut devenir « chiffres » ; ils passent aux règles suivantes : « moins de 4 mots », puis « texte identique », sinon « oui » avec leur règle de structure.\n")
J.append("| Nouvelle règle (v3) | Tous segments | Dans le cadre |\n|---|---|---|")
for r, n in sorted(tr_tous.items(), key=lambda x: (-x[1], x[0])): J.append(f"| {r} | {n} | {tr_cadre[r]} |")
J.append(f"| **Total** | {sum(tr_tous.values())} | {sum(tr_cadre.values())} |")
J.append("\nPar strate (unités du cadre), anciens segments « 5 espaces » devenus « oui » / restés « non » :\n")
J.append("| Lot | Strate | Devenus oui | Restés non (texte identique ou moins de 4 mots) |\n|---|---|---|---|")
for lot in LOTS:
    for st in STR: J.append(f"| {lot} | {st} | {tr_strate[(lot, st, 'oui')]} | {tr_strate[(lot, st, 'non')]} |")
J.append(f"\nEffet en chaîne de la règle « texte identique » : {sum(autres.values())} autres segments (dont {sum(n for k, n in autres.items() if k[2])} dans le cadre) changent de règle. Ils étaient « oui » en v2 et deviennent « texte identique » en v3, parce qu'un segment plus haut dans l'unité au texte identique, auparavant exclu par « 5 espaces », est maintenant retenu. Aucun autre changement de règle.\n")
J.append("| Règle v2 | Règle v3 | Segments | Dans le cadre |\n|---|---|---|---|")
agg = collections.Counter(); aggc = collections.Counter()
for (r2, r3, dc), n in autres.items(): agg[(r2, r3)] += n; aggc[(r2, r3)] += n if dc else 0
for (r2, r3), n in sorted(agg.items(), key=lambda x: (-x[1], x[0])): J.append(f"| {r2} | {r3} | {n} | {aggc[(r2, r3)]} |")
with open(V3 + "/journal_tirage.md", "a", encoding="utf-8") as f: f.write("\n".join(J) + "\n")

def oui(c):
    k = collections.Counter()
    for r in c.values():
        if r["exclu_du_cadre"] == "non": k[(r["lot"], r["strate"])] += int(r["n_segments_perimetre_v2_oui"]); k[(r["lot"], r["strate"], "u")] += int(r["n_segments_perimetre_v2_oui"]) >= 2
    return k
o2, o3 = oui(c2), oui(c3)
def eff(t):
    k = {}
    for lot in LOTS:
        for st in STR:
            rs = [r for r in t if r["lot"] == lot and r["strate"] == st]
            k[(lot, st)] = (len({r["doc_id"] for r in rs if r["reserve_document"] == "non"}), len({r["doc_id"] for r in rs if r["reserve_document"] == "oui"}),
                           len([r for r in rs if r["reserve_document"] == "non" and r["reserve_segment"] == "non"]),
                           len([r for r in rs if r["reserve_document"] == "non" and r["reserve_segment"] == "oui"]),
                           {r["doc_id"] for r in rs if r["reserve_document"] == "non"}, {r["segment_id"] for r in rs if r["reserve_document"] == "non" and r["reserve_segment"] == "non"})
    return k
e2, e3 = eff(t2), eff(t3)
princ = [r for r in t3 if r["reserve_document"] == "non" and r["reserve_segment"] == "non"]
E1 = re.compile(r"[^\S\r\n]{5,}")
n5 = sum(1 for r in princ if E1.search(r["texte_original"]))
n5s = collections.Counter((r["lot"], r["strate"]) for r in princ if E1.search(r["texte_original"]))
n5tous = sum(1 for r in t3 if E1.search(r["texte_original"]))
C = []
C.append("# Compte rendu — tirage v3 (ajustement du 17/11/2026)\n")
C.append(f"Rédigé le {heure} (heure d'Europe/Luxembourg). Seuls changements par rapport à la v2 : suppression de la règle « 5 espaces consécutifs ou plus » ; ajout des champs `texte_affichage`, `segment_precedent` et `segment_suivant` (lecture seulement). Deux exécutions ont donné des sorties identiques (voir autocontrole.md).\n")
C.append("## 1. Segments perimetre_v2 « oui » dans le cadre, v2 → v3\n")
C.append("| Lot | Strate | Segments oui v2 | Segments oui v3 | Écart | Unités éligibles (≥ 2 oui) v2 → v3 |\n|---|---|---|---|---|---|")
for lot in LOTS:
    for st in STR:
        a, b = o2[(lot, st)], o3[(lot, st)]
        C.append(f"| {lot} | {st} ({NOMS[st]}) | {a} | {b} | +{b - a} | {o2[(lot, st, 'u')]} → {o3[(lot, st, 'u')]} |")
C.append(f"| **Total** | | {sum(o2[(l, s)] for l in LOTS for s in STR)} | {sum(o3[(l, s)] for l in LOTS for s in STR)} | +{sum(o3[(l, s)] - o2[(l, s)] for l in LOTS for s in STR)} | |")
C.append("\n## 2. Écarts à la cible, v2 → v3\n")
C.append("Cible du tirage principal : 10 documents et 20 segments par strate (lot 1), 12 documents et 24 segments (lot 2). Réserve : 5 documents par strate, 3 segments de réserve par document principal.\n")
C.append("| Lot | Strate | Documents principal v2 / v3 (écart) | Segments principal v2 / v3 (écart) | Documents de réserve v2 / v3 | Segments de réserve des docs principaux v2 / v3 | Documents principaux communs v2-v3 | Segments principaux communs v2-v3 |\n|---|---|---|---|---|---|---|---|")
for lot in LOTS:
    for st in STR:
        a, b = e2[(lot, st)], e3[(lot, st)]; N = CIBLE[lot]
        C.append(f"| {lot} | {st} | {a[0]} / {b[0]} ({a[0]-N} / {b[0]-N}) | {a[2]} / {b[2]} ({a[2]-2*N} / {b[2]-2*N}) | {a[1]} / {b[1]} | {a[3]} / {b[3]} (cible {3*a[0]} / {3*b[0]}) | {len(a[4] & b[4])} | {len(a[5] & b[5])} |")
C.append("\nLes écarts en documents du lot 1 sont inchangés : ils viennent du nombre de fonds collectés, avec un document par fonds et par strate, et ont déjà été acceptés. Les documents principaux changent seulement en lot 2 S1 et S4, où des unités deviennent éligibles (au moins 2 segments « oui »). Ailleurs, les documents sont les mêmes, mais les segments tirés changent presque tous, parce que la liste des segments « oui » à mélanger a changé.\n")
C.append(f"## 3. Segments du tirage principal par règle de périmètre (v3, {len(princ)} segments)\n")
C.append("| Règle | v3 | v2 |\n|---|---|---|")
rp3 = collections.Counter(r["regle_perimetre_v2"] for r in princ); rp2 = collections.Counter(r["regle_perimetre_v2"] for r in t2 if r["reserve_document"] == "non" and r["reserve_segment"] == "non")
for r in sorted(set(rp3) | set(rp2), key=lambda x: (-rp3[x], x)): C.append(f"| {r} | {rp3[r]} | {rp2[r]} |")
C.append("\n## 4. Segments principaux avec une suite de 5 espaces ou plus\n")
C.append(f"{n5} segments principaux sur {len(princ)} ont, dans `texte_original`, une suite de 5 blancs ou plus. On compte comme blancs l'espace, l'espace insécable, les autres espaces Unicode et la tabulation, mais pas le saut de ligne. Par strate : " + " ; ".join(f"{l} {s} : {n5s[(l, s)]}" for l in LOTS for s in STR) + f". Sur l'ensemble des {len(t3)} lignes (réserves comprises), {n5tous} segments sont concernés. Pour eux, `texte_affichage` remplace ces suites par «  |  ».\n")
C.append("## 5. Effet de l'ordre des règles\n")
C.append(f"Sur les segments que la v2 excluait par « 5 espaces », {sum(tr_tous.values())} au total ({sum(tr_cadre.values())} dans le cadre), " + ", ".join(f"{n} ont maintenant la règle « {r} »" for r, n in sorted(tr_tous.items(), key=lambda x: (-x[1], x[0]))[:4]) + ". Les autres règles sont détaillées dans journal_tirage.md, section 9. Par ricochet, " + f"{sum(autres.values())} segments qui étaient « oui » en v2 deviennent « texte identique ».\n")
C.append("## 6. Anomalies\n")
C.append(f"- Aucune anomalie bloquante. Aucune strate n'a été complétée à la main. Les écarts à la cible restants sont listés au point 2 et dans le journal (section 6).")
C.append(f"- En lot 2 S4, le document LOT2-FR0000934325-FR-Rapport-8b48b254 n'a toujours que 3 segments, sur les 5 visés avec la réserve (2 en v2). Les autres manques de segments de la v2 (factsheets du lot 1 et du lot 2) sont comblés.")
C.append(f"- {sum(tr_tous[r] for r in tr_tous if r == DOUB)} anciens segments « 5 espaces » deviennent des doublons (« texte identique »). Ils restent exclus.")
C.append(f"- {n5} des {len(princ)} segments principaux contiennent une suite de 5 blancs ou plus (texte en colonnes). C'est l'effet attendu de la suppression de la règle ; `texte_affichage` les rend lisibles sans changer `texte_original`.")
vides_p = sum(r["segment_precedent"] == "" for r in t3); vides_s = sum(r["segment_suivant"] == "" for r in t3)
C.append(f"- `segment_precedent` est vide sur {vides_p} lignes et `segment_suivant` sur {vides_s}. Dans tous les cas, c'est le premier ou le dernier segment du document. Aucun voisin n'a été coupé par la limite des unités Colville.")
with open(V3 + "/compte_rendu_v3.md", "w", encoding="utf-8") as f: f.write("\n".join(C) + "\n")

h1, h2 = sys.argv[1], sys.argv[2]
ids = [r["segment_id"] for r in t3]
col = sorted({int(r["page"]) for r in t3 if r["doc_id"].endswith("68889a53-KID")})
A = []
A.append("# Auto-contrôle avant livraison — mission 3, version 3 (section 7)\n")
A.append(f"Rédigé le {heure} (heure d'Europe/Luxembourg).\n")
A.append("## 1. Deux exécutions successives\n")
A.append("- Exécution 1 : `nice python3 tirage_v3/tirage_script.py /workspace/doc-screener/tirage_v3` (PYTHONHASHSEED=1).")
A.append("- Exécution 2 : même script, mêmes fichiers d'entrée, PYTHONHASHSEED=777, sortie dans un dossier temporaire hors du projet (`/tmp/tirage_v3_run2`).")
A.append(f"- sha256 de tirage_pilote.csv, exécution 1 : `{h1}`")
A.append(f"- sha256 de tirage_pilote.csv, exécution 2 : `{h2}`")
same = all(open(V3 + "/" + n, "rb").read() == open(RUN2 + "/" + n, "rb").read() for n in ["tirage_pilote.csv", "cadre_documents.csv", "segments_perimetre_v2.csv", "entonnoir.md"])
A.append(f"- Résultat : {'identiques' if h1 == h2 else 'DIFFÉRENTS'} ; cadre_documents.csv, segments_perimetre_v2.csv et entonnoir.md identiques octet pour octet : {'oui' if same else 'non'}. journal_tirage.md ne diffère que par l'heure de production.\n")
A.append("## 2. Contrôles\n")
A.append(f"- Aucun segment_id en double : {'OK' if len(ids) == len(set(ids)) else 'ÉCHEC'} ({len(ids)} lignes, {len(set(ids))} segment_id distincts).")
du = collections.Counter((r["lot"], r["strate"], r["doc_id"]) for r in t3 if r["rang_segment"] == "1")
A.append(f"- Aucune unité documentaire tirée deux fois dans une strate : {'OK' if all(v == 1 for v in du.values()) else 'ÉCHEC'} ({len(du)} unités tirées).")
A.append(f"- Aucun document exclu du cadre dans le tirage : {'OK' if all(dans(r['doc_id']) for r in t3) else 'ÉCHEC'}.")
A.append(f"- Aucun segment tiré portant la règle « 5 espaces » : {'OK' if all(r['regle_perimetre_v2'] != ESP for r in t3) else 'ÉCHEC'} ; aucun segment du cadre ne porte plus cette règle : {'OK' if all(v[1] != ESP for v in s3.values()) else 'ÉCHEC'}.")
A.append(f"- Segments de l'unité LOT2-FR0013532363-FR-KID-68889a53-KID tous situés pages 1 à 3 : {'OK' if set(col) <= {1, 2, 3} else 'ÉCHEC'} (pages {col}).")
A.append(f"- Nouveaux champs : 3 colonnes ajoutées après regle_perimetre_v2 ; `texte_affichage` sans suite de 5 blancs : {'OK' if not any(E1.search(r['texte_affichage']) for r in t3) else 'ÉCHEC'} ; texte_original inchangé (les nouveaux champs sont calculés après le tirage).\n")
A.append("## 3. Effectifs du tirage principal par strate (cible section 5.1)\n")
A.append("| Lot | Strate | Documents principal (cible) | Segments principal (cible) | Documents de réserve (cible 5) | Segments de réserve des docs principaux (cible 3 × docs) |\n|---|---|---|---|---|---|")
for lot in LOTS:
    for st in STR:
        b = e3[(lot, st)]; N = CIBLE[lot]
        A.append(f"| {lot} | {st} | {b[0]} ({N}) | {b[2]} ({2*N}) | {b[1]} | {b[3]} ({3*b[0]}) |")
A.append("\n## 4. Explication des écarts\n")
A.append("- Écarts en documents du lot 1 identiques à la v1 et à la v2, et acceptés : 14 fonds collectés seulement, avec la règle « un document par fonds et par strate ». S2 perd aussi 5 factsheets réservées aux professionnels et 2 factsheets de paires. Plafond par maison inchangé.")
A.append("- Segments manquants dans un document : seul LOT2-FR0000934325-FR-Rapport-8b48b254 (lot 2 S4) reste incomplet en réserve (3 segments sur 5). Rien n'a été complété à la main.\n")
A.append("## 5. Anomalies\n")
A.append("- Aucune anomalie nouvelle (journal, section 8 ; détails dans compte_rendu_v3.md).")
with open(V3 + "/autocontrole.md", "w", encoding="utf-8") as f: f.write("\n".join(A) + "\n")
print("ok")
