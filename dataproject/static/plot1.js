const myForm= document.getElementById('plot');
myForm.addEventListener('submit', function(e){
    e.preventDefault();
    const formData = new FormData(this);
    var form_object = {};
formData.forEach(function(value, key){
    form_object[key] = value;
});

fetch("http://127.0.0.1:8000/plot1/", {                     
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
auth_cap_val=[];
reg_count = [];
authoried_cap = {'<=1L': 0,
             '1L to 10L': 0,
             '10L to 1Cr': 0,
             '1Cr to 10Cr': 0,
             '>10Cr': 0}

for(item of data){  
    authoried_cap[item["intervals"]]=item["count"];
}    

for (value in authoried_cap){
    auth_cap_val.push(value)
    reg_count.push(authoried_cap[value])
}

Highcharts.chart('output', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Barplot of Authorized Capital'
    },
    xAxis: {
        title: {
            text: 'Authorized Capital Value'
        },
        categories: auth_cap_val
    },
    yAxis: {
        title: {
            text: 'Number of Companies'
        }
    },
    series: [{
        name: 'Capital Count',
        data: reg_count
    }]
});
}