from matplotlib import pyplot
import matplotlib.pyplot as ax

s = []
with open('settings.txt', 'r') as settings:
    arr = settings.readlines()
    for i in arr:
        a = ''.join(i)
        s.append(float(a))

y = []
with open('data.txt', 'r') as data:
    arr = data.readlines()
    for i in arr:
        a = ''.join(i)
        y.append(float(a))

ax.minorticks_on()
ax.title('Charging and uncharging processes in RC')
ax.ylabel('Voltage U, B')
ax.xlabel('Time t, c')
ax.xlim([0, 90])
ax.ylim([0,3.3])
ax.grid(which='major', linestyle='-.')
ax.grid(which='minor', linestyle=':')
ax.tight_layout()
ax.text(55, 2.3, 'Time of charging: 34,4 c')
ax.text(55, 1.9, 'Time of uncharging: 46,4 c')

x=[]
y_true=[]
for i in range(len(y)):
    x.append(i/s[0])
    y_true.append(y[i]*3.3/256)
ax.plot(x, y_true, '-', color='r', label='U(t)')
ax.scatter(x[::30], y_true[::30], color='g', label = 'Experimental dots')

ax.legend(fontsize=14)
ax.show()
fig.savefig('U(t).svg')
print(min(y), max(y))