# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rw81DSU2TcyELKT4bqRD16wCcoAJUkCC
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

#downloaded = drive.CreateFile({'id':'1nHSHmz1E8wNu1loEJapn8bxgGJuUH2sm'})
#downloaded.GetContentFile('users.csv')  
#users = pd.read_csv('users.csv')
downloaded2 = drive.CreateFile({'id':'1Z-f2dmfw2W0gbQf65ztRL6iuhWsn8Rxg'}) 
downloaded2.GetContentFile('attend.csv')      
attend = pd.read_csv('attend.csv', 
                 usecols=['activity_name'.strip(), 'host_time'],
                 parse_dates=['host_time'])

attend['month_num'] = (pd.DatetimeIndex(attend['host_time']).month)
attend_grouped = attend.groupby(['month_num'])

attend.head()

attend_grouped.month_num.sum().plot(kind='bar',x='Month',y='Number of Attendees',title='Number of Activity Attendees by Month')

attend_grouped.month_num.sum().plot(kind='line',x='Month',y='Number of Attendees',title='Number of Activity Attendees by Month')