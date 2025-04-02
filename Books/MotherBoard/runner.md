# Order of Execution

1. Markdown files are parsed

   We hook into the parser and catch the Markdown Blocks. We also associate blocks with the information, where their content starts and ends in the file.

   - Additional Markdown files can be sent, and they are not included, but associated with the blocks - before, after or in replacement.

   - Inside the Markdown, on Motherboard level we already understand the parts where to replace scripts with their output, and the parts which nest or include another Document in this one. This means Markdown can already process script output as planned, so we have .md extension lookup also contain dynamic cards. The script could return it's own code block, or None, to Markdown to have user reproduce the script run at this point.

   - Here we have HTML and Markdown solved as they _produce less_ than Json, the output contains less layers of information.
   - For Json, all data which is added to blocks, remains, and each part registers it's activities with blocks. Templates to produce HTML can also access this.

2. We close this, but as the script runs it can still parse more Markdown files, or the ones it has generatively, and the content would appear inside the attachments to the blocks.

   - For Json, the script would produce metadags and information, connected to the blocks: an AI trainer is interested in this.
   - We add Json content, where it knows about how it's Markdown input was mapped to the output, recognizing the positions in Markdown file; generated Markdown gets the position items equally. Each part of Markdown must have unique reference to this. Spider must decode this to have file output in Markdown.

     Thus, we call it the "json script", which is now ran, as it generates only json: int actually knows, for example, where the study cards start and stop.

Now, where Json already collects the results, so each view is hiddenly ran each time if this flag is on; still it can be less expensive; HTML is to be generated and the Json would get the generational output of this: for example, some part of Json scripts might be interested in actual tags; anyway, it should not affect the HTML output without care now. HTML which is produced can be now processed only as HTML, but good cityzens of the site should be already sleeping, not working with new visions for the past so eagerly.

DHTML should be generated from the same blocklist as HTML was generated from, filling other personal properties. It creates more dynamic mode in later versions, currently table.

For important chapters such as "Menu", "Tools" etc., in DHTML where they are in separate cells of table, cut those titles and remove the title into style sheet variable, leaving the style sheet metadata.

3. Flask can be used here: each generated HTML is rather a block or piece of the site.

Thereof:
- We can show DHTML and HTML as they are rendered in the end.
- We can show Json as it collects all the hidden values for the script, for example it could detect actual types.
- We can show Markdown as we knew the scripts in advance and could run them, also we could properly include each part.
  - Our Markdown supports only top-level titles, which start from beginning of the line, and in python, top level comments as well to render them as Markdown, but perhaps having the "#" in visible or hidden form for copying.

----

# Systems used in the Architecture

__Systems__:
- __Python__: _Programming Language_.
- __Mistune__: _Markdown Parser_.
- __Flask__: _Web Server_.
