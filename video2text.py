#!/usr/bin/python
# -*- coding: utf-8 -*-
from video2text.analyze_key_frame import subtitle_frame
from video2text.extract_index_frame import extract_index_frame
from video2text.ocr import text_process, save_subtitle
from video2text.pdocr.infer import utility
from video2text.pdocr.pyocr.utils.utility import get_image_file_list
import warnings
warnings.simplefilter("ignore")  #忽略告警

def video2textImpl(video_path):
    args = utility.parse_args()
    args.video_path = video_path
    args.threshold = 0.2
    args.top = 35  # 35
    args.bottom = 0
    args.left = 20
    args.right = 20
    args.bg_mod = 1  # 深色背景
    key_frame_index = subtitle_frame(args.video_path, args.top, args.bottom, args.left, args.right, args.threshold,
                                     args.bg_mod)
    key_frame_num = len(key_frame_index)
    subtitle_path = extract_index_frame(args.video_path, key_frame_index, args.top, args.bottom, args.left, args.right)
    image_list = get_image_file_list(subtitle_path)
    subtitle = text_process(args, image_list)
    return subtitle
if __name__ == '__main__':
    args = utility.parse_args()
    args.video_path = 'F:/pycharm/data/Mutimodal2Text/video2text/data/videos/demo0.flv'
    args.threshold = 0.2
    args.top =35 #35
    args.bottom = 0
    args.left = 20
    args.right = 20
    args.bg_mod = 1  # 深色背景

    print('####### 1.分析字幕关键帧 #######')
    key_frame_index = subtitle_frame(args.video_path, args.top, args.bottom, args.left, args.right, args.threshold, args.bg_mod)
    key_frame_num = len(key_frame_index)
    print('\n####### 2.提取字幕关键帧 #######')
    #subtitle_path = 'F:/pycharm/data/Mutimodal2Text/video2text/data/results/demo0/'
    subtitle_path = extract_index_frame(args.video_path, key_frame_index, args.top, args.bottom, args.left, args.right)
    image_list = get_image_file_list(subtitle_path)
    print('\n####### 3.OCR识别字幕帧 #######')
    subtitle = text_process(args, image_list)
    print('\n####### 4.打印字幕结果 #######')
    print(subtitle)
    save_subtitle(subtitle, subtitle_path)

