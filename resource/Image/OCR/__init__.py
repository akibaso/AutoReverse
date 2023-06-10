import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def recoText(image,target, lang='chi_sim'):
    """
    识别字符并返回所识别的字符及它们的坐标
    :param im: 需要识别的图片
    :return data: 字符及它们在图片的位置
    """
    img = Image.open(image)

    # 进行文字识别并返回识别结果和文字所在位置
    result = pytesseract.image_to_data(img,lang=lang, output_type=pytesseract.Output.DICT)
    print(result['text'])
    # 遍历识别结果中的每一个单词
    for i, word in enumerate(result['text']):
        # 判断该单词是否为特定文字
        if target in word:
            # 获取该单词所在位置的信息
            left = result['left'][i]
            top = result['top'][i]
            width = result['width'][i]
            height = result['height'][i]
            return left,top




