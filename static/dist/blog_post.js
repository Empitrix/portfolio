import { remark } from "https://cdn.jsdelivr.net/npm/remark@15.0.1/+esm";
import { unified } from 'https://esm.sh/unified@11?bundle';
import remarkGfm from 'https://esm.sh/remark-gfm@4?bundle';
import remarkParse from 'https://esm.sh/remark-parse@11?bundle';
import remarkRehype from 'https://esm.sh/remark-rehype@11?';
import rehypeSanitize from 'https://esm.sh/rehype-sanitize@6?bundle';
import rehypeStringify from 'https://esm.sh/rehype-stringify@10?bundle';
import rehypeFormat from 'https://esm.sh/rehype-format@5?bundle';
import rehypeHighlight from 'https://esm.sh/rehype-highlight@6';
// import remarkPrism from 'https://cdn.skypack.dev/remark-prism';

// const file = await unified()
// const file = await remark()
const file = await unified()
	.use(remarkParse)
	.use(remarkGfm)
	.use(remarkRehype)  // CUZED
	.use(rehypeSanitize)
	.use(rehypeFormat)
	.use(rehypeStringify)
	// .use(remarkPrism)
	// .use(rehypeHighlight)
	.data('settings', {fragment: true})
	.use(rehypeHighlight, {plainText: ['txt', 'text']})
	// .process(markdownData);
	// .processSync("# Hi\n\n*Hello*\n**Hello**\n***Hello***\n, world!");
	.processSync(markdownData);

// console.log(file);
// document.getElementById('marked').innerHTML = file.value;
// console.log(String(file))
document.getElementById('marked').innerHTML = String(file);
// document.getElementById('marked').innerHTML = file.result;

