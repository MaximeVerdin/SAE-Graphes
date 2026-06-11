from Case import Case
from Motif import Motif, buildMotifFromListe


def test_ajout_case():
    m = Motif()
    c = Case(0, 0)

    m.ajouterCase(c)

    assert c in m.getCases()
    assert c.motif is m


def test_suppression_case():
    m = Motif()
    c = Case(0, 0)

    m.ajouterCase(c)
    m.supprimerCase(c)

    assert c not in m.getCases()
    assert c.motif is None


def test_get_case():
    m = Motif()
    c = Case(2, 3)

    m.ajouterCase(c)

    assert m.getCase(2, 3) is c


def test_est_valide_ok():
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(0, 1, 2))

    assert m.estValide()


def test_est_valide_erreur_doublon():
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(0, 1, 1))

    assert not m.estValide()


def test_est_plein_true():
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(0, 1, 2))

    assert m.estPlein()


def test_est_plein_false():
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(0, 1, None))

    assert not m.estPlein()


def test_contenu_valide_ok():
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    c2 = Case(0, 1, 2)

    m.ajouterCase(c2)

    assert m.contenuValide(c2)


def test_contenu_valide_erreur_doublon():
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    c2 = Case(0, 1, 1)

    m.ajouterCase(c2)

    assert not m.contenuValide(c2)


def test_build_motif():
    data = [
        [0, 0, 1],
        [0, 1, 2],
    ]

    m = buildMotifFromListe(data)

    assert m.tailleMotif() == 2
    assert m.getCase(0, 0).contenu == 1