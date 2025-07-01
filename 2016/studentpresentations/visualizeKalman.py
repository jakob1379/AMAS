import numpy as np
from matplotlib import pyplot as plt

# System characteristics
nStates = 3
nObervations = 2
radius = 1
dTheta = 2*np.pi
dt = 0.001

# The width of the Gaussian from which the noise added to the true observation is drawn (This of course would be
# something inherent to the measurement device or method and not something we would explicitly set)
trueObservationNoise = 0.3
# In the ideal situation where we would/could give correct initial values (state and covariance) this should be equal
# to the true observation noise.
guessedObsrevationNoise = 10

# We are modeling an ideal process that has no noise. In reality this would be something inherent to the true
# dynamical process in the world.
# trueProcessNoise = 0.1
# Same applies here as for the guessed observation noise.
guessedProcessNoise = 0.01


# State - r, theta, dTheta
x = (np.array([1, 0, dTheta])*0)[:, np.newaxis]

# Covariance Matrix
p = np.identity(nStates)*1

# Transition matrix
f = np.array([[1, 0,  0],
              [0, 1, dt],
              [0, 0,  1]])

# Observation Matrix
h = np.array([[1, 0],
              [0, 1],
              [0, 0]]).T

# Process noise
q = np.identity(nStates)*guessedProcessNoise

# Observation noise
r = np.identity(nObervations)*guessedObsrevationNoise


def polarToEuclid(pol):
    """ return (x, y) from r, theta  """
    return pol[0, :]*np.array([np.cos(pol[1, :]), np.sin(pol[1, :])])


def truePath(t, r, dTheta):
    """ return true observation at time t """
    return np.array([r, t*dTheta])[:, np.newaxis]


def updateLines(lines, true, obs, est):
    """ Update plot artists' data """
    d = polarToEuclid(true[:, :i+1])
    lines[0].set_data(d[0, :], d[1, :])
    d = polarToEuclid(obs[:, :i+1])
    lines[1].set_data(d[0, :], d[1, :])
    d = polarToEuclid(est[:, :i+1])
    lines[2].set_data(d[0, :], d[1, :])

# Loop and logging variables
t = 0
nIterations = 10**3
trueData = np.empty((nObervations, nIterations))
observedData = np.empty((nObervations, nIterations))
estimatedData = np.empty((nStates, nIterations))

# Set some more variables related to plotting
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='equal')
scale = 1.5
ax.set_xlim(-scale*radius, scale*radius)
ax.set_ylim(-scale*radius, scale*radius)
lines = []
lines.append(ax.plot([], [], '.', label="True")[0])
lines.append(ax.plot([], [], '.', label="Observed")[0])
lines.append(ax.plot([], [], linewidth=2, label="Estimated")[0])
plt.legend(loc=4)
itePerUpdate = nIterations/300
iteSinceUpdate = 0

for i in range(nIterations):
    # Generate observation
    zTrue = truePath(t, radius, dTheta)
    z = zTrue + np.random.randn(nObervations)[:, np.newaxis]*trueObservationNoise

    # Prediction
    x = f.dot(x)
    pPre = f.dot(p.dot(f.T)) + q

    # Correction
    y = z - h.dot(x)
    s = h.dot(pPre.dot(h.T)) + r
    k = pPre.dot(h.T.dot(np.linalg.inv(s)))
    x += k.dot(y)
    p = (np.identity(nStates) - k.dot(h)).dot(pPre)

    # Store data
    estimatedData[:, i] = x[:, 0]
    trueData[:, i] = zTrue[:, 0]
    observedData[:, i] = z[:, 0]

    # Plot once in a while
    if iteSinceUpdate > itePerUpdate:
        iteSinceUpdate = 0
        updateLines(lines, trueData, observedData, estimatedData)
        # matplotlib stinks - so we (might) need to do this
        plt.pause(0.00001)

    t += dt
    iteSinceUpdate += 1

updateLines(lines, trueData, observedData, estimatedData)
plt.ioff()
plt.show()
# plt.savefig('./kalman.pdf', bbox_inches='tight')
