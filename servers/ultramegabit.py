# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand - XBMC Plugin
# Conector para ultramegabit
# http://www.mimediacenter.info/foro/viewforum.php?f=36
#------------------------------------------------------------

import re

from core import logger


def get_video_url( page_url , premium = False , user="" , password="", video_password="" ):
    logger.info("[ultramegabit.py] get_video_url(page_url='%s')" % page_url)
    video_urls = []
    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    # http://ultramegabit.com/file/
    patronvideos  = '(ultramegabit.com/file/details/[^"]+)'
    logger.info("[ultramegabit.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[ultramegabit]"
        url ='http://'+match
        if url not in encontrados:
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'ultramegabit' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    return devuelve
