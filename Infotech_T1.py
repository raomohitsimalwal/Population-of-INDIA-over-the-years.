import matplotlib.pyplot as plt
import pandas as pd

file_path = "D:\OneDrive\Prodigy InfoTech\India_population_data.xls"

years = pd.read_excel(file_path, header=None, skiprows=3, usecols='E:BO', nrows=1).values.flatten()

population = pd.read_excel(file_path, header=None, skiprows=113, usecols='E:BO', nrows=1).values.flatten()

data = pd.DataFrame({'Year': years, 'Population': population})

plt.bar(data['Year'], data['Population'], color='blue', alpha=0.7, label='Population')

plt.title('Population of India Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Population (Billion)')
plt.grid(True)
plt.legend()

plt.show()
