

class Photo:
    def __init__(self, id, isHorizontal, numTags, tags):
        self.id = id
        self.isHorizontal = isHorizontal
        self.numTags = numTags
        self.tags=tags

    def __repr__(self):
        return "Photo "+self.id.__str__() + ":" +self.tags.__str__();

def extractPhotos(numPhotos: int, content: list, tagsToPhotos: dict) :
    photos = []

    for n in range(numPhotos):
        photoAttr = list(map(str, content[n+1].split(' ')))
        isHorizontal = True if photoAttr[0] == 'H' else False
        numTags = int(photoAttr[1])
        tags = set()
        photo = Photo(n, isHorizontal,numTags, tags)
        for L in range(numTags):
            tag = photoAttr[L+2]
            tags.add(tag)
            if tag in tagsToPhotos:
                tagsToPhotos[tag].add(n)
            else:
                tagsToPhotos[tag] = set()
                tagsToPhotos[tag].add(n)


        photos.append(photo)
    return photos;

def arrangePhotos(photos: list, tagToPhotoId: dict) :
    sortedTags = sorted(tagToPhotoId, key=lambda p: len(tagToPhotoId[p]), reverse=True)
    print(sortedTags)
    arrangedPhotosSet = set()
    arrangedPhotosList = list()
    tag = sortedTags[0]
    while True:
        if(len(photos) == len(arrangedPhotosSet)):
            break

        photosWithThisTag = tagToPhotoId[tag];

        for photoId in photosWithThisTag:
            if photoId in arrangedPhotosSet:
                continue;
            arrangedPhotosSet.add(photoId)
            arrangedPhotosList.append(photoId)
            for photosTag in photos[photoId].tags:
                if(len(tagToPhotoId[photosTag]) > 1 and photosTag != tag):
                    tag = photosTag
                    break;


    return arrangedPhotosList

def calcScore(arrangedPhotos: list, photos: list):
    prevPhotoId = arrangedPhotos[0]
    i = 1;
    total = 0
    for n in range(len(arrangedPhotos)-1):
        p1 = photos[prevPhotoId]
        p2 = photos[arrangedPhotos[i]]
        p1Tags = p1.tags
        p2Tags = p2.tags
        total += min(len(p1Tags.difference(p2Tags)), len(p2Tags.difference(p1Tags)), len(p1Tags.intersection(p2Tags)))
        prevPhotoId = i
        i += 1

    return total

def main():
    inputFile = "exampleA_input.txt"
    with open("input/" + inputFile, "r") as f:
        content = f.read().splitlines()

    numPhotos = int(content[0])
    tagsToPhotos = {}
    photos = extractPhotos(numPhotos, content, tagsToPhotos)
    arrangedPhotos = arrangePhotos(photos, tagsToPhotos)
    print(photos)
    #print(calcScore(photos[0], photos[1]))

    print(arrangedPhotos)
    print(calcScore(arrangedPhotos, photos))

if __name__ == '__main__':
    main()