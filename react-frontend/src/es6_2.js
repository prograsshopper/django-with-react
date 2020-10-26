// 고차함수

// function base_10(fn) {
//     function wrap(x, y) {
//         return fn(x, y) + 10;
//     }
//     return wrap;

    // const i = 10;
    // const fn = () => {};
    // function fn2() {

    // }
    // return fn;
// }
// function mysum(a, b) {
//     return a + b;
// }

const base_10 = (fn) => (x, y) => (fn(x, y) + 10);
const mysum = (a, b) => a + b;

const return_fn = base_10(mysum);
console.log(return_fn(1, 2));
