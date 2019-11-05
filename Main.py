import json
import os
from os.path import join
import zipfile
from Story import Story
from templates import Manifest, MainStory, Preface, TitlePage, TableOfContent


def main():
    # Read in Stories and metadata
    inputFilenames = [
        "story/story-template.json",
        "story/no-chapters.json"
    ]
    stories = readInStories(inputFilenames)

    for i, story in enumerate(stories):
        i += 1
        if story.hasPreface():
            writePreface(i, story.preface)
        writeMainContent(i, story)
        writeTitlePage(i, story)

    writeTableOfContent(stories)
    writeManifest()

    # Export ebook files
    makeEbook()


def readInStories(inputFilenames):
    stories = []
    for fileName in inputFilenames:
        with open(fileName, 'r', encoding="UTF-8") as jsonFile:
            data = json.load(jsonFile)
            stories.append(Story(data))
    return stories


def writeTableOfContent(stories):
    filename = join('Text', 'Section0001.xhtml')
    message = TableOfContent.formatMainTableOfContent(stories)
    writeContent(filename, message)


def writeTitlePage(index, story):
    filename = join('Text', 'Section%02d01.xhtml' % index)
    story.filenameTitlePage = filename
    message = TitlePage.formatTitlePage(story)
    writeContent(filename, message)


def writePreface(index, preface):
    filename = join('Text', 'Section%02d02.xhtml' % index)
    preface.filenamePreface = filename
    message = Preface.formatPreface(preface)
    writeContent(filename, message)


def writeMainContent(index, story):
    filename = join('Text', 'Section%02d03.xhtml' % index)
    story.filenameMainStory = filename
    message = MainStory.formatMainStory(story)
    writeContent(filename, message)


def writeManifest():
    filenames = os.listdir(join('book', 'OEBPS', 'Text'))
    filenames.sort()
    message = Manifest.manifest(filenames)
    writeContent('content.opf', message)


def writeContent(filename, content):
    f = open(join('book', 'OEBPS', filename), 'w', encoding='UTF-8')
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