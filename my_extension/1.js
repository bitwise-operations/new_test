var fs = require('fs'),
    ini = require('ini');
    
var config = ini.parse(fs.readFileSync('./config.ini', 'utf8'));
console.dir(Object.keys(config));



// document.getElementById('order_client_attributes_surname').value = "Демо"

// document.forms.new_order


// var i;

// for (i = 0; i < ; i++) {
//   alert( i );
// }





// x.querySelector("#clientForm li.name input")