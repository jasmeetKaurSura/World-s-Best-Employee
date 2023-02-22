# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(RANK, NAME)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
# Import the libraries
from matplotlib import pyplot as plt
import numpy as np
dataset.sort_values('RANK', inplace=True) 
# Creating values (budget amount) for the bars
iN = len(dataset)
arrCnts = dataset['RANK']/10
theta=np.arange(0,2*np.pi,2*np.pi/iN)
width = (2*np.pi)/iN *0.9 
# Plot size and proportions
fig = plt.figure(figsize=(20,18),frameon=False,dpi=200)

# Adding radial axes
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9], polar=True)
bars = ax.bar(theta, arrCnts, width=width, bottom=15,alpha=0.65,edgecolor='black')

ax.set_xticks(theta)
plt.axis('off')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

bottom = 15
rotations = np.rad2deg(theta)
y0,y1 = ax.get_ylim()

# Adding radial tags
for x, bar, rotation, label in zip(theta, bars, rotations, dataset['NAME']):
    offset = (bottom+bar.get_height())/(y1-y0)
    lab = ax.text(0, 0, label, transform=None, 
             ha='center', va='center',alpha=1)
    renderer = ax.figure.canvas.get_renderer()
    bbox = lab.get_window_extent(renderer=renderer)
    invb = ax.transData.inverted().transform([[0,0],[bbox.width,0] ])
    lab.set_position((x,offset+(invb[1][0]-invb[0][0])/2.*2.7 ) )
    lab.set_transform(ax.get_xaxis_transform())
    lab.set_rotation(rotation) 

fig.tight_layout()
plt.show()

