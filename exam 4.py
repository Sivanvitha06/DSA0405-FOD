import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42) 
data = pd.DataFrame({
    'no.of patients smoke': np.random.randint(20,100,size=20),
    'no.of patients got lung cancer': np.random.uniform(10,70,size=20)
})
print(data.head())
correlation_coefficient = data['no.of patients smoke'].corr(data['no.of patients got lung cancer'])
print(f'Correlation Coefficient: {correlation_coefficient}')
plt.figure(figsize=(10, 6))
plt.scatter(data['no.of patients smoke'], data['no.of patients got lung cancer'], alpha=0.5)
plt.title('No.of patients smoke vs no.of patients got lung cancer')
plt.xlabel('No.of patients smoke')
plt.ylabel('no.of patients got lung cancer')
plt.grid(True)
plt.show()
