from django.shortcuts import render
from .models import Student
import pandas as pd
import numpy as np

import os
# Create your views here.
def index(request):
    #item = Student.objects.all().values()
    df=getir("EBE","templates/2021.xlsx")
    df = pd.DataFrame(data=df,columns=["KODU","SB KODU","KURUM ADI","POZİSYON UNVANI","İL ADI","POZİSYON SAYISI"])
    #df= df[["KODU","SB KODU"]]
    #df.drop("POZİSYON SAYISI",axis=1,inplace=True)
    #print(df.iloc[0])
    #print(df.loc[4,"KODU"])
    #print(df.loc[[4,18],["KODU","SB KODU"]])
    #df=df[df['POZİSYON SAYISI']<5]
    #df=df[df['İL ADI']=="İSTANBUL"]
    df.set_index("POZİSYON UNVANI",inplace=True)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'index.html', context=mydict)
def getir(pozisyon,yıl):
    obje=pd.read_excel(yıl)
    kelime=obje['POZİSYON UNVANI']==pozisyon
    df=obje[kelime]
    return df
