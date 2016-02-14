var temperature_array = [];
var humidity_array = [];
var filtered_date = new Date();
filtered_date = filtered_date.getTime() - 172800000;

/* JSON has data sorted past-> present */
for (var i=0; i < jsonDataList.length; i++) {
    var obj = jsonDataList[i];
    var objReadDateTime = new Date(obj.fields.read_datetime);

    if (objReadDateTime > filtered_date) {
        if (obj.fields.type == 'temperature')
            temperature_array.push({date:obj.fields.read_datetime, temperature:obj.fields.value});
        else
            humidity_array.push({date:obj.fields.read_datetime, humidity:obj.fields.value});
    }

};

$(Morris.Line({
    element: 'morris-temperature-chart',

    data: temperature_array,

    xkey: 'date',

    ykeys: ['temperature'],

    labels: ['Temperature']
}));

$(Morris.Line({
    element: 'morris-humidity-chart',

    data: humidity_array,

    xkey: 'date',

    ykeys: ['humidity'],

    labels: ['Humidity']
}));