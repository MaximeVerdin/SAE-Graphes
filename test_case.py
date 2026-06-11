from Case import Case


def test_position():
    c = Case(2, 3)

    assert c.getPosition() == (2, 3)


def test_voisin_true():
    c1 = Case(0, 0)
    c2 = Case(1, 1)

    assert c1.estVoisin(c2)


def test_voisin_false_loin():
    c1 = Case(0, 0)
    c2 = Case(2, 2)

    assert not c1.estVoisin(c2)


def test_voisin_pas_soi_meme():
    c = Case(0, 0)

    assert not c.estVoisin(c)


def test_to_list():
    c = Case(1, 2, 5)

    assert c.toList() == [1, 2, 5]


def test_to_list_vide():
    c = Case(1, 2)

    assert c.toList() == [1, 2, 0]