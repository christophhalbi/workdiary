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
                            name: "productivity", type: "line",
                            values: data.map(item => item['productivity_rating'])
                        },
                        {
                            name: "happiness", type: "line",
                            values: data.map(item => item['happiness_rating'])
                        }
                    ]
                };

                let chart = new frappe.Chart('#chart-container', {
                    data: chartData,
                    type: 'line',
                    height: 300,
                    title: "Entries",
                });
            });
    }
}