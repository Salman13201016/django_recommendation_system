$(document).ready(function () {
    // localStorage.clear()
    quant_value = 0
    // quant = parseInt($('#quant_input_value').val());
    // price = parseFloat($('.price_box_main').text())
    // $('.basket-item-count span').text(quant)
    // $('.total-price .value').text(quant * price)

    if (localStorage.getItem('quantity')) {
        $('.basket-item-count span').text(localStorage.getItem('quantity'))
    }
    else {
        alert(1)
        quant = parseInt($('#quant_input_value').val());
        $('.basket-item-count span').text(quant)
    }

    if (localStorage.getItem('total_price')) {
        $('.total-price .value').text(localStorage.getItem('total_price'))
    }
    else {
        alert(2)
        price = parseFloat($('.price_box_main').text())
        $('.total-price .value').text(quant * price)
    }
    $('.arrow_plus').click(function () {
        quant = parseInt($('#quant_input_value').val());
        quant = quant + 1;

        if (quant > 2) {

            alert("you can not order more than 2")
            // $('.arrow_plus').prop('disabled', true)
            $('#quant_input_value').prop('disabled', true)
            $('#quant_input_value').val(2)
        }
        else {

            $('#quant_input_value').val(quant)
        }

        // alert(quant)

    });
    $('.arrow_minus').click(function () {
        quant = parseInt($('#quant_input_value').val());
        quant = quant - 1;

        if (quant < 1) {

            alert("you can not order less than 1")
            // $('.arrow_plus').prop('disabled', true)
            $('#quant_input_value').prop('disabled', true)
            $('#quant_input_value').val(1)
        }
        else {

            $('#quant_input_value').val(quant)
        }

        // alert(quant)

    });

    $('.add_to_cart_button').click(function () {
        quant = parseInt($('#quant_input_value').val());
        price = parseFloat($('.price_box_main').text())
        $('.basket-item-count span').text(quant)
        $('.total-price .value').text(quant * price)
        title = $("#course_title").text()

        localStorage.setItem('title', title)
        localStorage.setItem('quantity', quant)
        localStorage.setItem('price', price)
        localStorage.setItem('total_price', quant * price)


        // alert(quant)

    });
});

