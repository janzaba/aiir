
function getRenders(url){
    $.ajax({
        url: url,
        type: "POST",
        data: {},
        dataType:'json',
        success: function(data){
            var i = 1;
            $.each(data, function( index, v ) {
                var row = '<tr><td><a href="">' + i + '</a></td>';
                row += "<td>" + v.name + "</td>";
                row += "<td>" + v.start_date + "</td>";
                row += "<td>" + v.end_date + "</td></tr>";
                $('#renders tbody').append(row);
                i++;
            });
        },
        error: function(e){
            alert("failure: " + e.status);
        }
    });
}