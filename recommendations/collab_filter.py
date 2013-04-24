from numpy import array
from numpy import dot
from numpy import linalg
from numpy import matrix

# test matrix
documents = matrix( [
	[0, 1, 1],
	[0, 0, 1],
	[1, 1, 1],
	[1, 0, 1]])

query = array([1, 0, 0])

output = []

for column in documents:
	queryDotColumnT = dot(query, column.T)
	query2Norm = linalg.norm(query)
	columnT2Norm = linalg.norm(column.T)
	rank = queryDotColumnT/(query2Norm*columnT2Norm)
	output.append(rank.tolist()[0][0])

print sorted(output)
