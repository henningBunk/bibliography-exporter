def formatMainTableOfContent(stories):
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Inhalt</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
<p>&nbsp;</p>
<h1 class="titlepage-headline"><a id="content">Inhalt</a></h1>

%(entries)s

</body>
</html>""" % {'entries': getEntries(stories)}


def getEntries(stories):
    toc = ""
    for story in stories:
        toc += getTitlePageLink(story)
    return toc


def getTitlePageLink(story):
    return """  <p class="main-content-item-level-1"><a href="../%(filename)s#%(slug)s">%(title)s</a></p>
""" % {
        'title': story.titleGerman,
        'slug': story.titleGermanSlug,
        'filename': story.filenameTitlePage
    }
