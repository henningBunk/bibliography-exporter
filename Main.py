import json
import Templates
import re
import os
import zipfile

def main():
    # Read in Stories and metadata

    inputFilenames = ["story/story-template.json"] # TODO use a list with all input files here
    stories = readInJsons(inputFilenames)

    for story in stories:
        chapterCount = len(story["book"])

        print(story)
        # Title page
        writeTitlePage(1, story)
        # Preface
        # f = open('Section0002.xhtml', 'w')
        # f.write(message)
        # f.close()
        # # Main story
        # f = open('Section0003.xhtml', 'w')
        # f.write(message)
        # f.close()

    # Export ebook files
    makeEbook()


def readInJsons(inputFilenames):
    stories = []
    for fileName in inputFilenames:
        with open(fileName, 'r', encoding="UTF-8") as jsonFile:
            data = json.load(jsonFile)
            stories.append(data)
    return stories


def writeTitlePage(index, json):
    f = open('book\OEBPS\\Text\Section0001.xhtml', 'w', encoding='UTF-8')
    # print '<a href="%(url)s">%(url)s</a>' % {'url': my_url}
    values = {
        'title-german': json["title-german"],
        'title-german-slug': toSlug(json['title-german']),
        'title-original': json["title-original"],
        'year': json['year'],
        'published': json['published'],
        'translation': json['translation'],
        'source': json['source'],
        'category': json['category'],
        'toc': getTitlePageToc(json)
    }
    message = Templates.formatTitlePage(values)
    f.write(message)
    f.close()


def toSlug(string):
    return re.sub('[ #`\'"?!&()]', '-', re.sub('[ä]', 'ae', re.sub('[ö]', 'oe', re.sub('[ü]', 'ue', string)))) \
        .lower()


def getTitlePageToc(json):
    if not hasPreface(json) and not hasChapters(json):
        return ""
    preface = (Templates.tocPreface('vorwort-' + toSlug(json['title-german']))) if hasPreface(json) else ""
    main = getTitlePageMainToc(json)
    return Templates.toc(preface, main)


def getTitlePageMainToc(json):
    toc = Templates.tocMainTitle(json['title-german'], toSlug(json['title-german']))
    if hasChapters(json):
        for chapter in json['book']:
            toc += Templates.tocChapter(chapter['title'], toSlug(chapter['title']))
    return toc


def hasChapters(json):
    return len(json["book"]) > 1


def hasPreface(json):
    return 'preface' in json


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def makeEbook():
    zipf = zipfile.ZipFile('ebook.epub', 'w', zipfile.ZIP_DEFLATED)
    zipdir('book/', zipf)
    zipf.close()


main()