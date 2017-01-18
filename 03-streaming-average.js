//creates a continuous stream of averages until threshold is reached. still rather chunky, but kept it to a single loop
//I admit I have limited knowledge on best ways to allocate memory as my primary experience is in JavaScript, but I attempted use objects as they are stored by reference 
function stream(lower, upper, threshold) {
	var result = {average: 0, count: 2}
	var averages = {};
  averages.avgGoal = Number((lower.lower + upper.upper)/2);
  averages.random1 = Math.floor(Math.random() * (upper.upper - lower.lower + 1)) + lower.lower;
  averages.random2 = Math.floor(Math.random() * (upper.upper - lower.lower + 1)) + lower.lower;
  averages.currentAvg = Number((averages.random2 + averages.random1)/2);
  result.average = averages.currentAvg;
  while(averages.avgGoal - threshold.threshold > averages.currentAvg || averages.currentAvg > averages.avgGoal + threshold.threshold) {
  	result.count++;
  	averages.random = Math.floor(Math.random() * (upper.upper - lower.lower + 1)) + lower.lower;
  	averages.currentAvg = (averages.currentAvg + averages.random)/result.count;
  	result.average = averages.currentAvg;
  }
  console.log(result);
  return result;
}

stream({lower: 0}, {upper: 10}, {threshold: 2});