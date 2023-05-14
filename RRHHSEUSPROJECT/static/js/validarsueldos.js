function validarSueldo(event) {
    var input = String.fromCharCode(event.which || event.keyCode); // Obtener el valor del carácter ingresado
    var pattern = /^\d*\.?\d*$/; // Definir una expresión regular para validar números con punto decimal
    if (!pattern.test(input)) { // Validar el carácter ingresado con la expresión regular
      event.preventDefault(); // Si no es un número con punto decimal, evitar que se ingrese en el campo
    }
  }