def formatTitlePage(story):
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
</html>""" % {
        'title-german': story.titleGerman,
        'title-german-slug': story.titleGermanSlug,
        'title-original': story.titleOriginal,
        'year': story.year,
        'published': story.published,
        'translation': story.translation,
        'source': story.source,
        'category': story.category,
        'toc': formatToc(story)
    }


def formatToc(story):
    if not story.hasPreface() and not story.hasChapters():
        return ""
    return toc(story)


def toc(story):
    return """<h3 class="story-content sigil_not_in_toc">Inhalt</h3>
    
%(toc-preface)s
%(toc-main)s
""" % {
        'toc-preface': (tocPreface(story)) if story.hasPreface() else "",
        'toc-main': tocMain(story)
    }


def tocPreface(story):
    return """  <p class="story-content-item-level-1"><a href="../Text/Section0002.xhtml#%(slug)s">Vorwort</a></p>
""" % {
        'slug': story.preface.slug
    }


def tocMain(story):
    toc = tocMainTitle(story)
    if story.hasChapters():
        for chapter in story.chapters:
            toc += tocMainChapter(chapter.title, chapter.slug)
    return toc


def tocMainTitle(story):
    return """  <p class="story-content-item-level-1"><a href="../Text/Section0003.xhtml#%(main-story-slug)s">%(title)s</a></p>

""" % {
        'title': story.titleGerman,
        'main-story-slug': story.mainStorySlug
    }


def tocMainChapter(chapterTitle, chapterSlug):
    return """  <p class="story-content-item-level-2"><a href="../Text/Section0003.xhtml#%(chapter-slug)s">%(chapter-title)s</a></p>
    
""" % {
        'chapter-title': chapterTitle,
        'chapter-slug': chapterSlug
    }
