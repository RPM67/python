import qrcode as qr

img = qr.make("https://www.youtube.com/watch?v=Ez8F0nW6S-w")  # convert the provide link into qrcode and store it in 'img'

img.save("GGitHubTutorialByApnaCollege.png")  # it saves the image of qrcode stored in 'img' with provided file name
