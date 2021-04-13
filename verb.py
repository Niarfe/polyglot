import re
import sys


class VerbFactory:
    def __init__(self):
        pass

    def get_verb_obj(self, verb):
        if verb.endswith('cer'):
            return VerbCer(verb)
        if verb.endswith('er'):
            return VerbEr(verb)
        else:
            None

class VerbEr:
    def __init__(self, verb):
        self.verb = verb
        self.root = self.get_root()

    def get_root(self):
        return self.verb[:-2]

    def je(self):
        return self.root + 'e'

    def tu(self):
        return self.root + 'es'

    def il(self):
        return self.root + 'e'

    def elle(self):
        return self.root + 'e'

    def nous(self):
        return self.root + 'ons'

    def vous(self):
        return self.root + 'ez'

    def ils(self):
        return self.root + 'ent'

    def elles(self):
        return self.root + 'ent'

class VerbCer(VerbEr):
    def __init__(self, verb):
        super().__init__(verb) 

    def nous(self):
        # Er verbs ending in cer use cedilla to avoid hard C sound before an O
        return self.root[:-1] + 'çons'



def test_conjugate_parler():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('parler')

    assert verb.get_root() == 'parl'
    assert verb.je() == 'parle'
    assert verb.tu() == 'parles'
    assert verb.il() == 'parle'
    assert verb.elle() == 'parle'
    assert verb.nous() == 'parlons'
    assert verb.vous() == 'parlez'
    assert verb.ils() == 'parlent'
    assert verb.elles() == 'parlent'


def test_conjugate_chanter():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('chanter')

    assert verb.get_root() == 'chant'
    assert verb.je() == 'chante'
    assert verb.tu() == 'chantes'
    assert verb.il() == 'chante'
    assert verb.elle() == 'chante'
    assert verb.nous() == 'chantons'
    assert verb.vous() == 'chantez'
    assert verb.ils() == 'chantent'
    assert verb.elles() == 'chantent'

def test_conjugate_annoncer():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('annoncer')

    assert verb.get_root() == 'annonc'
    assert verb.je() == 'annonce'
    assert verb.tu() == 'annonces'
    assert verb.il() == 'annonce'
    assert verb.elle() == 'annonce'
    assert verb.nous() == 'annonçons'
    assert verb.vous() == 'annoncez'
    assert verb.ils() == 'annoncent'
    assert verb.elles() == 'annoncent'

def test_conjugate_défoncer():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('défoncer')

    assert verb.get_root() == 'défonc'
    assert verb.je() == 'défonce'
    assert verb.tu() == 'défonces'
    assert verb.il() == 'défonce'
    assert verb.elle() == 'défonce'
    assert verb.nous() == 'défonçons'
    assert verb.vous() == 'défoncez'
    assert verb.ils() == 'défoncent'
    assert verb.elles() == 'défoncent'

if __name__ == '__main__':
    import sys
    verb = sys.argv[1]
    vFact = VerbFactory()
    verb = vFact.get_verb_obj(verb.strip())

    print(verb.je())
    print(verb.tu())
    print(verb.il())
    print(verb.elle())
    print(verb.nous())
    print(verb.vous())
    print(verb.ils())
    print(verb.elles())
