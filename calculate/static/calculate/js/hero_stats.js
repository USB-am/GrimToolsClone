document.querySelector('#rem-physique').onclick = function () {
	var available_points = document.getElementById('available-points');
	var count = document.getElementById('physique-count');
	var current_val = document.getElementById('physique-count-current');
	var global_val = document.getElementById('global-physique');

	if (parseInt(count.innerHTML, 10) > 0) {
		count.innerHTML = parseInt(count.innerHTML, 10) - 1;
		available_points.innerHTML = parseInt(available_points.innerHTML, 10) + 1;
		current_val.innerHTML = 50 + parseInt(count.innerHTML, 10);
		global_val.innerHTML = current_val.innerHTML;
		document.getElementById('rem-physique').style.opacity = 1;
		onAllAddBtns();
	}
	if (parseInt(count.innerHTML, 10) == 0) {
		document.getElementById('rem-physique').style.opacity = .5;
	}
}
document.querySelector('#add-physique').onclick = function () {
	var available_points = document.getElementById('available-points');
	var count = document.getElementById('physique-count');
	var current_val = document.getElementById('physique-count-current');
	var global_val = document.getElementById('global-physique');

	if (parseInt(available_points.innerHTML, 10) > 0) {
		count.innerHTML = parseInt(count.innerHTML, 10) + 1;
		available_points.innerHTML = parseInt(available_points.innerHTML, 10) - 1;
		current_val.innerHTML = 50 + parseInt(count.innerHTML, 10);
		global_val.innerHTML = current_val.innerHTML;
		document.getElementById('rem-physique').style.opacity = 1;
		document.getElementById('add-physique').style.opacity = 1;
	}
	if (parseInt(available_points.innerHTML, 10) == 0) {
		offAllAddBtns();
		document.getElementById('rem-physique').style.opacity = 1;
	}
}

document.querySelector('#rem-cunning').onclick = function () {
	var available_points = document.getElementById('available-points');
	var count = document.getElementById('cunning-count');
	var current_val = document.getElementById('cunning-count-current');
	var global_val = document.getElementById('global-cunning');

	if (parseInt(count.innerHTML, 10) > 0) {
		count.innerHTML = parseInt(count.innerHTML, 10) - 1;
		available_points.innerHTML = parseInt(available_points.innerHTML, 10) + 1;
		current_val.innerHTML = 50 + parseInt(count.innerHTML);
		global_val.innerHTML = current_val.innerHTML;
		document.getElementById('rem-cunning').style.opacity = 1;
		onAllAddBtns();
	}
	if (parseInt(count.innerHTML, 10) == 0) {
		document.getElementById('rem-cunning').style.opacity = .5;
	}
}
document.querySelector('#add-cunning').onclick = function () {
	var available_points = document.getElementById('available-points');
	var count = document.getElementById('cunning-count');
	var current_val = document.getElementById('cunning-count-current');
	var global_val = document.getElementById('global-cunning');

	if (parseInt(available_points.innerHTML, 10) > 0) {
		count.innerHTML = parseInt(count.innerHTML, 10) + 1;
		available_points.innerHTML = parseInt(available_points.innerHTML, 10) - 1;
		current_val.innerHTML = 50 + parseInt(count.innerHTML, 10);
		global_val.innerHTML = current_val.innerHTML;
		document.getElementById('rem-cunning').style.opacity = 1;
		document.getElementById('add-cunning').style.opacity = 1;
	}
	if (parseInt(available_points.innerHTML, 10) == 0) {
		offAllAddBtns();
		document.getElementById('rem-cunning').style.opacity = 1;
	}
}

document.querySelector('#rem-spirit').onclick = function () {
	var available_points = document.getElementById('available-points');
	var count = document.getElementById('spirit-count');
	var current_val = document.getElementById('spirit-count-current');
	var global_val = document.getElementById('global-spirit');

	if (parseInt(count.innerHTML, 10) > 0) {
		count.innerHTML = parseInt(count.innerHTML, 10) - 1;
		available_points.innerHTML = parseInt(available_points.innerHTML, 10) + 1;
		current_val.innerHTML = 50 + parseInt(count.innerHTML, 10);
		global_val.innerHTML = current_val.innerHTML;
		document.getElementById('rem-spirit').style.opacity = 1;
		onAllAddBtns();
	}
	if (parseInt(count.innerHTML, 10) == 0) {
		document.getElementById('rem-spirit').style.opacity = .5;
	}
}
document.querySelector('#add-spirit').onclick = function () {
	var available_points = document.getElementById('available-points');
	var count = document.getElementById('spirit-count');
	var current_val = document.getElementById('spirit-count-current');
	var global_val = document.getElementById('global-spirit');

	if (parseInt(available_points.innerHTML, 10) > 0) {
		count.innerHTML = parseInt(count.innerHTML, 10) + 1;
		available_points.innerHTML = parseInt(available_points.innerHTML, 10) - 1;
		current_val.innerHTML = 50 + parseInt(count.innerHTML, 10);
		global_val.innerHTML = current_val.innerHTML;
		document.getElementById('rem-spirit').style.opacity = 1;
		document.getElementById('add-spirit').style.opacity = 1;
	}
	if (parseInt(available_points.innerHTML, 10) == 0) {
		offAllAddBtns();
		document.getElementById('rem-spirit').style.opacity = 1;
	}
}

function offAllAddBtns() {
	document.getElementById('add-physique').style.opacity = .5;
	document.getElementById('add-cunning').style.opacity = .5;
	document.getElementById('add-spirit').style.opacity = .5;
}
function onAllAddBtns() {
	document.getElementById('add-physique').style.opacity = 1;
	document.getElementById('add-cunning').style.opacity = 1;
	document.getElementById('add-spirit').style.opacity = 1;
}