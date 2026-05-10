import pandas as pd

data={
       'Region':['North','East','West','South'],
        'Sales':[100,200,300,400],
         'Product':['A','B','C','D']
}
df=pd.DataFrame(data)
print("Original Data:\n")
print(df)

print("\nRoll-UP\n")

roll_up=df.groupby('Region')['Sales'].sum()
print(roll_up)

print("\nDrill-Down:\n")

drill_down=df[df['Region']=='North']

print(drill_down)

print("\nSlice:\n")
slice=df[df['Region']=='East']
print(slice)

print("\nDice:\n")

dice=df[(df['Region']=='West')&(df['Product']=='C')]
print(dice)

print("\nPivot:\n")

pivote=df.pivot_table(
    values='Sales',
    index='Region',
    columns='Product',
    fill_value=0
)
print(pivote)