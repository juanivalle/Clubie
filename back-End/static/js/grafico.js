// Variables globales para los gráficos
let modelsChart = null;
let yearsChart = null;

// Función para obtener colores
function getDataColors() {
  return [
    'rgba(179, 102, 133, 0.8)',
    'rgba(102, 133, 179, 0.8)',
    'rgba(133, 179, 102, 0.8)',
    'rgba(179, 153, 102, 0.8)',
    'rgba(153, 102, 179, 0.8)',
    'rgba(102, 179, 153, 0.8)',
    'rgba(179, 102, 102, 0.8)',
    'rgba(102, 179, 179, 0.8)',
  ];
}

// Función para cargar el gráfico de razas con filtros
function cargarGraficoRazas(tipo = 'anual', anio = '', mes = '', desde = '', hasta = '') {
  // Construir URL con parámetros
  let url = '/prueba?tipo=' + tipo;
  if (anio) url += '&anio=' + anio;
  if (mes) url += '&mes=' + mes;
  if (desde) url += '&desde=' + desde;
  if (hasta) url += '&hasta=' + hasta;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      // Agrupar datos por raza
      const groupedData = data.reduce((result, venta) => {
        if (!result[venta.raza]) {
          result[venta.raza] = 0;
        }
        result[venta.raza] += venta.cantidad;
        return result;
      }, {});

      const uniqueLabels = Object.keys(groupedData);
      const values = Object.values(groupedData);

      // Destruir gráfico anterior si existe
      if (modelsChart) {
        modelsChart.destroy();
      }

      // Crear nuevo gráfico
      const ctx = document.getElementById('modelsChart').getContext('2d');
      modelsChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: uniqueLabels,
          datasets: [{
            label: 'Cantidad (gramos)',
            data: values,
            backgroundColor: getDataColors(),
            borderColor: getDataColors(),
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
    .catch(error => {
      console.error('Error cargando gráfico de razas:', error);
    });
}

// Función para cargar el gráfico de ventas por año/mes
function cargarGraficoAnual() {
  fetch('/prueba')
    .then(response => response.json())
    .then(data => {
      const months = Array(12).fill(0);
      const labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

      data.forEach(venta => {
        const date = new Date(venta.retiro);
        const month = date.getMonth();
        months[month] += venta.cantidad;
      });

      // Destruir gráfico anterior si existe
      if (yearsChart) {
        yearsChart.destroy();
      }

      const ctx = document.getElementById('yearsChart').getContext('2d');
      yearsChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Cantidad Retirada',
            data: months,
            backgroundColor: 'rgba(102, 133, 179, 0.4)',
            borderColor: 'rgba(102, 133, 179, 1)',
            borderWidth: 2,
            fill: true
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
    .catch(error => {
      console.error('Error cargando gráfico anual:', error);
    });
}

// Función para poblar el selector de años
function poblarSelectorAnios() {
  const selectAnio = document.getElementById('selectAnio');
  const currentYear = new Date().getFullYear();

  // Agregar últimos 5 años
  for (let i = 0; i < 5; i++) {
    const year = currentYear - i;
    const option = document.createElement('option');
    option.value = year;
    option.textContent = year;
    selectAnio.appendChild(option);
  }
}

// Función para manejar cambio de tipo de filtro
function manejarCambioTipoFiltro() {
  const tipoSeleccionado = document.querySelector('input[name="tipoFiltro"]:checked').value;
  const filtroAnio = document.getElementById('filtroAnio');
  const filtroMes = document.getElementById('filtroMes');
  const filtroRango = document.getElementById('filtroRango');

  // Ocultar todos primero
  filtroMes.classList.add('oculto');
  filtroRango.classList.add('oculto');

  if (tipoSeleccionado === 'anual') {
    filtroAnio.classList.remove('oculto');
  } else if (tipoSeleccionado === 'mes') {
    filtroAnio.classList.remove('oculto');
    filtroMes.classList.remove('oculto');
  } else if (tipoSeleccionado === 'rango') {
    filtroAnio.classList.add('oculto');
    filtroRango.classList.remove('oculto');
  }
}

// Función para aplicar filtro
function aplicarFiltro() {
  const tipoSeleccionado = document.querySelector('input[name="tipoFiltro"]:checked').value;
  const anio = document.getElementById('selectAnio').value;
  const mes = document.getElementById('selectMes').value;
  const desde = document.getElementById('fechaDesde').value;
  const hasta = document.getElementById('fechaHasta').value;

  if (tipoSeleccionado === 'rango') {
    if (!desde || !hasta) {
      alert('Por favor selecciona fecha de inicio y fin');
      return;
    }
    cargarGraficoRazas('rango', '', '', desde, hasta);
  } else if (tipoSeleccionado === 'mes') {
    if (!anio) {
      alert('Por favor selecciona un año');
      return;
    }
    cargarGraficoRazas('mes', anio, mes, '', '');
  } else {
    cargarGraficoRazas('anual', anio, '', '', '');
  }
}

// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function () {
  // Poblar selector de años
  poblarSelectorAnios();

  // Cargar gráficos iniciales
  cargarGraficoRazas();
  cargarGraficoAnual();

  // Event listeners para radio buttons
  const radioButtons = document.querySelectorAll('input[name="tipoFiltro"]');
  radioButtons.forEach(radio => {
    radio.addEventListener('change', manejarCambioTipoFiltro);
  });

  // Event listener para botón de filtrar
  const btnFiltrar = document.getElementById('btnFiltrar');
  if (btnFiltrar) {
    btnFiltrar.addEventListener('click', aplicarFiltro);
  }
});