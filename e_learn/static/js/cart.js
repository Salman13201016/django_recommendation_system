$(document).ready(function () {
    $(".cart-product-description a").text(localStorage.getItem('title'))
    $(".quant-input input").val(localStorage.getItem('quantity'))
    $(".quant-input input").val(localStorage.getItem('quantity'))
    $(".cart-product-sub-total span").text(localStorage.getItem('price'))
    $(".cart-product-grand-total span").text(localStorage.getItem('total_price'))
})