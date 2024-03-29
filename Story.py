import re


class Story:
    def __init__(self, json):
        self.filenameTitlePage = ""
        self.filenameMainStory = ""
        self.author = json["author"]
        self.titleGerman = json["title-german"]
        self.titleGermanSlug = Story.toSlug(json["title-german"])
        self.titleOriginal = json["title-original"]
        self.year = json['year']
        self.published = json['published']
        self.source = json['source']
        self.translation = json['translation'] if 'translation' in json else None
        self.category = json['category'] if 'category' in json else None
        self.preface = self.Preface(json) if 'preface' in json else None
        self.mainStorySlug = 'hauptgeschichte-' + Story.toSlug(json["title-german"])
        self.chapters = list(map(lambda chapter: self.Chapter(chapter, self.titleGermanSlug), json["chapters"]))

    def hasPreface(self):
        return self.preface is not None

    def hasChapters(self):
        return self.getChapterCount() > 1

    def getChapterCount(self):
        return len(self.chapters)

    class Preface:
        def __init__(self, json):
            self.filenamePreface = ""
            self.author = json["preface"]["author"]
            self.content = json["preface"]["content"]
            self.slug = 'vorwort-' + Story.toSlug(json["title-german"])

        def hasAuthor(self):
            return self.author is not None

    class Chapter:
        def __init__(self, json, titleGermanSlug):
            self.content = json["content"]
            self.title = json["title"] if 'title' in json else None
            self.slug = (titleGermanSlug + '-' + Story.toSlug(json["title"])) if 'title' in json else None

    @staticmethod
    def toSlug(string):
        return re.sub('[ #`\'"?!&()]', '-', re.sub('[ä]', 'ae', re.sub('[ö]', 'oe', re.sub('[ü]', 'ue', string)))) \
            .lower()
