from Grille import Grille
from Motif import Motif
from Case import Case


class SolveurSuguruBitmask:
    """
    Solveur Suguru basé sur bitmask avec backtracking.
    """

    def __init__(self, grille: Grille):

        self.grille = grille
        self.cases = grille.getCases()

        # index basé sur (x, y) -> FIX du bug "unhashable Case"
        self.index = {(c.x, c.y): i for i, c in enumerate(self.cases)}
        self.n = len(self.cases)

        # voisins indexés par case
        self.voisins = {
            (c.x, c.y): grille.getVoisins(c)
            for c in self.cases
        }

        self.dom = [0] * self.n
        self.val = [0] * self.n

        self.solutions: list[Grille] = []


    def bit(self, v: int) -> int:
        return 1 << (v - 1)

    def full_mask(self, size: int) -> int:
        return (1 << size) - 1

    def count_bits(self, m: int) -> int:
        return bin(m).count("1")


    def init(self) -> None:

        for c in self.cases:
            i = self.index[(c.x, c.y)]

            if c.contenu is not None:
                self.val[i] = c.contenu
                self.dom[i] = self.bit(c.contenu)
            else:
                self.val[i] = 0
                self.dom[i] = self.full_mask(c.motif.tailleMotif())


    def ok(self, i: int, v: int) -> bool:

        c = self.cases[i]

        # motif
        for x in c.motif.getCases():
            j = self.index[(x.x, x.y)]
            if self.val[j] == v:
                return False

        # voisins
        for x in self.voisins[(c.x, c.y)]:
            j = self.index[(x.x, x.y)]
            if self.val[j] == v:
                return False

        return True


    def remove(self, i: int, v: int, stack: list) -> bool:

        b = self.bit(v)

        if self.dom[i] & b:
            self.dom[i] &= ~b
            stack.append((i, b))

            if self.dom[i] == 0:
                return False

        return True


    def select_case(self) -> int:

        best = -1
        best_score = 10**9

        for i in range(self.n):
            if self.val[i] != 0:
                continue

            score = self.count_bits(self.dom[i])

            if score < best_score:
                best_score = score
                best = i

        return best


    def build_grille_from_solution(self) -> Grille:

        new_grid = Grille()
        motif_map = {}

        for c in self.cases:

            orig_motif = c.motif

            if orig_motif not in motif_map:
                motif_map[orig_motif] = Motif()

            new_motif = motif_map[orig_motif]

            i = self.index[(c.x, c.y)]
            val = self.val[i]

            new_case = Case(
                x=c.x,
                y=c.y,
                contenu=val,
                motif=new_motif
            )

            new_motif.ajouterCase(new_case)
            new_grid._cases[(new_case.x, new_case.y)] = new_case

        new_grid._motifs = list(motif_map.values())

        return new_grid


    def solve(self) -> None:

        i = self.select_case()

        if i == -1:
            self.solutions.append(self.build_grille_from_solution())
            return

        mask = self.dom[i]
        m = mask

        while m:

            b = m & -m
            v = b.bit_length()

            if self.ok(i, v):

                self.val[i] = v
                self.dom[i] = b

                stack = []
                c = self.cases[i]

                key = (c.x, c.y)

                # motif
                for x in c.motif.getCases():
                    j = self.index[(x.x, x.y)]
                    if j != i:
                        if not self.remove(j, v, stack):
                            self.restore(stack)
                            break
                else:
                    # voisins
                    for x in self.voisins[key]:
                        j = self.index[(x.x, x.y)]
                        if j != i:
                            if not self.remove(j, v, stack):
                                self.restore(stack)
                                break
                    else:
                        self.solve()

                self.restore(stack)
                self.val[i] = 0
                self.dom[i] = mask

            m &= m - 1


    def restore(self, stack: list) -> None:

        for i, b in reversed(stack):
            self.dom[i] |= b


    def resoudre(self) -> list[Grille]:

        self.init()
        self.solve()
        return self.solutions


if __name__ == "__main__":
    g = Grille()
    g.chargerGrilleFromJson("grilles/grille2.json")

    solveur = SolveurSuguruBitmask(g)
    solutions = solveur.resoudre()

    print(len(solutions), "solutions")
    for solution in solutions:
        print("Grille")
        solution.afficherGrille()