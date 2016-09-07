var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
        var line_array = line.split(',');
        var n = parseInt(line_array[0]);
        var m = parseInt(line_array[1]);
        console.log(n-((Math.floor(n/m)*m)));
    }
});