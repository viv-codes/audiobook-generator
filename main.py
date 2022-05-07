import ebooklib, os

from ebooklib import epub
from gtts import gTTS


def run():
    epubPath = input("Enter path for epub: ")
    txt2mp3(epub2txt(epubPath), epubPath)


def epub2txt(epubPath):
    book = epub.read_epub(epubPath)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


def txt2mp3(chapterSet, epubPath):
    chapterCount = 0
    os.mkdir(epubPath)
    os.chdir(epubPath)
    for chapter in chapterSet:
        chapterCount = chapterCount + 1
        tts = gTTS(chapter)
        tts.save("Chapter " + chapterCount)


if __name__ == '__main__':
    run()
