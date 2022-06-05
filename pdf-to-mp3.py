from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        return 'File exists!'
    else:
        return 'File not exists, check the file path!'


def main():
    print(pdf_to_mp3(file_path='D:\progr\pdf-to-mp3\Путь жизни.pdf'))


if __name__ == '__main__':
    main()