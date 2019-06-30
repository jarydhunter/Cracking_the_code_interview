import math
# Rotate image in place, assume in python the image is represented as a nested
# list.
def rotate_img_90(img):
    max_index = len(img) - 1
    for i in range((len(img)+1)//2):
        for j in range(len(img)//2):
            tmp1 = img[i][j]
            tmp2 = img[max_index - j][i]
            tmp3 = img[max_index - i][max_index - j]
            tmp4 = img[j][max_index - i]

            img[max_index - j][i] = tmp1
            img[max_index - i][max_index - j] = tmp2
            img[j][max_index - i] = tmp3
            img[i][j] = tmp4
    return img

if __name__ == "__main__":
    test1 = [[1,3], [2,4]]
    print(rotate_img_90(test1))

    test2 = [[1,4,7],[2,5,8],[3,6,9]]
    print(rotate_img_90(test2))

    test3 = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
    print(rotate_img_90(test3))