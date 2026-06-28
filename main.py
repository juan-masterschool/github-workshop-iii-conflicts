import statistics

def average_calculation(elements):
  average = statistics.mean(elements)
  return average
  

def main():
  goals_scored = [3, 2, 4, 0, 0, 1, 2]
  average_goals = average_calculation(goals_scored)
  print(f"The goals' average scored was {average_goals}!")

if __name__ == "__main__":
  main()
