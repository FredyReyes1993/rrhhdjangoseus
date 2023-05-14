// definir las opciones disponibles para cada Nivel de estudio
const opcionesEstudios = {
    primaria : ['Sexto Primaria'],

    basicos : ['Primero Básico','Segundo Básico','Tercero Básico'],

    diversificado : ['Cuarto diversificado','Quinto diversificado', 'Sexto diversificado'],

    universidad : ['Primer año','Segundo año', 'Tercer año','Cuarto año','Quinto año','Sexto año','Graduado'],

    postgrado : ['Estudiando','Graduado'],

    maestria : ['Primer año','Segundo año','Graduado'],

    doctorado : ['Primer año','Segundo año', 'Tercer año','Cuarto año','Quinto año','Sexto año','Graduado']

};

// obtener la referencia a las listas desplegables
const niveleducativo = document.getElementById('id_niveleducativo');
const gradoacademico = document.getElementById('id_gradoacademico');

// escuchar los cambios en la lista de departamento
niveleducativo.addEventListener('change', () => {
  // borrar todas las opciones anteriores en la lista de municipios
  gradoacademico.innerHTML = '';

  // obtener las opciones disponibles para el departamento seleccionado
  const opciones = opcionesEstudios[niveleducativo.value];

  // agregar una opción para cada municipio disponible
  opciones.forEach((opcion) => {
    const option = document.createElement('option');
    option.value = opcion;
    option.text = opcion;
    gradoacademico.add(option);
  });
});