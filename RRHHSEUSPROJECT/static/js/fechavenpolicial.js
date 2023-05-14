const fechapolicialesInput = document.getElementById("fechapoliciales");
const fechavenpoliInput = document.getElementById("fechavenpoli");

function calcularFechaVen() {
  const fecha = new Date(fechapolicialesInput.value);
  const fechavenpoli = new Date(fecha.getFullYear(), fecha.getMonth() + 6, fecha.getDate());
  const fechavenpoliStr = `${fechavenpoli.getFullYear()}-${(fechavenpoli.getMonth() + 1).toString().padStart(2, '0')}-${fechavenpoli.getDate().toString().padStart(2, 0)}`;
  fechavenpoliInput.value = fechavenpoliStr;
}