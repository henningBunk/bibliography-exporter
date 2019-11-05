def manifest(filenames):
    return """<?xml version="1.0" encoding="utf-8"?>
<package version="2.0" unique-identifier="BookId" xmlns="http://www.idpf.org/2007/opf">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier opf:scheme="UUID" id="BookId">urn:uuid:204e84e9-f3e7-465a-b14e-768b8e8fe875</dc:identifier>
    <dc:language>de</dc:language>
    <dc:title>Gesammelte Werke</dc:title>
    <meta content="0.9.18" name="Sigil version" />
    <dc:date xmlns:opf="http://www.idpf.org/2007/opf" opf:event="modification">2019-10-24</dc:date>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="style.css" href="Styles/style.css" media-type="text/css"/>
%(entries)s
  </manifest>
  <spine toc="ncx">
%(toc)s
  </spine>
</package>
""" % {
        'entries': getManifestEntries(filenames),
        'toc': getToc(filenames)
    }


def getManifestEntries(filenames):
    entries = ""
    for filename in filenames:
        entries += getManifestEntry(filename)
    return entries


def getManifestEntry(filename):
    return """    <item id="%(filename)s" href="Text/%(filename)s" media-type="application/xhtml+xml"/>
""" % {'filename': filename}


def getToc(filenames):
    entries = ""
    for filename in filenames:
        entries += getTocEntry(filename)
    return entries


def getTocEntry(filename):
    return """    <itemref idref="%(filename)s"/>
""" % {'filename': filename}
