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

  %(content)s
</body>
</html>""" % values

def content(values):
    return """<h3 class="story-content sigil_not_in_toc">Inhalt</h3>
    
  <p class="story-content-item-level-1"><a href="../Text/Section0002.xhtml#vorwort-der-fluesterer-im-dunkeln">Vorwort</a></p>

  <p class="story-content-item-level-1"><a href="../Text/Section0003.xhtml#hauptgeschichte-der-fluesterer-im-dunkeln">Der Flüsterer im Dunkeln</a></p>

  <p class="story-content-item-level-2"><a href="../Text/Section0003.xhtml#der-fluesterer-im-dunkeln-kapitel-I">Kapitel I</a></p>

  <p class="story-content-item-level-2"><a href="../Text/Section0003.xhtml#der-fluesterer-im-dunkeln-kapitel-II">Kapitel II</a></p>"""