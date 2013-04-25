# Computes the dot product of two vectors
def dot(VectorA, VectorB):
	sum = 0
	length = min(len(VectorA), len(VectorB))
	for i in range(0, length):
		sum += VectorA[i]*VectorB[i]
	return sum

# Computes the norm of a vector
def norm(Vector, power):
	radicand = 0
	for element in Vector:
		radicand += pow(element, power)
	return pow(float(radicand), 1/float(power))

# Gets the ranking of two users using vector space model search
def getRanking(UserA, UserB):
	return dot(UserA, UserB)/(norm(UserA, 2)*norm(UserB, 2))


# Create matrix of Users x Games
# Each row should be a User
# Each column should be a Game
	# For testing
UserGames = [
		[1, 1, 0, 1],
		[0, 0, 1, 1],
		[1, 0, 0, 0],
		[0, 1, 1, 0],
		[1, 0, 1, 0]
	]

for currentUser in UserGames:
	rankings = {}
	for i, otherUser in enumerate(UserGames):
		rankings[i] = getRanking(currentUser, otherUser)
	print rankings
