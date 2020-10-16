
import numpy as np 
import pandas as pd 



df = pd.DataFrame({"A":[12, 4, 5, None, 1], 
                   "B":[None, 2, 54, 3, None], 
                   "C":[20, 16, None, 3, 8], 
                   "D":[14, 3, None, None, 6]}) 

print(df.loc[([1,3,4])])




# Creating the dataframe  
# df = pd.DataFrame({"A":[12, 4, 5, None, 1], 
#                    "B":[None, 2, 54, 3, None], 
#                    "C":[20, 16, None, 3, 8], 
#                    "D":[14, 3, None, None, 6]}) 

# print(df)

# # interpolation
# print(df)
# df2 = df.interpolate(method ='linear', limit_direction ='both') 
# print(df2)


# frente e traz
# df2 = df.fillna(method='bfill')
# df2 = df.bfill().ffill()
# print(df2)

# # method : {linear, time, index, values, nearest, zero, slinear, quadratic, cubic, barycentric, krogh, polynomial, spline, piecewise_polynomial, from_derivatives, pchip, akima}


## estranha
# df = pd.DataFrame([(0.0, np.nan, -1.0, 1.0),
#                    (np.nan, 2.0, np.nan, np.nan),
#                    (2.0, 3.0, np.nan, 9.0),
#                    (np.nan, 4.0, -4.0, 16.0)],
#                   columns=list('abcd'))

# print(df)
# df2 = df['d'].interpolate(method='spline', order=2)
# print(df2)


# import numpy as np
# from sklearn.impute import SimpleImputer
# imp = SimpleImputer(missing_values=np.nan, strategy='mean')
# imp.fit([[1, 2], [np.nan, 3], [7, 6]])
# X = [[np.nan, 2], [6, np.nan], [7, 6]]
# print(imp.transform(X))
