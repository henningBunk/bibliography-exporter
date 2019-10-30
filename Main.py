import json
import Templates
import re
import os
import zipfile
from Story import Story

def main():
    # Read in Stories and metadata

    inputFilenames = ["story/story-template.json"] # TODO use a list with all input files here
    stories = readInJsons(inputFilenames)

    for story in stories:
        chapterCount = story.getChapterCount()

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
            stories.append(Story(data))
    return stories


def writeTitlePage(index, story):
    f = open('book\OEBPS\\Text\Section0001.xhtml', 'w', encoding='UTF-8')
    message = Templates.formatTitlePage(story)
    f.write(message)
    f.close()


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