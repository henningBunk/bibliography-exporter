import json
import Templates


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
        'title': json["title-original"]
    }
    message = Templates.formatTitlePage(values)
    f.write(message)
    f.close()


# Read in Stories and metadata

inputFilenames = ["story/story-template.json"]
stories = readInJsons(inputFilenames)

for story in stories:
    chapterCount = len(story["book"])

    print(story)
    # Title page
    writeTitlePage(1, story)
    # Preface
    f = open('Section0002.xhtml', 'w')
    f.write(message)
    f.close()
    # Main story
    f = open('Section0003.xhtml', 'w')
    f.write(message)
    f.close()

# Export ebook files
