

class Photo:
    def __init__(self, id, isHorizontal, numTags, tags):
        self.id = id
        self.isHorizontal = isHorizontal
        self.numTags = numTags
        self.tags=tags

    def __repr__(self):
        return "Photo: "+self.tags.__str__();


def calcScore(p1: Photo, p2: Photo) :
    p1Tags = p1.tags
    p2Tags = p2.tags
    return min(len(p1Tags.difference(p2Tags)), len(p2Tags.difference(p1Tags)), len(p1Tags.intersection(p2Tags)))

def extractPhotos(numPhotos: int, content: list) :
    photos = []
    tagsToPhotoMap = {}
    i = 1
    for n in range(numPhotos):

        photoAttr = list(map(str, content[i].split(' ')))
        isHorizontal = True if photoAttr[0] == 'H' else False
        numTags = int(photoAttr[1])
        tags = set()
        photo = Photo(isHorizontal, i,numTags, tags)
        j=2
        for L in range(numTags):
            tag = photoAttr[j]
            tags.add(tag)
            j += 1
            if tag in tagsToPhotoMap:
                tagsToPhotoMap[tag].append(photo)
            else:
                tagsToPhotoMap[tag] = [photo]


        photos.append(photo)
        i += 1
    return photos;


def main():
    inputFile = "exampleA_input.txt"
    with open("input/" + inputFile, "r") as f:
        content = f.read().splitlines()

    numPhotos = int(content[0])
    photos = extractPhotos(numPhotos, content)
    print(photos)
    print(calcScore(photos[0], photos[1]))

if __name__ == '__main__':
    main()