import numpy as np
import teapot_factory
import pprint

def index_array(max, idx):
    return [1 if i in idx else 0 for i in range(max)]

# prepare data matrix
N = len(teapot_factory.worker_names)
y = np.array([s["teapots"] for s in teapot_factory.shifts])
W = np.matrix(np.array([index_array(N, s["workers"]) for s in teapot_factory.shifts]))

# solve w: Wx = y
# W.t * W x = W.t * y
# x = (W.t * W)^-1 * W.t * y

A = (W.T.dot(W) + 1e-3 * np.diag(np.ones(N)))
x = A.I.dot(W.T.dot(y).T)

pprint.pprint(dict((name, x[i][(0,0)]) for (i, name) in teapot_factory.worker_names.items()))
