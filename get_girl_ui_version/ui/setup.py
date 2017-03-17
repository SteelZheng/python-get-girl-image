from distutils.core import setup
import py2exe

setup(options={'py2exe':{'excludes':['re','sys','threading',
    'PyQt5','urllib','os','_util','requests','bs4']}}, windows=['ui_main.py','GetMezi.py','MyThreads.py'])