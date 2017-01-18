var sander = require('sander');

//function that reads the directories and subsequent log files. adds to count it regex matches in file. This was new territory as I've used logger npm module as nodejs doesn't make server log files. I feel like I know much more on server logs, but have quite a ways to go. I'm also concerned on this promise chain. 
//I brought in the sander npm module (fs wrapper) to read the directores/files though fs module in Node would have worked as well.
function parseLogs(dirs) {
	var dailyCount = 0;
	dirs.forEach(dir => {
		sander.readdir(dir)
		.then(files => {
			files.forEach(file => {
				sander.readFile(file)
					.then(contents => {
						var regex = /myfakesite\.com\:80\/newapi/;
						if(contents.match(regex)) dailyCount++;
					})
			})
		})
	})
}