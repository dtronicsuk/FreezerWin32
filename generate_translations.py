import zipfile
import json

def generate():
    with zipfile.ZipFile('translations.zip') as zip:
        for file in zip.namelist():
            if 'freezerpc.json' in file:
                data = zip.open(file).read()
                lang = file.split('/')[0].split('-')[0].lower()
                if lang != 'en':
                    with open('app/client/src/locales/' + lang + '.json', 'wb') as f:
                        f.write(data)



if __name__ == '__main__':
    generate()