fetch('/prueba')
  .then(response => response.json())
  .then(data => {
    // Preparar los datos para el gráfico
    const groupedData = data.reduce((result, venta) => {
      if (!result[venta.raza]) {
        result[venta.raza] = 0;
      }
      result[venta.raza] += venta.cantidad;
      return result;
    }, {});

    // Preparar los datos para el gráfico
    const uniqueLabels = Object.keys(groupedData);
    const values = Object.values(groupedData);

    // Configurar y generar el gráfico utilizando Chart.js
    const ctx = document.getElementById('modelsChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: uniqueLabels,
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
    const months = Array(12).fill(0);
    const labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    
    // Agrupar la cantidad retirada por mes
    data.forEach(venta => {
      const date = new Date(venta.retiro);
      const month = date.getMonth();
      const cantidad = venta.cantidad;
      months[month] += cantidad;
    });

    // Configurar y generar el gráfico utilizando Chart.js
    const ctx = document.getElementById('yearsChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Cantidad Retirada',
          data: months,
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