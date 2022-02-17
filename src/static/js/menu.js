$(document).ready(function() {
	$('.menu-burger__header').click(function(event){
                $('.menu-burger__header').toggleClass('open-menu');
                $('.header__nav').toggleClass('open-menu');
                $('body').toggleClass('fixed-page');
	});
});