import wikipedia
from wikipedia.exceptions import DisambiguationError as HasAnotherMeaning
from wikipedia.exceptions import PageError as NoCoincidences


class WikiHelper:
    class __WikiHelper:
        def __init__(self):
            pass

    instance = None

    def __init__(self):
        if not WikiHelper.instance:
            WikiHelper.instance = WikiHelper.__WikiHelper()

    looking_for = ""

    def start(self):
        self.set_looking_for()
        results = self.search()
        for result in results:
            print(" - " + result + ": ")
            self.resume(result)

    def set_looking_for(self):
        print("Search: ")
        self.looking_for = input()

    def search(self):
        return wikipedia.search(self.looking_for, results=3)

    @staticmethod
    def resume(result):
        try:
            print("\t" + wikipedia.summary(result, sentences=1))
        except HasAnotherMeaning as another_meaning:
            print("Other pages for this result: ")
            options = another_meaning.options[:3]
            for other_option in options:
                print(other_option)
        except NoCoincidences:
            print("Without results")
            wikipedia.suggest(result)


wiki = WikiHelper()
wiki.start()
