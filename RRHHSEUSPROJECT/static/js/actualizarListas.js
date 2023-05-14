function actualizarListas() {
    // Obtener las listas desplegables
    var lista1 = document.getElementById("id_Lista1");
    var lista2 = document.getElementById("id_Lista2");
    var lista3 = document.getElementById("id_Lista3");

    // Obtener el valor seleccionado en cada lista desplegable
    var seleccion1 = lista1.value;
    var seleccion2 = lista2.value;
    var seleccion3 = lista3.value;

    // Habilitar todas las opciones en todas las listas desplegables
    for (var i = 0; i < lista1.options.length; i++) {
      lista1.options[i].disabled = false;
      lista2.options[i].disabled = false;
      lista3.options[i].disabled = false;
    }

    // Deshabilitar la opción seleccionada en las otras listas desplegables
    if (seleccion1 !== "") {
      lista2.querySelector('option[value="' + seleccion1 + '"]').disabled = true;
      lista3.querySelector('option[value="' + seleccion1 + '"]').disabled = true;
    }
    if (seleccion2 !== "") {
      lista1.querySelector('option[value="' + seleccion2 + '"]').disabled = true;
      lista3.querySelector('option[value="' + seleccion2 + '"]').disabled = true;
    }
    if (seleccion3 !== "") {
      lista1.querySelector('option[value="' + seleccion3 + '"]').disabled = true;
      lista2.querySelector('option[value="' + seleccion3 + '"]').disabled = true;
    }
  }