var data_array = [];
for (var i=0; i < jsonDataList.length; i++) {
    var obj = jsonDataList[i];
    if (obj.fields.type == 'temperature')
        data_array.push({date:obj.fields.read_datetime, temperature:obj.fields.value});
    else
        data_array.push({date:obj.fields.read_datetime, humidity:obj.fields.value});
};

$(Morris.Line({
    element: 'morris-sensor-chart',

    data: data_array,

    xkey: 'date',

    ykeys: ['temperature', 'humidity'],

    labels: ['Temperature', 'Humidity']
}));