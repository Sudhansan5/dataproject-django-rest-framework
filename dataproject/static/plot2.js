
    const myForm= document.getElementById('plot');
    myForm.addEventListener('submit', function(e){
        e.preventDefault();
        const formData = new FormData(this);
        var form_object = {};
    formData.forEach(function(value, key){
        form_object[key] = value;
    });

    fetch("http://127.0.0.1:8000/plot2/", {                     
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
    reg_year = [];
    company_count = [];
    for(values of data){
        reg_year.push(values["DATE_OF_REGISTRATION__year"]);
        company_count.push(values["count"]);
    }
    Highcharts.chart('output', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Barplot Of Registrations of Companies Per Year'
        },
        xAxis: {
            title: {
                text: 'Registration Year'
            },
            categories: reg_year
        },
        yAxis: {
            title: {
                text: 'Number of Companies'
            }
        },
        series: [{
            name: 'no of companies',
            data: company_count
        }]
    });
}
