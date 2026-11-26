"""Alpha de Krippendorff (données nominales, deux codeurs, sans valeur manquante).

Usage : python3 alpha_krippendorff.py codage_A.csv codage_B.csv [colonne]
La colonne par défaut est code_principal. Les fichiers sont joints sur id_codage.
"""
import csv
import sys
from collections import Counter


def alpha_nominal(x, y):
    paires = list(zip(x, y))
    n = 2 * len(paires)
    o = Counter()
    for a, b in paires:
        o[(a, b)] += 1
        o[(b, a)] += 1
    nc = Counter(list(x) + list(y))
    d_obs = sum(v for (a, b), v in o.items() if a != b) / n
    d_att = sum(nc[a] * nc[b] for a in nc for b in nc if a != b) / (n * (n - 1))
    return 1 - d_obs / d_att if d_att else float("nan")


def lire(chemin, colonne):
    with open(chemin, encoding="utf-8") as f:
        return {r["id_codage"]: r[colonne] for r in csv.DictReader(f)}


if __name__ == "__main__":
    col = sys.argv[3] if len(sys.argv) > 3 else "code_principal"
    a, b = lire(sys.argv[1], col), lire(sys.argv[2], col)
    ids = sorted(set(a) & set(b))
    x, y = [a[i] for i in ids], [b[i] for i in ids]
    accord = sum(p == q for p, q in zip(x, y))
    print(f"{col} : alpha = {alpha_nominal(x, y):.3f} ; accord brut = {accord}/{len(ids)}")
