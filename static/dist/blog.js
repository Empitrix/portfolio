// console.log("Hello, World !");

function moveToPost(id){
	console.log(id);
	document.location.href = `${document.location.href}/0x${id.toString(16)}`
	// a = `${document.location.href}/${id}`
	// console.log(typeof a);
	// console.log(a);
}

