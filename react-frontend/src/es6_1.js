console.log(username);

var username = "Prograsshopper"

console.log(username);

// object destructuring
const tommy = {
    name: "Tom",
    age: 10,
    region: "Seoul"
};

const print_person1 = (person) => {
    console.log(person.name);
};
const print_person2 = ({ name }) => {
    console.log(name);
};
print_person1(tommy);
print_person2(tommy);

const person = {
    name: 'Tom',
    age: 10,
    region: {
    country: '서울',
    postcode: '06222',
    }
};
const { name, region: { postcode }} = person;
console.log(name, postcode);


// Arrow function
// this와 arguments를 바인딩하지 않는다
var tom = {
    name: "Tom",
    print1: function() {
        console.log(`[print1-1] name : ${this.name}`);
        (function() {
        console.log(`[print1-2] name : ${this.name}`);
        })();
    },
    print2: function() {
        console.log(`[print2-1] name : ${this.name}`);
        var me = this;
        (function() {
        console.log(`[print2-2] name : ${me.name}`);
        })();
    },
    print3: function() {
        console.log(`[print3-1] name : ${this.name}`);
        (() => {
        console.log(`[print3-2] name : ${this.name}`);
        })();
    }
};

// print2와 print3은 같은 결과를 낳는다. AF에선 this가 바뀌지않기 때문
tom.print1();
tom.print2();
tom.print3();
