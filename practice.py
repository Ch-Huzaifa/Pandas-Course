import pandas as pd
data={
    "Name":['Huzaifa','Shuban','Taimoor','Ahsan','Ali'],
    "Age":[20,21,21,22,35],
    "Arid_no":['24-Arid-801','24-Arid-848','24-Arid-852','24-Arid-791','24-Arid-795'],
    "City":['Rawalpindi','Mansehra','KotliSattiyan','Rawalpindi','Chakwal'],
    "Salary":[80000,75000,70000,20000,5000]
}

df=pd.DataFrame(data)
print (df[df["Salary"] >= 70000])
print(df[(df["Salary"] >= 70000)&(df["Age"]<=20)])