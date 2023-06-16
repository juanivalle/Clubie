const printCharts = () => {
    renderModelsChart()
}

const renderModelsChart = () => {
    const data = {
        labels: ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'],
        datasets: [{
            data: [10,20,30, 40, 50,60,70,80,90,100],
            borderColor: getDataColors(),
            borderWidth: 1,
            backgroundColor: getDataColors(20)
        }]
    }
    const options = {
        plugins: {
            
        }
    }
    
    new Chart ('modelsChart', {type: 'bar', data, options })
}


printCharts()