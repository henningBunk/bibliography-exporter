# print '<a href="%(url)s">%(url)s</a>' % {'url': my_url}
def formatTitlePage(values):
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title></title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>

<body>
  <p> </p>

  <h1 class="titlepage-headline"><a id="%(title-german-slug)s">%(title-german)s</a></h1>

  <p class="data-field">Originaltitel: <span class="data-content">%(title-original)s</span></p>

  <p class="data-field">Geschrieben: <span class="data-content">%(year)s</span></p>

  <p class="data-field">Erstveröffentlichung: <span class="data-content">%(published)s</span></p>

  <p class="data-field">ÜbersetzerIn: <span class="data-content">%(translation)s</span></p>

  <p class="data-field">Quelle: <span class="data-content">%(source)s</span></p>

  <p class="data-field">Kategorie: <span class="data-content">%(category)s</span></p>

  %(toc)s
</body>
</html>""" % values


def toc(tocPreface, tocMain):
    return """<h3 class="story-content sigil_not_in_toc">Inhalt</h3>
    
  %(toc-preface)s

  %(toc-main)s""" % {'toc-preface': tocPreface, 'toc-main': tocMain}


def tocPreface(slug):
    return """<p class="story-content-item-level-1"><a href="../Text/Section0002.xhtml#%(slug)s">Vorwort</a></p>""" % {'slug': slug }


def tocMainTitle(title, titleSlug):
    return """<p class="story-content-item-level-1"><a href="../Text/Section0003.xhtml#hauptgeschichte-%(title-slug)s">%(title)s</a></p>
""" % {'title': title, 'title-slug': titleSlug}


def tocChapter(chapterTitle, chapterSlug):
    return """<p class="story-content-item-level-2"><a href="../Text/Section0003.xhtml#%(chapter-slug)s">%(chapter-title)s</a></p>
""" % {'chapter-title': chapterTitle, 'chapter-slug': chapterSlug}
