// TERNARIOS EN JS
var security_level= 3;
var access_level= 4;

var access;

if (access_level > security_level) {
    acess= 'adelante';}
else  {
    access= 'no puedes pasar';}

//es lo mismo que 
var access= access_level > security_level ? 'adelante' :'no puedes pasar';

// otro ejemplo
var persona = {
    'detalles': {
        'nombre_completo': {
            'nombre': 'Alvaro',
            'apellido': 'Sanchez'
        }
    }
}


// 3 formas de llamar a lo mismo, forma clasica (objetos)
persona.detalles.nombre_completo.nombre
// forma a prueba de fallos
persona && persona.detalles && persona.detalles.nombre_completo && persona.detalles.nombre_completo.nombre
//forma mas moderna
persona?.detalles?.nombre_completo?.nombre

var persona2=persona //esto hace un enlace, no hace una copia



