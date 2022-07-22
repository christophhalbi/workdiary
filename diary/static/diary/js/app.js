document.addEventListener('DOMContentLoaded', (event) => {

    if (window.ChartLoader) {
        const chartLoader = new window.ChartLoader();
        chartLoader.render();
    }
});