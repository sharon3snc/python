var n=10

while (n>=0) {
    if (n===7) {
        n-=1
        continue
    }
    console.log(n);
    n-=1;
}


for (var i=0; i>10; i++){
    console.log(i);
}

var temperaturas_list = [-2.1, -2.3, -1.3, 3.4, 6.9, 6.3, 4.1]

for (temp in temperaturas_list) {
    console.log(temperaturas_list[temp]);
}

//si fuese un diccionario en lugar de array
for (key in temperaturas_dict) {
    console.log(key)
}


//.map
var temp_fahr = temperaturas_list.map(temperatura => temperatura * 1.8 + 32)
// me devuelve una nueva lista

//.forEach
var suma=0
temperaturas_list.forEach(temperatura => { suma+= temperatura})
// no retorna nada, sino que ejecuta n veces

//.filter
temperaturas_list.filter(temperatura => temperatura >= 0)
//devuelve una nueva lista

//filter y map se pueden encadenar
temperaturas_list.filter(temperatura => temperatura >= 0).map(temperatura => temperatura * 1.8 + 32)

//forEach debe ir al final

