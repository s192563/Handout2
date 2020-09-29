# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:19:12 2020

@author: APEROOO
"""
import pandas as pd

Dataset=pd.read_csv("C:/Users/Popof/Desktop/Dataset.csv",sep=';')
Dataset['SENIOR']=Dataset['AGE']==5
Dataset['Vcar']=-0.608-0.0111*Dataset['CAR_TT']-0.00936*Dataset['CAR_CO']-1.88*Dataset['SENIOR']
Dataset['Vtrain']=-0.0111*Dataset['TRAIN_TT']-0.0268*Dataset['TRAIN_CO']-0.00586*Dataset['TRAIN_HE']+0.557*Dataset['GA']
Dataset['Vsm']=-0.135-0.0111*Dataset['SM_TT']-0.0104*Dataset['SM_CO']-0.00586*Dataset['SM_HE']-1.88*Dataset['SENIOR']+0.557*Dataset['GA']

