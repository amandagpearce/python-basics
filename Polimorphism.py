class English:
    def greet(self, name):
        print('Goord morning', name)


class French:
    def greet(self, name):
        print('Bonjour', name)


def greetings(language, name):
    language.greet(name)


eng = English()
fr = French()

greetings(eng, "Amanda")
greetings(fr, "Amanda")
