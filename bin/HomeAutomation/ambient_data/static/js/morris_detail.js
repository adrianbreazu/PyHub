var temperature_array = [];
var humidity_array = [];
/* JSON has data sorted past-> present */
for (var i=0; i < jsonDataList.length; i++) {
    var obj = jsonDataList[i];

    if (obj.fields.type == 'temperature')
        temperature_array.push({date:obj.fields.read_datetime, temperature:obj.fields.value});
    else
        humidity_array.push({date:obj.fields.read_datetime, humidity:obj.fields.value});

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