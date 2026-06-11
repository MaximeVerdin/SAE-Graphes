from Case import Case
from Motif import Motif
from Grille import Grille


def test_add_motif():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(0, 0))

    g.addMotif(m)

    assert g.getNombreMotif() == 1
    assert g.getCase(0, 0) is not None


def test_remove_motif():
    g = Grille()
    m = Motif()

    c = Case(0, 0)
    m.ajouterCase(c)

    g.addMotif(m)
    g.removeMotif(m)

    assert g.getNombreMotif() == 0
    assert g.getCase(0, 0) is None


def test_set_get_valeur():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(1, 1))

    g.addMotif(m)

    g.setValeur(1, 1, 5)

    assert g.getValeur(1, 1) == 5


def test_get_voisins():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(0, 0))
    m.ajouterCase(Case(1, 0))
    m.ajouterCase(Case(0, 1))
    m.ajouterCase(Case(1, 1))

    g.addMotif(m)

    voisins = g.getVoisins(g.getCase(0, 0))

    assert len(voisins) == 3


def test_est_valide_ok():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(1, 0, 2))

    g.addMotif(m)

    assert g.estValide()


def test_est_valide_erreur_voisin():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(1, 0, 1))

    g.addMotif(m)

    assert not g.estValide()


def test_est_pleine():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))
    m.ajouterCase(Case(1, 0, 2))

    g.addMotif(m)

    assert g.estPleine()


def test_to_dico():
    g = Grille()
    m = Motif()

    m.ajouterCase(Case(0, 0, 1))

    g.addMotif(m)

    d = g.toDico()

    assert isinstance(d, dict)
    assert "motif1" in d