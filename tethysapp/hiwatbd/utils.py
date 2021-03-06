import datetime
import requests
from .config import *
import xml.etree.ElementTree as ET


def get_thredds_info():
    catalog_url = THREDDS_catalog

    catalog_wms = THREDDS_wms

    urls_obj = {}
    if catalog_url[-1] != "/":
        catalog_url = catalog_url + '/'

    if catalog_wms[-1] != "/":
        catalog_wms = catalog_wms + '/'

    catalog_xml_url = catalog_url+'catalog.xml'

    possible_dates = []
    valid_dates = []

    cat_response = requests.get(catalog_xml_url,verify=False)

    cat_tree = ET.fromstring(cat_response.content)

    for elem in cat_tree.iter():
        for k, v in list(elem.attrib.items()):
            if 'title' in k:
            # if 'title' in k and '2018' in v:
                possible_dates.append(v[:8])

    for date in possible_dates:
        try:
            valid_date = datetime.datetime.strptime(date, "%Y%m%d")
            valid_dates.append(valid_date)

        except Exception as e:
            print("this is error")
            print(date)
            continue


    latest_date = max(valid_dates).strftime("%Y%m%d12")

    date_xml_url = catalog_url + latest_date + '/catalog.xml'

    date_xml = requests.get(date_xml_url, verify=False)

    date_response = ET.fromstring(date_xml.content)

    for el in date_response.iter():
        for k, v in list(el.items()):
            if 'urlPath' in k:
                if 'Control' in v:
                    urls_obj['det'] = catalog_wms+v
                if 'hourly' in v:
                    urls_obj['hourly'] = catalog_wms+v
                if 'day1' in v:
                    urls_obj['day1'] = catalog_wms+v
                if 'day2' in v:
                    urls_obj['day2'] = catalog_wms+v

    return urls_obj