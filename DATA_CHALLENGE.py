#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos3= pd.read_csv("Saldos_Atms_Sucursales.csv", sep="|")


# In[2]:


v1 = datos3['CAS_1']*datos3['PIEZAS_CAS_1']
v2 = datos3['CAS_2']*datos3['PIEZAS_CAS_2']
v3 = datos3['CAS_3']*datos3['PIEZAS_CAS_3']
v4 = datos3['CAS_4']*datos3['PIEZAS_CAS_4']
vf = v1+v2+v3+v4


# ATMS OK ARRIBA DEL MÍNIMO

# In[4]:


datos3[vf >= datos3.MINIMO]


# ATMS OK ARRIBA DEL MÍNIMO AGRUPADOS POR DIVISIÓN

# In[5]:


(datos3[vf >= datos3.MINIMO]).groupby(['DIVISION']).mean()


# CONTEO DE ATMS ARRIBA DEL MÍNIMO AGRUPADOS POR DIVISION

# In[9]:


columnas=["DIVISION", "ATM"]
base=datos3[columnas]
res=base["DIVISION"].value_counts().to_frame()
res


# 
# GRÁFICA DE BARRAS DEL NÚMERO DE ATMS CON SALDO ARRIBA DEL MÍNIMO AGRUPADOS POR DIVISION

# 
# 

# In[18]:


res.plot(kind="bar", title="NÚMERO DE ATMS CON SALDO ARRIBA DEL MÍNIMO", figsize=(20,20))


# SALDO TOTAL

# In[19]:


new_datos3=datos3.assign(SaldoTotal=vf)


# NUEVA COLUMNA SaldoTotal

# In[20]:


new_datos3


# In[ ]:





# In[ ]:





# SALDO 25% MENOR AL MÍNIMO CRITICIDAD C

# In[ ]:





# In[ ]:




