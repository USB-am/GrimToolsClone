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
	el.onclick = function () {
		var id_name = this.attributes['id'].value;
		open_inventory(id_name);
	};
}

async function open_inventory(item_type) {
	document.getElementById('equipments').style.display = 'block';
	var data = {
		'request_type': 'open_inventory',
		'item_type': item_type,
	}
	var items = await request(URL_OPEN_INVENTORY, data);
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
	bind_all_items();

	return result
}
/* = SEND REQUEST TO SERVER = */
/* === OPEN INVENTORY === */

/* === SELECT ITEM === */
var ACTIVE_ITEM_SELECTED = null;

function bind_all_items() {
	var items = document.getElementsByClassName('equip');
	for (var i = 0; i < items.length; i++) {
		items[i].onclick = function () {
			if (ACTIVE_ITEM_SELECTED != null) {
				ACTIVE_ITEM_SELECTED.classList.remove('selected-equip');
			}
			this.classList.add('selected-equip');
			ACTIVE_ITEM_SELECTED = this;
			// alert(this.getElementsByClassName('item-pk')[0].innerHTML);
		}
	}
}
/* === SELECT ITEM === */