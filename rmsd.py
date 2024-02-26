# module importing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data loading
df1=pd.read_excel('PL_RMSD_111313.xlsx')
df2=pd.read_excel('PL_RMSD_40354.xlsx')
df3=pd.read_excel('PL_RMSD_35505.xlsx')
#df4=pd.read_excel('PL_RMSD_CCL.xlsx')

# ploting of graph from RMSD Data
plt.plot(df1['frame']/10, df1['Lig_wrt_Protein']/10, label='111313')
plt.plot(df2['frame']/10, df2['Lig_wrt_Protein']/10, label='40354')
plt.plot(df3['frame']/10, df3['Lig_wrt_Protein']/10, label='35505')
#plt.plot(df4['frame']/10, df4['Lig_wrt_Protein']/10, label='CCL')

plt.xlabel('Simulation time (ns)')
plt.ylabel('Ligand RMSD (nm)')
plt.ylim([0, 2.0])
plt.legend(loc='upper right')
plt.legend(frameon=False)
plt.savefig('rmsd_otava_ligand_7meq.png', dpi=300)

