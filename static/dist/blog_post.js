// document.getElementById('marked').innerHTML = marked.parse('');


// console.log(document.getElementById('marked').innerHTML)
// document.getElementById('marked').innerHTML = marked.parse(document.getElementById('marked').innerHTML);
const {markedHighlight} = globalThis.markedHighlight;

marked.use(markedHighlight({
	langPrefix: 'hljs language-',
	highlight(code, lang) {
		const language = hljs.getLanguage(lang) ? lang : 'plaintext';
		return hljs.highlight(code, { language }).value;
	}
}));


// document.getElementById('marked').innerHTML = "MAMAD";
document.getElementById('marked').innerHTML = DOMPurify.sanitize(marked.parse(markdownData))
// document.getElementById('marked').innerHTML =
// 	DOMPurify.sanitize(marked.parse(document.getElementById('marked').innerHTML));


// console.log();

