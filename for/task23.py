school = [{'school_class': '2a', 'scores': [3, 4, 4, 5, 2]},
          {'school_class': '2b', 'scores': [3, 4, 4, 5, 2]},
          {'school_class': '3a', 'scores': [2, 5, 3, 4, 3]},
          {'school_class': '4a', 'scores': [5, 3, 4, 4, 5]},
          {'school_class': '5a', 'scores': [3, 2, 2, 3, 2]}]
scores_sum = 0
for score in school:
    print(f"Average of marks class {score['school_class']} is {sum(score['scores'])/len(score['scores'])}")
    scores_sum += sum(score['scores'])/len(score['scores'])
    print(scores_sum)
print(f"Average school marks is {scores_sum/len(school)}")
