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


# Replace with code to select from user_game
# Create 2d matrix where rows are users and columns are games
# We may need additional dictionaries to map row indexes to user_ids
# and column indexes to game_ids
UserGames = [
		[1, 1, 0, 1],
		[0, 0, 1, 1],
		[1, 0, 0, 0],
		[0, 1, 1, 0],
		[1, 0, 1, 0]
	]

for i, currentUser in enumerate(UserGames):
	rankings = {}
	for j, otherUser in enumerate(UserGames):
		rankings[j] = getRanking(currentUser, otherUser)
	rankings = list(reversed(sorted(rankings.items(), key=lambda x: x[1])))
	
	recommendations = []
	for ranking in rankings:
		otherUser = UserGames[ranking[0]]
		for i in range(0, len(otherUser)):
			if (otherUser[i] and not currentUser[i] and i not in recommendations):
				recommendations.append(i)
	# Replace this with code to insert into database
	print recommendations
