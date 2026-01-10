// JAVASCRIPT
// filter through array and return only countries without 'land'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
res = countries.filter(x => !x.includes('land'))
console.log(res)

// fitler through arr that contains only 7 characters
res_length = countries.filter(x => x.length == 7)
console.log(res_length)

// Use filter to filter out countries having exactly six characters.
sixChar = countries.filter(x => x.length !== 6)
console.log(sixChar)
