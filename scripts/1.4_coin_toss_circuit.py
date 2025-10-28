#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator


# In[51]:


q = QuantumRegister(2)
c = ClassicalRegister(2)

qc = QuantumCircuit(q, c)
qc.h(q)

qc.measure(q, c)
qc.draw("mpl", filename="artifacts/draw.pdf")   # text, latex, latex_source, and mpl
plt.show()




# In[50]:


simulator = AerSimulator()
job = simulator.run(qc)

results = job.result()
iterations = results.results[0].shots
print(iterations)
counts = results.get_counts(qc) # give us counts for each basis
print(counts)


# In[48]:


plot_histogram(counts)

