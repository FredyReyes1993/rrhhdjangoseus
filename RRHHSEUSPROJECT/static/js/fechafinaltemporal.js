const opcionCampo = document.querySelector('#txttcont');
const fechaCampo = document.querySelector('#Fecha_Final');

opcionCampo.addEventListener('change', () => {
    if (opcionCampo.value === 'temporal') {
        fechaCampo.style.display = 'block';
    } else {
        fechaCampo.style.display = 'none';
    }
});