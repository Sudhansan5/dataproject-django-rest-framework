
    const myForm= document.getElementById('plot');
    myForm.addEventListener('submit', function(e){
        e.preventDefault();
        const formData = new FormData(this);
        var form_object = {};
        multi_data = [];
    formData.forEach(function(value, key){
        if (key == "pba"){
            multi_data.push(value);
        }
        else{
            form_object[key] = value;
        }
    });
    form_object["pba"]= multi_data;

    fetch("http://127.0.0.1:8000/plot4/", {                     
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
    reg_year = []
    activity = {}
    for(values of data){
        if (!reg_year.includes(values["DATE_OF_REGISTRATION__year"]))
            {
                reg_year.push(values["DATE_OF_REGISTRATION__year"]);
            }
        activity[values["BUSINESS_ACTIVITY"]] = []
    }

    for(values of data){
        activity[values["BUSINESS_ACTIVITY"]].push(values["count"])
    }
    
    series_data = []
    for (values in activity){
        organised_data = {}
        organised_data["name"]= values
        organised_data["data"]= activity[values]

        series_data.push(organised_data)
    }
    Highcharts.chart('output', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Registration Counts for Principal Business Activity'
    },
    xAxis: {
        categories: reg_year,
        title: {
            text: 'Year'
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Registration Count'
        }
    },

    series: series_data
});
}