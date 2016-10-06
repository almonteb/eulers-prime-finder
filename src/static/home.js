$(document).ready(function () {
    $('#singleSubmit').on('click', function (event) {
        clear_results();
        $.ajax({
            type: 'POST',
            url: '/single',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                x: $('#x').val(),
                y: $('#y').val()
            }),
            success: function (data) {
                handle_primes(data);
            },
            error: function (data) {
                handle_error(data);
            }
        });
        event.preventDefault();
    });

    $('#uploadSubmit').on('click', function (event) {
        clear_results();
        var data = new FormData();
        data.append('file', $('#file')[0].files[0]);

        $.ajax({
            type: 'POST',
            url: '/multiple',
            processData: false,
            contentType: false,
            data: data,
            success: function (data) {
                handle_primes(data);
            },
            error: function (data) {
                handle_error(data);
            }
        });
        event.preventDefault();
    });

    function handle_primes(data) {
        var content = '<table border=1>';
        content += '<tr><th>Xth</th><th>Y # of digits</th><th>Prime</th><th>Position</th></tr>';
        $.each(data.primes, function (index, prime) {
            content += '<tr><td>' + prime.xth + '</td><td>' + prime.num_digits + '</td><td>' + prime.prime + '</td><td>' + prime.pos + '</td></tr>'

        });
        content += '</table>';
        $('#results').html(content)
    }

    function handle_error(data) {
        console.log(data);
        $('#results').html("Error: " + data.responseJSON.error);
    }

    function clear_results() {
        $('#results').html('');
    }
});
