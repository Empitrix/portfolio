function moveToPost(id){
	/* Convert id (DECIMAL) to HEXADECIMAL */
	id = `0x${id.toString(16).padStart(4, "0")}`;
	document.location.href = `${document.location.href}/${id}`
}

