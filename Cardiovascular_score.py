import numpy as np
import pandas as pd

def Cardiovascular_score(**kwargs):
    # Assign "none" to missing values presented as errors
    var = dict.fromkeys(kwargs, None)
    for k in kwargs:
        ck = isinstance(kwargs[k], (int, float))
        if ck == False:
            er = "error" in kwargs[k]
            if er:
                var[k] = None
            else:
                var[k] = kwargs[k]
        else:
            var[k] = kwargs[k]

    # Give variables shorter names
    var["Smoker"] = var.pop("Current smoker")
    var["Sex"] = var.pop("SEX_CATEGORICAL")
    var["SystolicBP"] = var.pop("AVG_2_SBP")
    var["cholesterol"] = var.pop("Total Cholesterol (mmol/L)")
    var["DiastolicBP"] = var.pop("AVG_2_DBP")
    var["Diabetic"] = var.pop("Dx_Diabetes_10B")
    var["hdl_cholesterol"] = var.pop("HDL Cholesterol (mmol/L)")
    var["Age"] = var.pop("AGE")
    var["GFR"] = var.pop("eGFR (ml/min/1.73m2)")
    var["ECG"] = var.pop("OR_ECG_LVH")
    var["Alb_Creat_ratio"] = var.pop("Albumin/Creatinine (ACR)")
    var["heart_disease"] = var.pop("Dx_Heart Disease")
    
   #Check if the person has high risk of developing CVD
   check1=int(var["heart_disease"]==1) #Not sure what to do here
   check2=int(var["Age"]>=75)
   check3=int(var["Diabetic"]==1 and var["Age"]>60)
   check4=int(var(["Diabetic"]==1 and (var["Sex"]=="m" and var["Alb_Creat_ratio"]>2.5) or (var["Sex"]=="f" and var["Alb_Creat_ratio"]>3.5)))
