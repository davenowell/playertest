var fs = require('fs')
var data = require('./lib.json')

fs.writeFile('lib.json', JSON.stringify(data), (err) =>{
    console.log('write finished', err)
})