$(document).ready(function() {
    $('.side_navigation').hover(function(){
        $('.main_content').attr('id', 'side_navigation_hover');
        $('.main_content_2').attr('id', 'side_navigation_hover_2');
    });

    $('.side_navigation').click(function(){
        $('.main_content').attr('id', 'side_navigation_hover');
        $('.main_content_2').attr('id', 'side_navigation_hover_2');
    });

    $('.side_navigation').mouseleave(function(){
        $('#side_navigation_hover').removeAttr('id');
        $('#side_navigation_hover_2').removeAttr('id');
    });

    $('.search').hover(function(){
        $('.search').attr('id', 'main_content_2_hover');
        $('.choose').attr('id', 'choose_fade_with_search_hover');
        $('#search_input_box').focus();
    });

    $('.search').click(function(){
        $('.search').attr('id', 'main_content_2_hover');
        $('.choose').attr('id', 'choose_fade_with_search_hover');
        $('#search_input_box').focus();
    });

    $('.search').mouseleave(function(){
        $('#main_content_2_hover').removeAttr('id');
        $('#choose_fade_with_search_hover').removeAttr('id');
    });

    $('.choose').click(function(){
        $('#main_content_2_hover').removeAttr('id');
        $('#choose_fade_with_search_hover').removeAttr('id');
    });


    $('.shop_container').click(function() {

        if ($(this).find('.checkbox_css').attr('checked')) {
            $(this).find('.checkbox_css').removeAttr('checked');
        }
        else {
            $(this).find('.checkbox_css').attr('checked');
        }
    });

    // var $choose = $('.choose'),
 //    var  $element = $('.choose_scroll_top'),
 //    var  className = 'hasScrolled';

    // $choose.scroll(function() {
    //   $element.toggleClass(className, $document.scrollTop() >= 50);
    // });


});
