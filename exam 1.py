import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42) 
data = pd.DataFrame({
    'no.of sales': np.random.randint(20,100,size=12),
    'advertizing amount': np.random.uniform(10,70,size=12)
})
print(data.head())
correlation_coefficient = data['no.of sales'].corr(data['advertizing amount'])
print(f'Correlation Coefficient: {correlation_coefficient}')
plt.figure(figsize=(10, 6))
plt.scatter(data['no.of sales'], data['advertizing amount'], alpha=0.5)
plt.title('No.of sales vs Advertizing amount')
plt.xlabel('No.of sales')
plt.ylabel('Advertizing amount')
plt.grid(True)
plt.show()
