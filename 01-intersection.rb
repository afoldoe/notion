require "set"
#unsure if this is brittle/not recommended as best practice in ruby, but it does return intersecting values in two arrays.
#I chose this solution as it brings the Big-O time complexity from O(N^2) to O(N) by getting rid of the nested loop
def intersect(xs, ys)
  result = []
  result = xs & ys
  puts result
end

