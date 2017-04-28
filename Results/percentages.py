
import json

with open("results.json") as infile:
  data = infile.read()

print(data)

X = json.loads(data)

print(" | network | Percent hysteresis match | Percent resettable bistability match | time | ")
print(" | ------- | ------------------------ | ------------------------------------ | ---- | ")
for key in X:
  rpi = float(X[key]["reduced_param_indices"])
  h_match = float(X[key]["hysteresis_matches"])
  r_match = float(X[key]["resettable_matches"])
  h_time = float(X[key]["time_to_compute_hysteresis"])
  r_time = float(X[key]["time_to_compute_resettable"])
  print( key + "|" + str(100.0 *h_match / rpi) + "% | " + str(100.0 * r_match / rpi) + "% | " + str(h_time + r_time) + " | ")