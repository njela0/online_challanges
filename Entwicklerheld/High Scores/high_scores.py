"""
Scenario 1: Latest Score
The function latest(scores) just returns the latest score from the list of scores.
The latest score is the last value in the list.

Personal Best
The function personal_best(scores) returns the highest score achieved by the player.
The personal best score is the maximum value in the list of scores.

Personal Top Three
The function personal_top_three(scores) returns the top three highest scores from the list, sorted in descending order.
If there are fewer than three scores, return all the scores sorted in descending order.
"""

class HighScores:
    def __init__(self, scores):
        self.scores = scores.copy()

    def latest(self):
        return self.scores[-1]


    def personal_best(self):
        highest_score = 0

        for score in self.scores:
            if score > highest_score:
                highest_score = score

        return highest_score


    def personal_top_three(self):
        top_three = []

        if len(self.scores) <= 3:
            top_three = self.scores
            top_three.sort(reverse=True)

        else:
            for _ in range(3):
                highest_score = self.personal_best()
                top_three.append(highest_score)
                self.scores.remove(highest_score)

        return top_three


scores = [10, 100]

danis_scores = HighScores(scores)
print(danis_scores.latest())
print(danis_scores.personal_best())
print(danis_scores.personal_top_three())
print(scores)