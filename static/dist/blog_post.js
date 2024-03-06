import { remark } from "https://cdn.jsdelivr.net/npm/remark@15.0.1/+esm";
import { unified } from 'https://esm.sh/unified@11?bundle';
import remarkGfm from 'https://esm.sh/remark-gfm@4?bundle';
import remarkParse from 'https://esm.sh/remark-parse@11?bundle';
import remarkRehype from 'https://esm.sh/remark-rehype@11?';
import rehypeSanitize from 'https://esm.sh/rehype-sanitize@6?bundle';
import rehypeStringify from 'https://esm.sh/rehype-stringify@10?bundle';
import rehypeFormat from 'https://esm.sh/rehype-format@5?bundle';
import rehypeHighlight from 'https://esm.sh/rehype-highlight@6';

const file = await remark()
	.use(remarkParse)
	.use(remarkGfm)
	.use(remarkRehype)  // CUZED
	.use(rehypeSanitize)
	.use(rehypeFormat)
	.use(rehypeStringify)
	.use(rehypeHighlight, {plainText: ['txt', 'text']})
	.processSync(markdownData);

document.getElementById('marked').innerHTML = String(file);


/*
// using typescript classes
// import { Marked, Renderer } from '@ts-stack/markdown';
import { Marked, Renderer } from 'https://cdn.jsdelivr.net/npm/@ts-stack/markdown@1.5.0/+esm';

Marked.setOptions ({
	renderer: new Renderer,
	gfm: true,
	tables: true,
	breaks: false,
	pedantic: false,
	sanitize: false,
	smartLists: true,
	// highlight: (code, lang) => lang != null ? hljs.highlight(lang, code).value : null,
	smartypants: false
});
document.getElementById('marked').innerHTML = Marked.parse(markdownData);
*/

