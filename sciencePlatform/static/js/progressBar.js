// processBar进度条 js

function shuffle(o){ //v1.0
	for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
}

var colors = [
	['#D3B6C6', '#4B253A'], ['#FCE6A4', '#EFB917'], ['#BEE3F7', '#45AEEA'], ['#F8F9B6', '#D2D558'], ['#F4BCBF', '#D43A43']
], circles = [];

var li = [59.657,58.621,64.529,57.482,0] // 要填入的值

for (var i = 1; i <= 4; i++) {
	var child = document.getElementById('circles-' + i),
		percentage = li[i - 1];

	circles.push(Circles.create({
		id:         child.id,
		value:		percentage,
		radius:     60,
		width:      10,
		colors:     colors[i - 1]
	}));
}

// document.getElementById('add_button').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].update(circles[i]._value + 10, 250);
// };
//
// document.getElementById('substract_button').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].update(circles[i]._value - 10, 250);
// };
//
// document.getElementById('add_width_button').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].updateWidth(circles[i]._strokeWidth + 10);
// };
//
// document.getElementById('substract_width_button').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].updateWidth(circles[i]._strokeWidth - 10);
// };
//
// document.getElementById('colors_button').onclick = function()
// {
// 	colors = shuffle(colors);
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].updateColors(colors[i]);
// };