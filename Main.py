import json
import Templates
import re

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


def readInJsons(inputFilenames):
    stories = []
    for fileName in inputFilenames:
        with open(fileName, 'r', encoding="UTF-8") as jsonFile:
            data = json.load(jsonFile)
            stories.append(data)
    return stories


def writeTitlePage(index, json):
    f = open('Section0001.xhtml', 'w')
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
        'content': getTitlePageContent(json)
    }
    message = Templates.formatTitlePage(values)
    f.write(message)
    f.close()


def toSlug(string):
    return re.sub('[ #`\'"?!&()]', '-', string).lower()


def getTitlePageContent(json):
    # TODO check if there should be a TOC, than create one
    if hasChapters(json):

    if hasPreface(json):
    values = {

    }
    return Templates.content(values)

main()