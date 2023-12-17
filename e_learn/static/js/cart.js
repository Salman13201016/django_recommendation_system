$(document).ready(function () {
    // $(".cart-product-description a").text(localStorage.getItem('title'))
    // $(".quant-input input").val(localStorage.getItem('quantity'))
    // $(".quant-input input").val(localStorage.getItem('quantity'))
    // $(".cart-product-sub-total span").text(localStorage.getItem('price'))
    // $(".cart-product-grand-total span").text(localStorage.getItem('total_price'))

    tbody = $('.cart_details_tbody').empty()
    title_array = JSON.parse(localStorage.getItem('title'))

    for (i = 0; i < title_array.length; i++) {
        tr = '<tr><td class="romove-item"><a href="#" title="cancel" class="icon"><i class="fa fa-trash-o"></i></a></td><td class="cart-image"><a class="entry-thumbnail" href="detail.html"><img src="assets/images/products/p1.jpg" alt=""></a></td><td class="cart-product-name-info"><h4 class="cart-product-description"><a href="detail.html">' + title_array[i] + '</a></h4><div class="row"><div class="col-sm-4"><div class="rating rateit-small"></div></div><div class="col-sm-8"><div class="reviews">(06 Reviews)</div></div></div><div class="cart-product-info"><span class="product-color">COLOR:<span>Blue</span></span></div></td><td class="cart-product-edit"><a href="#" class="product-edit">Edit</a></td><td class="cart-product-quantity"><div class="quant-input"><div class="arrows"><div class="arrow plus gradient"><span class="ir"><i class="icon fa fa-sort-asc"></i></span></div><div class="arrow minus gradient"><span class="ir"><i class="icon fa fa-sort-desc"></i></span></div></div><input type="text" value="1"></div></td><td class="cart-product-sub-total"><span class="cart-sub-total-price">$300.00</span></td><td class="cart-product-grand-total"><span class="cart-grand-total-price">$300.00</span></td></tr>'
        tbody.append(tr)

    }


})