def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for rIdx in range(len(results)):
        # determin which team is the winner
        if results[rIdx] == 0:
            winnerTeam = competitions[rIdx][1]
        else:
            winnerTeam = competitions[rIdx][0]

        # update the scores
        if winnerTeam not in scores:
            scores[winnerTeam] = 0
        scores[winnerTeam] += 1

        # determine which team is the current best team
        if (scores[winnerTeam] > scores[currentBestTeam]):
            currentBestTeam = winnerTeam
            
    return currentBestTeam
