// definir las opciones disponibles para cada departamento
const opcionesPuestos = {
    Administracion : ['Gerente General','Representante Legal','Asistente Gerencia',
                    'Gerente Operaciones','Asistente Operaciones','Encargado Sede',
                    'Coordinador','Armero','Asistente Armeria',
                    'Gerente Puesto Fijos','Asistente Puestos Fijos',
                    'Gerente Administrativo','Asistente Administrativo',
                    'Contador General','Auxiliar Contable',
                    'Gerente Vehiculos','Mecanico','Asistente Mecanico',
                    'Gerente Recursos Humanos','Asistente Recursos Humanos','Verificador','Reclutador','Instructor',
                    'Conserje'],

    Operativo: ['Guardia de Ruta Guatemala','Guardia de Ruta Puerto Barrios',
                    'Guardia de Ruta Tecun Uman','Guardia de Ruta Pedro de Alvarado',
                    'Guardia Puesto Fijo Guatemala','Guardia Puesto Fijo Puerto Barrios',
                    'Guardia Puesto Fijo Tecun Uman','Guardia Puesto Fijo Pedro Alvarado'],

    Supervisores: ['Supervisor Guatemala','Supervisor Puerto Barrios',
                    'Supervisor Tecun Uman','Supervisor Pedro de Alvarado',
                    'Supervisor Puestos Fijos'],

    Otros_Servicios: ['Domestica','Conserje',
                'Piloto Ejecutivo','Jardinero',
                'Guardaespaldas'],
  };


  // obtener la referencia a las listas desplegables
  const tipoexp = document.getElementById('id_tipo_exp');
  const puestoexp = document.getElementById('id_puesto_exp');

  // escuchar los cambios en la lista de departamento
  tipoexp.addEventListener('change', () => {
    // borrar todas las opciones anteriores en la lista de municipios
    puestoexp.innerHTML = '';

    // obtener las opciones disponibles para el departamento seleccionado
    const opciones = opcionesPuestos[tipoexp.value];

    // agregar una opción para cada municipio disponible
    opciones.forEach((opcion) => {
      const option = document.createElement('option');
      option.value = opcion;
      option.text = opcion;
      puestoexp.add(option);
    });
  });