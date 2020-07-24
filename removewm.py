import pikepdf
import sys


def deleteWatermark(inputFileName, outputFileName):
    pdf = pikepdf.open(inputFileName)

    for page in pdf.pages:
        imageList = list(page.images.keys())
        # delete link
        del page["/Annots"][0]
        # delete image
        for image in imageList:
            del page["/Resources"]["/XObject"][image]

    pdf.save(outputFileName)
    print("The Watermark from {} has been removed and saved into {} ".format(
        inputFileName, outputFileName))


if __name__ == '__main__':
    deleteWatermark(str(sys.argv[1]), str(sys.argv[2]))
