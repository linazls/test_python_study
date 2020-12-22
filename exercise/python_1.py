# -*- coding: utf-8 -*-
from GCAir import *

#变量名称 =Variable("显示名称", "变量类型", "描述信息", 默认值)

in_1 = Variable("in_1", "input","", 0.0)

in_2 = Variable("in_2", "input","", 0.0)

out_1 = Variable("out_1", "output","", 0.0)

out_2 = Variable("out_2", "output","", 0.0)

out_3 = Variable("out_3", "output","", 0.0)

parameter_1 = Variable("parameter_1", "parameter","", 0.0)

parameter_2 = Variable("parameter_2", "parameter","", 0.0)

parameter_3 = Variable("parameter_3", "parameter","", 0.0)

parameter_4 = Variable("parameter_4", "parameter","", 0.0)

def Init():
#	Insert Initialize Code Here
	return


def DoStep(t_start, t_step):
#	Insert DoStep Code Here
	return


#Simple Example
#def Init():
#	# initialize variables for t=0	
#	var1.value=0
#	var2.value=10
# 	
#def DoStep(t_start, t_step):
#	if(time.value >5):
#		var1.value = cos(time)
#	elif(time.value>8):
#		var1.value = 2
#	else:
#		var1.value = 1
#		var2.value = var1.prevalue
#


