def formatPreface(preface):
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

<h2><a id="%(preface-slug)s">Vorwort</a></h2>

<p>%(preface-author)s</p>

<p>%(preface)s</p>
</body>
</html>""" % {
        'preface-slug': preface.slug,
        'preface-author': ('Von ' + preface.author) if preface.hasAuthor() else "",
        'preface': preface.content,
    }
