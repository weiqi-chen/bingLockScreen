#!/usr/bin/env python3
# coding: utf-8

import winreg
import urllib.request
import json
import os
import platform

# 必应获取美图的API：
# （无水印）http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1
# 这里会包含一个包含图片资源URL的文本（JSON格式）
# 上面的URL参数自行体验吧。
# 资源{"images":[{"url":"xxxx"}]}


test = False


def reduce_the_size(name):
    import PIL.Image
    im = PIL.Image.open(name)
    im.resize((1366, 768)).save(name)
    if os.path.getsize(name) >= 255 * 1024:
        im.resize((1280, 720)).save(name)
    if os.path.getsize(name) >= 255 * 1024:
        im.resize((960, 540)).save(name)


def get_bing_today_homepage():
    # 使用CN域名网速会快一些。
    host_prefix = 'https://cn.bing.com'
    bing_api_url = '/HPImageArchive.aspx?format=js&idx=0&n=1'
    res = urllib.request.urlopen(host_prefix + bing_api_url).read().decode('utf8')  # 有时候，read()返回的是bytes，调用一下decode稳妥一些
    js = json.loads(res)
    return host_prefix + js['images'][0]['url']


def set_up_windows_7_oem_background_reg():
    mid_key_str = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Authentication\\LogonUI\\Background'
    target_key_name = 'OEMBackground'
    top_key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, mid_key_str,
                                 access=winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
    winreg.SetValueEx(top_key, target_key_name, 0, winreg.REG_DWORD, 1)


def set_up_windows_7_oem_background_file():
    bing_today_homepage = get_bing_today_homepage()
    _a = os.environ['WINDIR'] + '\\'
    # 32 bit python.exe running on a windows 64 bit system
    if platform.machine() == 'AMD64' and platform.architecture()[0] == '32bit':
        _b = 'Sysnative\\'
    else:
        _b = 'System32\\'
    _c = 'oobe\\info\\backgrounds\\backgroundDefault.jpg'
    win7_oobe = _a + _b + _c
    win7_oobe_dir = os.path.dirname(win7_oobe)

    if not os.path.exists(win7_oobe_dir):
        os.makedirs(win7_oobe_dir, exist_ok=True)

    if test == True:
        win7_oobe = 'D:\\test.jpg'
    urllib.request.urlretrieve(bing_today_homepage, win7_oobe)
    if os.path.getsize(win7_oobe) >= 255 * 1024:
        reduce_the_size(win7_oobe)


if __name__ == '__main__':
    set_up_windows_7_oem_background_reg()
    set_up_windows_7_oem_background_file()
