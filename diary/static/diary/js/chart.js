class Chart {
    constructor(container) {
        this.container = container;
    }

    render() {
        fetch("api/entry")
            .then(response => response.json())
            .then(data => {
                /* TODO - prepare data
                new frappe.Chart(this.container, {
                    data: data,
                    type: 'bar',
                    height: 300,
                });*/
            });
    }
}