document.addEventListener('DOMContentLoaded', function() {

const menuIcon = document.getElementById('menu-icon');
const dropDownMenu = document.getElementById('dropDown-menu');

console.log('menu icon clicked');

menuIcon.addEventListener('click', function(){dropDownMenu.classList.toggle('show');
});
});