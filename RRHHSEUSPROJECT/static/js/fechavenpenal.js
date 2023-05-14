const fechapenalesInput = document.getElementById("fechapenales");
const fechavenpenalInput = document.getElementById("fechavenpenal");

function calcularFechaVencimiento() {
  const fecha = new Date(fechapenalesInput.value);
  const fechavenpenal = new Date(fecha.getFullYear(), fecha.getMonth() + 6, fecha.getDate());
  const fechavenpenalStr = `${fechavenpenal.getFullYear()}-${(fechavenpenal.getMonth() + 1).toString().padStart(2, '0')}-${fechavenpenal.getDate().toString().padStart(2, 0)}`;
  fechavenpenalInput.value = fechavenpenalStr;
}