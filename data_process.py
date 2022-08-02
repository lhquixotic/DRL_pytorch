import matplotlib.pyplot as plt
f = open("vfe.txt","r")
a = [line.rstrip() for line in f]
vfe = [float(line.split()[-1]) for line in a]

ax = plt.gca()
ax.plot(range(len(vfe)), vfe, label="VFE", color='r')
ax.set_facecolor('xkcd:white')

ax.set_title("Variational Free Energy", fontsize=15, fontweight='bold')
ax.set_ylabel('VFE')
ax.set_xlabel('Step Number')
plt.show()