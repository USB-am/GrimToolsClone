/* === CLOSE INVENTORY === */
document.getElementById('close-inventory-btn').onclick = function () {
	document.getElementById('equipments').style.display = 'none';
}
/* === CLOSE INVENTORY === */


/* === OPEN INVENTORY === */
const OPENING_BLOCKS = ['helm', 'amulet', 'chest-armor', 'shoulders'];
for (var i = 0; i < OPENING_BLOCKS.length; i++) {
	var now_id = OPENING_BLOCKS[i];
	var el = document.getElementById(now_id);
	el.onclick = function () {open_inventory(now_id);}
}

function open_inventory(item_type) {
	document.getElementById('equipments').style.display = 'block';
	var data = {
		'item_type': item_type,
	}
	var items = request(URL_OPEN_INVENTORY, data);
	var equip_list = document.getElementById('equip-list');
	equip_list.innerHTML = items;
}

/* = SEND REQUEST TO SERVER = */
async function request(url, data) {
	const response = await fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
			'X-CSRFToken': CSRF_TOKEN,
		},
		body: JSON.stringify(data),
	})
	const result = await response.text()
	return result
}
/* = SEND REQUEST TO SERVER = */
/* === OPEN INVENTORY === */