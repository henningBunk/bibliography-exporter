import json

import MainStoryTemplate
import PrefaceTemplate
import TitlePageTemplate
import re
import os
from os.path import join
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
        writePreface(1, story.preface)
        # # Main story
        writeMainContent(1, story)

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
    filename = 'Section0001.xhtml'
    message = TitlePageTemplate.formatTitlePage(story)
    writeContent(filename, message)


def writePreface(index, preface):
    filename = 'Section0002.xhtml'
    message = PrefaceTemplate.formatPreface(preface)
    writeContent(filename, message)

def writeMainContent(index, story):
    filename = 'Section0003.xhtml'
    message = MainStoryTemplate.formatMainStory(story)
    writeContent(filename, message)


def writeContent(filename, content):
    f = open(join('book', 'OEBPS', 'Text', filename), 'w', encoding='UTF-8')
    f.write(content)
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