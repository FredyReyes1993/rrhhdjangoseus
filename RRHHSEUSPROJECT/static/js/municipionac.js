// definir las opciones disponibles para cada departamento
const opcionesDepartonac = {
    alta_verapaz : ['Cahabón','Chahal',
                    'Chisec','Cobán',
                    'Fray Bartolomé de las Casas','Lanquín',
                    'Panzós','Raxruhá',
                    'San Cristóbal Verapaz','San Juan Chamelco',
                    'San Pedro Carchá','Santa Catalina la Tinta',
                    'Santa Cruz Verapaz','Senahú',
                    'Tactic','Tamahú',
                    'Tucurú'],

    baja_verapaz: ['Cubulco','El Chol',
                    'Granados','Purulhá',
                    'Rabinal','Salamá',
                    'San Jerónimo','San Miguel Chicaj'],

    chimaltenango: ['Acatenango','Chimaltenango',
                    'Comalapa','El Tejar',
                    'Parramos','Patzicía',
                    'Patzún','Pochuta',
                    'San Andrés Itzapa','San José Poaquil',
                    'San Martín Jilotepeque','Santa Apolonia',
                    'Santa Cruz Balanyá','Tecpán Guatemala',
                    'Yepocapa','Zaragoza'],

    chiquimula: ['Camotán','Chiquimula',
                'Concepción Las Minas','Esquipulas',
                'Ipala','Jocotán',
                'Olopa','Quetzaltepeque',
                'San Jacinto','San José La Arada',
                'San Juan Ermita'],

    el_progreso: ['El Jícaro','Guastatoya',
                    'Morazán','San Agustín Acasaguastlán',
                    'San Antonio la Paz','San Cristóbal Acasaguastlán',
                    'Sanarate','Sansare'],

    escuintla: ['Escuintla','Guanagazapa',
                'Iztapa','La Democracia',
                'La Gomera','Masagua',
                'Nueva Concepción','Palín',
                'San José','San Vicente Pacaya',
                'Santa Lucía Cotzumalguapa','Siquinalá',
                'Tiquisate'],

    guatemala: ['Amatitlán','Chinautla',
                'Chuarrancho','Fraijanes',
                'Guatemala','Mixco',
                'Palencia','Petapa',
                'San José del Golfo','San José Pinula',
                'San Juan Sacatepéquez','San Pedro Ayampuc',
                'San Pedro Sacatepéquez','San Raymundo',
                'Santa Catarina Pinula','Villa Canales',
                'Villa Nueva'],

    huehuetenango: ['Aguacatán','Barillas',
                    'Chiantla','Colotenango',
                    'Concepción Huista','Cuilco',
                    'Huehuetenango','Ixtahuacán',
                    'Jacaltenango','La Democracia',
                    'La Libertad','Malacatancito',
                    'Nentón','San Antonio Huista',
                    'San Gaspar Ixchil','San Juan Atitán',
                    'San Juan Ixcoy','San Mateo Ixtatán',
                    'San Miguel Acatán','San Pedro Necta',
                    'San Rafael la Independencia','San Rafael Petzal',
                    'San Sebastián Coatán','San Sebastián Huehuetenango',
                    'Santa Ana Huista','Santa Bárbara',
                    'Santa Eulalia','Santiago Chimaltenango',
                    'Soloma','Tectitán',
                    'Todos Santos Cuchumatán','Unión Cantinil'],
    
    izabal: ['El Estor','Livingston',
                'Los Amates','Morales',
                'Puerto Barrios'],

    jalapa: ['Jalapa','Mataquescuintla',
                'Monjas','San Carlos Alzatate',
                'San Luis Jilotepeque','San Manuel Chaparrón',
                'San Pedro Pinula'],
    
    jutiapa: ['Agua Blanca','Asunción Mita',
                'Atescatempa','Comapa',
                'Conguaco','El Adelanto',
                'El Progreso','Jalpatagua',
                'Jerez','Jutiapa',
                'Moyuta','Pasaco',
                'Quesada','San José Acatempa',
                'Santa Catarina Mita','Yupiltepeque',
                'Zapotitlán'],

    peten: ['Dolores','El Chal',
            'Flores','La Libertad',
            'Las Cruces','Melchor de Mencos',
            'Poptún','San Andrés',
            'San Benito','San Francisco',
            'San José','San Luis',
            'Santa Ana','Sayaxché'],

    quetzaltenango:['Almolonga','Cabricán',
                    'Cajolá','Cantel',
                    'Coatepeque','Colomba',
                    'Concepción Chiquirichapa','El Palmar',
                    'Flores Costa Cuca','Génova',
                    'Huitán','La Esperanza',
                    'Olintepeque','Ostuncalco',
                    'Palestina de los Altos','Salcajá',
                    'San Carlos Sija','San Francisco la Unión',
                    'San Martín Sacatepéquez','San Mateo',
                    'San Miguel Siguilá','Sibilia',
                    'Zunil'],

    quiche: ['Canillá','Chajul',
            'Chicamán','Chiché',
            'Chichicastenango','Chinique',
            'Cunén','Ixcán',
            'Joyabaj','Nebaj',
            'Pachalum','Patzité',
            'Sacapulas','San Andrés Sajcabajá',
            'San Antonio Ilotenango','San Bartolomé Jocotenango',
            'San Juan Cotzal','San Pedro Jocopilas',
            'Santa Cruz del Quiché','Uspantán',
            'Zacualpa'],

    retalhuleu: ['Champerico','El Asintal',
                    'Nuevo San Carlos','Retalhuleu',
                    'San Andrés Villa Seca','San Felipe',
                    'San Martín Zapotitlán','San Sebastián',
                    'Santa Cruz Muluá'],

    sacatepequez:['Alotenango','Antigua Guatemala',
                    'Ciudad Vieja','Jocotenango',
                    'Magdalena Milpas Altas','Pastores',
                    'San Antonio Aguas Calientes','San Bartolomé Milpas Altas',
                    'San Lucas Sacatepéquez','San Miguel Dueñas',
                    'Santa Catarina Barahona','Santa Lucía Milpas Altas',
                    'Santa María de Jesús','Santiago Sacatepéquez',
                    'Santo Domingo Xenacoj','Sumpango'],
    
    san_marcos: ['Ayutla','Catarina',
                    'Comitancillo','Concepción Tutuapa',
                    'El Quetzal','El Rodeo',
                    'El Tumbador','Esquipulas Palo Gordo',
                    'Ixchiguán','La Blanca',
                    'La Reforma','Malacatán',
                    'Nuevo Progreso','Ocós',
                    'Pajapita','Río Blanco',
                    'San Antonio Sacatepéquez','San Cristóbal Cucho',
                    'San José Ojetenán','San Lorenzo',
                    'San Marcos','San Miguel Ixtahuacán',
                    'San Pablo','San Pedro Sacatepéquez',
                    'San Rafael Pié de la Cuesta','Sibinal',
                    'Sipacapa','Tacaná',
                    'Tajumulco','Tejutla'],

    santa_rosa: ['Barberena','Casillas',
                    'Chiquimulilla','Cuilapa',
                    'Guazacapán','Nueva Santa Rosa',
                    'Oratorio','Pueblo Nuevo Viñas',
                    'San Juan Tecuaco','San Rafael las Flores',
                    'Santa Cruz Naranjo','Santa María Ixhuatán',
                    'Santa Rosa de Lima','Taxisco'],
    
    solola: ['Concepción','Nahualá',
                'Panajachel','San Andrés Semetabaj',
                'San Antonio Palopó','San José Chacayá',
                'San Juan la Laguna','San Lucas Tolimán',
                'San Marcos la Laguna','San Pablo la Laguna',
                'San Pedro la Laguna','Santa Catarina Ixtahuacán',
                'Santa Catarina Palopó','Santa Clara la Laguna',
                'Santa Cruz la Laguna','Santa Lucía Utatlán',
                'Santa María Visitación','Santiago Atitlán',
                'Sololá'],

    suchitepequez: ['Chicacao','Cuyotenango',
                    'Mazatenango','Patulul',
                    'Pueblo Nuevo','Río Bravo',
                    'Samayac','San Antonio Suchitepéquez',
                    'San Bernardino','San Francisco Zapotitlán',
                    'San Gabriel','San José el Idolo',
                    'San José La Máquina','San Juan Bautista',
                    'San Lorenzo','San Miguel Panán',
                    'San Pablo Jocopilas','Santa Bárbara',
                    'Santo Domingo Suchitepéquez','Santo Tomás la Unión',
                    'Zunilito'],

    totonicapan: ['Momostenango','San Andrés Xecul',
                    'San Bartolo','San Cristóbal Totonicapán',
                    'San Francisco el Alto','Santa Lucía la Reforma',
                    'Santa María Chiquimula','Totonicapán'],

    zacapa: ['Cabañas','Estanzuela',
                'Gualán','Huité',
                'La Unión','Río Hondo',
                'San Diego','San Jorge',
                'Teculután','Usumatlán',
                'Zacapa']

  };


  // obtener la referencia a las listas desplegables
  const deptonac = document.getElementById('id_depto_nac');
  const muninac = document.getElementById('id_muni_nac');

  // escuchar los cambios en la lista de departamento
  deptonac.addEventListener('change', () => {
    // borrar todas las opciones anteriores en la lista de municipios
    muninac.innerHTML = '';

    // obtener las opciones disponibles para el departamento seleccionado
    const opciones = opcionesDepartonac[deptonac.value];

    // agregar una opción para cada municipio disponible
    opciones.forEach((opcion) => {
      const option = document.createElement('option');
      option.value = opcion;
      option.text = opcion;
      muninac.add(option);
    });
  });