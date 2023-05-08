// console.log('--------------------');
// for (var year = 2014; year <= 2050; year++) {
//     var d = new Date(year, 0, 1);
//     console.log(d);
//     console.log(d.getDay());

//     // if (d.getDay() === 0)
//     // console.log("1st January is being a Sunday  " + year);
// }
// console.log('--------------------');

// function isLeapYear(year) {
//     if (year % 4 !== 0) {
//         return false;  // not divisible by 4
//     } else if (year % 100 !== 0) {
//         return true;   // divisible by 4 but not by 100
//     } else if (year % 400 !== 0) {
//         return false;  // divisible by 100 but not by 400
//     } else {
//         return true;   // divisible by 400
//     }
// }
// for (var year = 2014; year <= 2050; year++) {
//     if (isLeapYear(year)) {
//         console.log(year);
//     }
// }


// // Example usage
// console.log(isLeapYear(2000));  // true
// console.log(isLeapYear(1900));  // false
// console.log(isLeapYear(2024));  // true
// console.log(isLeapYear(2022));  // false


for (let year = 2014; year <= 2025; year++) {
    if (year % 4 !== 0) {
        console.log(`${year} is not a leap year`);
    } else if (year % 100 !== 0) {
        console.log(`${year} is a leap year`);
    } else if (year % 400 !== 0) {
        console.log(`${year} is not a leap year`);
    } else {
        console.log(`${year} is a leap year`);
    }
}
