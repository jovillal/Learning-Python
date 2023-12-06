#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:42:03 2023

@author: jovillal
"""
gmf = 4/1000
comisionVP = 65/10000 
comisionVariableIVAP = 19/100
reteFuenteP = 11/100 
reteICAP = 966/100000

amount_received = input('amount_received:')
rate_cop_usd=input('rate_cop_usd:')
#rate_token=input('rate_token:')
#fixed_fee=input('fixed_fee:')

amount_sent = (float(amount_received)*(1 + gmf))

amount_sent = amount_sent/(float(rate_cop_usd)*(1 - comisionVP*(1 + comisionVariableIVAP - (1 + gmf)*(reteFuenteP + reteICAP))))

print(amount_sent )
