var fs = require('fs')
var data = require('./lib.json')

console.log(data.name)

fs.readFile('./lib.json', 'utf-8', (err,data) => {
    var data = JSON.parse(data)
    console.log(data.name)
})