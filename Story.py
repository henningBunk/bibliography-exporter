import re

class Story:
    def __init__(self, json):
        self.author = json["author"]
        self.titleGerman = json["title-german"]
        self.titleGermanSlug = Story.toSlug(json["title-german"])
        self.titleOriginal = json["title-original"]
        self.year = json['year']
        self.published = json['published']
        self.source = json['source']
        self.translation = json['translation']
        self.category = json['category']
        self.preface = self.Preface(json)
        self.chapters = list(map(lambda chapter: self.Chapter(chapter), json["chapters"]))

    def hasPreface(self):
        return self.preface is not None

    def hasChapters(self):
        return self.getChapterCount() > 1

    def getChapterCount(self):
        return len(self.chapters)

    class Preface:
        def __init__(self, json):
            self.author = json["preface"]["author"]
            self.content = json["preface"]["content"]
            self.slug = 'vorwort-' + Story.toSlug(json["title-german"])

        def hasAuthor(self):
            return self.author is not None

    class Chapter:
        def __init__(self, json):
            self.title = json["title"]
            self.content = json["content"]
            self.slug = Story.toSlug(json["title"])

    @staticmethod
    def toSlug(string):
        return re.sub('[ #`\'"?!&()]', '-', re.sub('[ä]', 'ae', re.sub('[ö]', 'oe', re.sub('[ü]', 'ue', string)))) \
            .lower()
