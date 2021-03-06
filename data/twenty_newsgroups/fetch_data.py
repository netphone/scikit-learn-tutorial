"""Script to download the 20 newsgroups text classification set"""

import os
import urllib
import tarfile

URL = ("http://people.csail.mit.edu/jrennie/"
       "20Newsgroups/20news-bydate.tar.gz")

ARCHIVE_NAME = URL.rsplit('/', 1)[1]
TRAIN_FOLDER = "20news-bydate-train"
TEST_FOLDER = "20news-bydate-test"


if not os.path.exists(TRAIN_FOLDER) or not os.path.exists(TEST_FOLDER):

    if not os.path.exists(ARCHIVE_NAME):
        print "Downloading dataset from %s (14 MB)" % URL
        opener = urllib.urlopen(URL)
        open(ARCHIVE_NAME, 'wb').write(opener.read())

    print "Decompressing %s" % ARCHIVE_NAME
    tarfile.open(ARCHIVE_NAME, "r:gz").extractall(path='.')
    os.remove(ARCHIVE_NAME)

