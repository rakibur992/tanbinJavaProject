$(function () {
    var noty =  new Noty({
        type: 'success',
        layout: 'topLeft',
        theme: 'nest',
        text: 'Data Submitted Successfull',
        timeout: '4000',
        progressBar: true,
        closeWith: ['click'],
        killer: true,
    })

    // Handler for .ready() called.
    $("#comboBox").on("click", function (event) {
        var clicked = $(event.target)
        console.log()
        if (clicked.hasClass("dropdown-item")) {
            $("#selectMonth").text(clicked.text())
        }
    });
    $(".save").on("click", function (events) {
        var clicked_pack = $(events.target).parent().parent()
        var id = clicked_pack.attr('id')
        var month = $("#selectMonth").text()
        var monthly_incentive = clicked_pack.children(".monthly_incentive").text()
        var performance_bonus = clicked_pack.children(".performance_bonus").text()
        try {
            monthly_incentive = parseInt(monthly_incentive)
            performance_bonus = parseInt(performance_bonus)
        } catch (err) {
            console.log(err.message)
        }
        
        csrf_token=$('{% csrf_token %}').val()
        
        $.ajax({
            type: "POST",
            url: "{% url 'MonthlyEmployeePayroll' company %}",
            data:  {'data': "sucess",
            'csrfmiddlewaretoken' : csrf_token
            }
          });
        noty.show()
       
        


    });

});