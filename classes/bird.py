class Bird:
    def __init__(self, kind, call):
        self._kind = kind
        self._call = call

    def do_call(self):
        print 'a %s goes %s' % (self._kind, self._call)

owl = Bird('Owl', 'Twit Twoo!')
print owl._kind


class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.learned_phrases = set()

    def learn_phrase(self, phrase):
        self.learned_phrases.add(phrase)

    def do_call(self):
        Bird.do_call(self)
        print '\n'.join(self.learned_phrases)

parrot = Parrot()
parrot.learn_phrase("I'm a pretty polly")
parrot.learn_phrase("Who's a pretty boy, then?")
parrot.do_call()
