#!/usr/bin/env python3
# coding: utf-8

import urllib.request
import urllib.error
import json
import os
import platform
import time

# 必应获取美图的API：
# （无水印）http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1
# 这里会包含一个包含图片资源URL的文本（JSON格式）
# 上面的URL参数自行体验吧。
# 资源{"images":[{"url":"xxxx"}]}



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


def get_bing_today_homepage_data():
    count = 0
    while count < 5:
        try:
            bing_today_homepage_url = get_bing_today_homepage()
            return urllib.request.urlopen(bing_today_homepage_url).read()
        except urllib.error.URLError as e :
            print( e.reason() )
            print("Try again.")
        time.sleep(10)
        count += 1
    return None


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

    urllib.request.urlretrieve(bing_today_homepage, win7_oobe)
    if os.path.getsize(win7_oobe) >= 255 * 1024:
        reduce_the_size(win7_oobe)


def set_up_linux_background_file():
    global bing_lock_screen_file
    data = get_bing_today_homepage_data()
    if data != None:
        open(bing_lock_screen_file, 'wb').write(data)


def set_up_ubuntu_lightdm_settting():
    global dist_ver
    major_ver = int(float(dist_ver))
    if 14 <= major_ver <= 16:
        import configparser
        print("14.x ~ 16.x version")
        # [com.canonical.unity-greeter]
        # draw-user-backgrounds=false
        # background='/foo/wallpaper.png'
        c_section = 'com.canonical.unity-greeter'

        config_path = '/usr/share/glib-2.0/schemas/10_unity-settings-daemon.gschema.override'
        config = configparser.ConfigParser()
        config.read(config_path)
        need_to_compile_schemas = False
        if c_section not in config:
            need_to_compile_schemas = True
            config.add_section(c_section)
            config[c_section]['draw-user-backgrounds'] = 'false'
            config[c_section]['background'] = "'/var/bing_lock_screen.jpg'"
        else:
            try:
                if config[c_section]['draw-user-backgrounds'] != 'false':
                    config[c_section]['draw-user-backgrounds'] = 'false'
                    need_to_compile_schemas = True
                if config[c_section]['background'] != "'/var/bing_lock_screen.jpg'":
                    config[c_section]['background'] = "'/var/bing_lock_screen.jpg'"
                    need_to_compile_schemas = True
            except KeyError:
                config[c_section]['draw-user-backgrounds'] = 'false'
                config[c_section]['background'] = "'/var/bing_lock_screen.jpg'"
                need_to_compile_schemas = True
        if need_to_compile_schemas:
            config.write(open(config_path, 'w'))
            os.system("glib-compile-schemas /usr/share/glib-2.0/schemas/")
            print("You need to restart lightdm to take effect.")


if __name__ == '__main__':
    system = platform.system()
    if system.lower() == 'Windows'.lower():
        import winreg

        win_release = platform.win32_ver()[0]
        if win_release == '7':
            set_up_windows_7_oem_background_reg()
            set_up_windows_7_oem_background_file()
        else:
            print("Not Support version of Windows: {0}".format(win_release))
            exit(1)
    elif system.lower() == 'Linux'.lower():
        linux_dist, dist_ver, dist_id = platform.dist()
        bing_lock_screen_file = '/var/bing_lock_screen.jpg'
        if linux_dist.lower() == 'Ubuntu'.lower():
            set_up_ubuntu_lightdm_settting()
        else:
            print("Not Support version of Linux distribution: {0}".format(linux_dist))
            exit(1)
        set_up_linux_background_file()
