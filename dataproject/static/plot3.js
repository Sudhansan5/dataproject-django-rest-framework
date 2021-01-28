
    const myForm= document.getElementById('plot');
    myForm.addEventListener('submit', function(e){
        e.preventDefault();
        const formData = new FormData(this);
        var form_object = {};
    formData.forEach(function(value, key){
        form_object[key] = value;
    });

    fetch("http://127.0.0.1:8000/plot3/", {                     
        method: ["POST"],                     
        body: JSON.stringify(form_object),         
        headers: { 
            "Content-type": "application/json; charset=UTF-8"
        } 
    }) 
    .then(response => response.json())
    .then(data => plot_data(data)); 
});
function plot_data(data){
    activity = [];
    reg_count = [];
    for(values of data){
        activity.push(values["BUSINESS_ACTIVITY"]);
        reg_count.push(values["count"]);
    }
    Highcharts.chart('output', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Top registrations by Principal Business Activity'
        },
        xAxis: {
            title: {
                text: 'Business Activity '
            },
            categories: activity
        },
        yAxis: {
            title: {
                text: 'Registrations'
            }
        },
        series: [{
            name: 'Registrations',
            data: reg_count
        }]
    });
}
