

//Navigation
var app = function () {
	var body = undefined;
	var menu = undefined;
	var menuItems = undefined;
	var init = function init() {
		body = document.querySelector('.cd-header');
		menu = document.querySelector('.menu-icon');
		menuItems = document.querySelectorAll('.nav__list-item');
		applyListeners();
	};
	var applyListeners = function applyListeners() {
		menu.addEventListener('click', function () {
			return toggleClass(body, 'nav-active');
		});
	};
	var toggleClass = function toggleClass(element, stringClass) {
		if (element.classList.contains(stringClass)) element.classList.remove(stringClass);else element.classList.add(stringClass);
	};
	init();
}();              
(function($) { "use strict";
	$(function() {
		var header = $(".cd-header");
		$(window).scroll(function() {    
			var scroll = $(window).scrollTop();
		
			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
				
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});		
		
			
	
})(jQuery); 