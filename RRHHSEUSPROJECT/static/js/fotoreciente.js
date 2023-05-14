
// Función para mostrar la imagen después de cargarla
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#fotorec').attr('src', e.target.result);
            $('#fotorec').show(); // Mostramos la imagen
        }
        reader.readAsDataURL(input.files[0]);
    } 
}
