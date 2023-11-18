$(document).ready(function () {
    quant_value = 0
    quant = parseInt($('#quant_input_value').val());
    price = parseFloat($('.price_box_main').text())
    $('.basket-item-count span').text(quant)
    $('.total-price .value').text(quant * price)
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


        // alert(quant)

    });
});

