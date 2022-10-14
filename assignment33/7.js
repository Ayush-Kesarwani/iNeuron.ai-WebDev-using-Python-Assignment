// Create a human readable time format using the Date time object
// a. YYYY-MM-DD HH:mm
// b. DD-MM-YYYY HH:mm
// c. DD/MM/YYYY HH:mm

var d = new Date();
console.log(d);
var date = d.getDate();
var month = d.getMonth();
var year = d.getFullYear();
var hour=d.getHours();
var minute=d.getMinutes();
console.log(year + "-" + (month+1) + "-" + date + " " + hour + ":" + minute);
console.log(date + "-" + (month+1) + "-" + year + " " + hour + ":" + minute);
console.log(date + "/" + (month+1) + "/" + year + " " + hour + ":" + minute);