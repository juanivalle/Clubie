fetch('/prueba')
  .then(response => response.json())
  .then(data => {
    // Preparar los datos para el gráfico
    const labels = data.map(venta => venta.raza);
    const values = data.map(venta => venta.cantidad);

    // Configurar y generar el gráfico utilizando Chart.js
    const ctx = document.getElementById('modelsChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'raza',
          data: values,
          backgroundColor: getDataColors(),
          borderColor: getDataColors(),
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  
  .catch(error => {
    console.error('Error:', error);
  });

  fetch('/prueba')
  .then(response => response.json())
  .then(data => {
    // Preparar los datos para el gráfico
    const labels = data.map(venta => venta.raza);
    const values = data.map(venta => venta.cantidad);
    enableEventHandlers(labels);

    // Configurar y generar el gráfico utilizando Chart.js
    const ctx = document.getElementById('featuresChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'raza',
          data: values,
          backgroundColor: getDataColors(),
          borderColor: getDataColors(),
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  
  .catch(error => {
    console.error('Error:', error);
  });

  fetch('/prueba')
  .then(response => response.json())
  .then(data => {
    // Preparar los datos para el gráfico
    const labels = data.map(venta => venta.retiro);
    const values = data.map(venta => venta.cantidad);
    
    // Configurar y generar el gráfico utilizando Chart.js
    const month = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Sepiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    const ctx = document.getElementById('yearsChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: month,
        datasets: [{
          label: 'retiro',
          data: values,
          backgroundColor: getDataColors(),
          borderColor: getDataColors(),
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })
  
  .catch(error => {
    console.error('Error:', error);
  });

