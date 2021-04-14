import re
import sys
from pryzm import Pryzm
red = Pryzm(echo=False).red

class VerbFactory:
    def __init__(self):
        pass

    def get_verb_obj(self, verb):
        if verb.endswith('cer'):
            return VerbCer(verb)
        elif verb.endswith('ger'):
            return VerbGer(verb)
        elif verb.endswith('er'):
            return VerbEr(verb)
        else:
            None

class VerbEr:
    def __init__(self, verb):
        self.verb_id = 'er'
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
        self.verb_id = 'cer'

    def nous(self):
        # Er verbs ending in cer use cedilla to avoid hard C sound before an O
        return self.root[:-1] + 'çons'

class VerbGer(VerbEr):
    def __init__(self, verb):
        super().__init__(verb) 
        self.verb_id = 'ger'

    def nous(self):
        # Er verbs ending in ger insert an e to avoid 'gons', to get 'geons' 
        return self.root + 'eons'

# =========================== TESTS =======================================

def test_verbs_ending_in_er():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('parler')

    assert verb.verb_id == 'er'
    assert verb.get_root() == 'parl'
    assert verb.je() == 'parle'
    assert verb.tu() == 'parles'
    assert verb.il() == 'parle'
    assert verb.elle() == 'parle'
    assert verb.nous() == 'parlons'
    assert verb.vous() == 'parlez'
    assert verb.ils() == 'parlent'
    assert verb.elles() == 'parlent'

def test_verbs_ending_in_cer():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('défoncer')

    assert verb.verb_id == 'cer'
    assert verb.get_root() == 'défonc'
    assert verb.je() == 'défonce'
    assert verb.tu() == 'défonces'
    assert verb.il() == 'défonce'
    assert verb.elle() == 'défonce'
    assert verb.nous() == 'défonçons'
    assert verb.vous() == 'défoncez'
    assert verb.ils() == 'défoncent'
    assert verb.elles() == 'défoncent'

def test_verbs_ending_in_ger():
    vFact = VerbFactory()
    verb = vFact.get_verb_obj('voyager')

    assert verb.verb_id == 'ger'
    assert verb.get_root() == 'voyag'
    assert verb.je() == 'voyage'
    assert verb.tu() == 'voyages'
    assert verb.il() == 'voyage'
    assert verb.elle() == 'voyage'
    assert verb.nous() == 'voyageons'
    assert verb.vous() == 'voyagez'
    assert verb.ils() == 'voyagent'
    assert verb.elles() == 'voyagent'

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
