### Handelling Missing Value...
#      1.REPLACE- for replacing data
#      2.INTERPOLATE-


##  REPLACE FUCTION()
import pandas as pd
var=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv")
print(var)

print(var.replace(to_replace=11,value=25))                  # replace number
print(var.replace(to_replace="Male",value="Third Gender"))  # replace string
print(var.replace([1,2,3],10))                              # replace index-no[1,2,]..shoud be in list

# Replace by passing regex=true parameter
print(var.replace("[A-Z]","java",regex=True))               # replace using list
print(var.replace({"Gender":"[A-Z]"},22,regex=True))

print(var.replace(22,method="bfill"))                        # method..replace 22 with bfill/ffill
print(var.replace(22,method="ffill",limit=3))                # replace in limit parameter

var.replace(3,method="ffill",limit=3,inplace=True)           # inplace is used to replace in original data..(it does not create copy of replaced data)
print(var)



## INTERPOLATE FUNCTION()...it fill automatically missing data from previous data in a sequence

var=pd.read_csv("C:\\Users\\Welcome\\Desktop\\EXCEL\\p2.csv")
print(var)
                     
print(var.interpolate())           #it fill data in linear

# to Linear we use...methd:{'linear','time','index','value','nearest','zero','slinear','quadratic','cubic',
#    'barycentric','krogh','polynomial','spline','piecewise_polynomial','from_derivatives','pchip','akima'}

print(var.interpolate(method="linear",axis=0))             # it does not work with axis=1,it is string dtype

print(var.interpolate(limit=5))                            # fill data in limit
print(var.interpolate(limit_direction="both"))             # both= ffill & bfill       
print(var.interpolate(limit_direction="both",limit=2))   

# inside..fill all missing value, outside..return data with NaN value
print(var.interpolate(limit_area="inside"))                 #inside..fill all missing value (ffill/bfill)
print(var.interpolate(limit_area="outside"))                #outside..return data with NaN value

# Inplace.. (True = place all value in original file...False = make multiple copy)
print(var.interpolate(limit_area="inside",inplace=True))   


