export class ChartLoader {
    constructor() {
    }

    render() {
        fetch("api/entry")
            .then(response => response.json())
            .then(data => {

                const chartData = {
                    labels: data.map(item => item['day']),
                    datasets: [
                        {
                            name: "productivity",
                            chartType: "line",
                            values: data.map(item => item['productivity_rating'])
                        },
                        {
                            name: "happiness",
                            chartType: "line",
                            values: data.map(item => item['happiness_rating'])
                        },
                        {
                            name: "incidents",
                            chartType: "bar",
                            values: data.map(item => item['incidents'].length)
                        }
                    ]
                };

                let chart = new frappe.Chart('#chart-container', {
                    data: chartData,
                    type: 'axis-mixed',
                    height: 300,
                    colors: ['blue', 'green', 'red']
                });
            });
    }
}
