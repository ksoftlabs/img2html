from PIL import Image


def loadImage(imgUrl):
    '''
        Load Image url
    '''
    return Image.open(imgUrl)


def getPixels(imgResources):
    return imgResources.load()


img = loadImage('ksoftlabs.png')
pixels = getPixels(img)

strHtml = ''
rgbaHtml = 'rgba({},{},{},{})'
innerObj = '<div style="background-color: {};" class="b"></div>'.format(rgbaHtml)

f = open('index.html', 'w')
strHtml=strHtml+'<head>'
strHtml=strHtml+'<title>KSoftLabs</title>'
strHtml=strHtml+'<style>.a{display:flex}.b{width:1px;height:1px;}</style>'
strHtml=strHtml+'</head>'
strHtml = strHtml + '<body>'
for i in range(img.size[0]):
    strHtml = strHtml + '<div class="a">'
    for j in range(img.size[1]):
        px = pixels[j, i]
        # print(px)
        strHtml += innerObj.format(px[0], px[1], px[2], px[3])

    strHtml = strHtml + '</div>'

strHtml = strHtml + '</body>'
f.write(strHtml)
