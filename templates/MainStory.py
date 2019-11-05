def formatMainStory(story):
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title></title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
<p>&#160;</p>

<h2><a id="%(main-story-slug)s">%(title-german)s</a></h2>

%(main-story-content)s</body>
</html>""" % {
        'title-german': story.titleGerman,
        'main-story-slug': story.mainStorySlug,
        'main-story-content': formatMainContent(story)
    }


def formatMainContent(story):
    if story.hasChapters():
        return formatMultipleChapters(story.chapters)
    else:
        return formatSingleChapter(story.chapters[0].content)


def formatMultipleChapters(chapters):
    content = ''
    for chapter in chapters:
        content += """<h3 id="sigil_toc_id_1"><a id="%(chapter-slug)s">%(chapter-title)s</a></h3>

        <p>%(chapter-content)s</p>
        
""" % {
            'chapter-title': chapter.title,
            'chapter-content': chapter.content,
            'chapter-slug': chapter.slug
        }
    return content

def formatSingleChapter(content):
    return """<p>%(content)s</p>
    
""" % {'content': content}
