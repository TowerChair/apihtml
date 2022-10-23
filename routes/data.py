from bson import ObjectId
from fastapi import APIRouter, status,Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from schemas.data import userEntity
from models.data import Data


data = APIRouter()

@data.post('/data', response_model=Data,tags=["data"] )
async def getAllData(data: Data): 
    new_data = dict(data)
    soup = BeautifulSoup(data.data, 'lxml')
    name_div = soup.find('div', {'class': 'display-flex mt2'})

    # name
    try:
        name = name_div.find('li', {'class': 'inline t-24 t-black t-normal break-words'}).get_text().strip()
    except IndexError: # To ignore any kind of error
        name = 'NULL'
    except AttributeError:
        name = 'NULL'

    # location
    try:
        location = name_div.find('li', {'class': 't-16 t-black t-normal inline-block'}).get_text().strip()
    except IndexError:
        location = 'NULL'
    except AttributeError:
        location = 'NULL'

    # degree_level
    try:
        degree_level = name_div.find('span', {'class': 'dist-value'}).get_text().strip()
    except IndexError:
        degree_level = 'NULL'
    except AttributeError:
        degree_level = 'NULL'
        
    # No. of connections            
    try:
        c_div = name_div.find('ul', {'class': 'pv-top-card--list pv-top-card--list-bullet mt1'})
        connections = c_div.find('span', {'class': 't-16 t-black t-normal'}).get_text().strip()
    except IndexError:
        connections = 'NULL'
    except AttributeError:
        connections = 'NULL'


    # Professional Details
    Experience_div = soup.find('div', {'class': 'pv-entity__summary-info pv-entity__summary-info--background-section'})

    # recent positions
    try:
        job_title = Experience_div.find('h3', {'class': 't-16 t-black t-bold'}).get_text().strip()
    except IndexError:
        job_title = 'NULL'
    except AttributeError:
        job_title = 'NULL'
        
    #company name
    try:
        company_name = soup. find('p', {'class': 'pv-entity__secondary-title t-14 t-black t-normal'}).get_text().strip()
    except IndexError:
        company_name = 'NULL'
    except AttributeError:
        company_name = 'NULL'   
        
    #experience
    try:
        experience = soup. find('span', {'class': 'pv-entity__bullet-item-v2'}).get_text().strip()
    except IndexError:
        experience = 'NULL'
    except AttributeError:
        experience = 'NULL'

        
    # saving outputs
    output = ({'Name': name}) 

    print(output)
    return userEntity(new_data)
