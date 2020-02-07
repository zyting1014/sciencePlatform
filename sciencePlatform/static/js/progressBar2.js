// processBar进度条 js

function shuffle(o){ //v1.0
	for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
}

var colors2 = [
	['#8491C3', '#8CD2BC'],
	['#D3B6C6', '#4B253A'],
	['#BEE3F7', '#45AEEA'],
	['#F5F5F2', '#CCA6BF'],
	['#7FCCE3', '#308BAE'],
	['#FFE8D9', '#1C6867'],
], circles = [];

var li = [56.390,32.557,4.479,9.067,5.205,24.654] // 要填入的值

for (var i = 6; i <= 11; i++) {
	var child = document.getElementById('circles-' + i),
		percentage = li[i - 6];

	circles.push(Circles.create({
		id:         child.id,
		value:		percentage,
		radius:     60,
		width:      10,
		colors:     colors2[i - 6]
	}));
}

// document.getElementById('add_button_').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].update(circles[i]._value + 10, 250);
// };
//
// document.getElementById('substract_button_').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].update(circles[i]._value - 10, 250);
// };
//
// document.getElementById('add_width_button_').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].updateWidth(circles[i]._strokeWidth + 10);
// };
//
// document.getElementById('substract_width_button_').onclick = function()
// {
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].updateWidth(circles[i]._strokeWidth - 10);
// };
//
// document.getElementById('colors_button_').onclick = function()
// {
// 	colors = shuffle(colors);
// 	for(var i = 0, l = circles.length; i < l; i++)
// 		circles[i].updateColors(colors[i]);
// };