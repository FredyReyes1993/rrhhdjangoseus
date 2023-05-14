function validarNumero(event) {
	var tecla = event.which || event.keyCode; // Obtener el código de la tecla
	if (tecla < 48 || tecla > 57) { // Permitir solo números del 0 al 9
		event.preventDefault();
	}
}