def fds_statistics(marks):
  """
  This function computes various statistics for a list of "Fundamental of Data Structures" marks.

  Args:
    marks: A list of integers representing marks scored by N students.

  Returns:
    A dictionary containing the following statistics:
      - average_score: The average score of the class.
      - highest_score: The highest score in the class.
      - lowest_score: The lowest score in the class.
      - absent_count: The number of students who were absent for the test.
      - most_frequent_mark: The mark with the highest frequency.

  """

  # Check for empty list
  if not marks:
    raise ValueError("No marks provided!")

  # Calculate average score
  average_score = sum(marks) / len(marks)

  # Find highest and lowest scores
  highest_score = max(marks)
  lowest_score = min(marks)

  # Count absent students (marks -1 represent absent)
  absent_count = marks.count(-1)

  # Create a dictionary to store frequency of each mark
  mark_frequency = {}
  for mark in marks:
    if mark in mark_frequency:
      mark_frequency[mark] += 1
    else:
      mark_frequency[mark] = 1

  # Find the mark with the highest frequency
  most_frequent_mark = max(mark_frequency, key=mark_frequency.get)

  # Return the statistics as a dictionary
  return {
      "average_score": average_score,
      "highest_score": highest_score,
      "lowest_score": lowest_score,
      "absent_count": absent_count,
      "most_frequent_mark": most_frequent_mark,
  }

# Example usage
marks = [75, 88, 92, 65, 80, -1, 95, 78, 85, 88]

statistics = fds_statistics(marks)

print("Average score:", statistics["average_score"])
print("Highest score:", statistics["highest_score"])
print("Lowest score:", statistics["lowest_score"])
print("Number of absent students:", statistics["absent_count"])
print("Mark with highest frequency:", statistics["most_frequent_mark"])
