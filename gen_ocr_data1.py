# -*- coding: utf-8 -*-

'''
Created on 2020/12/17  15:54

@project: OCR

@filename: gen_ocr_data1.py

@author: knavezl

@Desc:    
    生成数据
'''

import os,math
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 文字转图片
def text_to_img(char,img_size,font_type,margin,rotate_rate,save_img_path):
    '''

    :param char: 输入字符
    :param img_size: 图片大小
    :param font_type: 字体类型
    :param save_img_path: 保存路径
    :param margin: 偏移
    :param rotate_rate: 旋转角度
    :param save_img_path: 保存路径
    :return:
    '''

    # 黑色背景
    gen_image = Image.new('RGBA', (img_size,img_size), "black")  # 创建一个新图
    draw = ImageDraw.Draw(gen_image)
    #font = ImageFont.truetype('font/simsun.ttc', font_size)

    # 白色字体
    draw.text((margin, margin), char, (255, 255, 255), font=font_type)

    # 旋转图像
    if rotate_rate != 0:
        gen_image = gen_image.rotate(rotate_rate, expand=0,fillcolor="black")
    #new_image.show()

    #保存图片
    gen_image.save(os.path.expanduser(save_img_path))




if __name__ == '__main__':
    font_dir='data/font/'
    font_list=os.listdir(font_dir)
    #print('font_list=',font_list)


    file = open('data/hanzi.txt', encoding='utf-8-sig')
    data = np.loadtxt(file, str, delimiter=",")
    char_list=data[:,0]
    index_list=data[:,1]
    # print('char_list=',char_list)
    # print('index_list=',index_list)

    img_save_path = 'data/images/'

    rotate_list=[0,30,45,60,300,315,330]

    #遍历字体
    for i in range(len(font_list)):
        font_type = ImageFont.truetype(font_dir+font_list[i], 40)
        print('**********生成',font_list[i],'字体图片**********')

        #遍历字符
        for j in range(10):
        #for j in range(len(char_list)):
            if j%1000==0:
                print('**********生成第', j+1, '个字的图片**********')
            # 创建目录
            if not os.path.exists(img_save_path+str(index_list[j])+'/'):
                os.makedirs(img_save_path+str(index_list[j])+'/')

            #遍历旋转角度
            for k in range(len(rotate_list)):
                text_to_img(char_list[j], 50, font_type,5,rotate_list[k], img_save_path+str(index_list[j])+'/'+str(i)+'_'+str(index_list[j])+'_'+str(k)+'.png')