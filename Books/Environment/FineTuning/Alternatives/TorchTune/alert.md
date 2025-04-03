# Alert

So it was like I _had_ depend on Hugging Face not on stable provider of models in compatible format. Now it's resolved: torchtune.

/ I don't want to stop before I know an installation, which won't have version conflicts: even if they pack the correct versions into their bundle with built-in python, they would have solved the problem /

## CoPilot for very specific question, again just gave the same answer.

Yes, there are self-contained distributions designed specifically to bypass those dependency headaches. Instead of manually installing the Hugging Face Transformers library and wrestling with its version requirements, you can use tools like PyTorch’s torchtune that come packaged with fixed dependency versions and an integrated CLI. This means you get an environment where the fine-tuning recipes and model downloads are managed internally, so you don’t need to worry about external library conflicts.

For example, torchtune includes built-in commands such as:
```bash
tune download meta-llama/Llama-3.2-1B-Instruct --output-dir /tmp/Llama-3.2-1B-Instruct --hf-token <YOUR_TOKEN>
```

This command downloads one of the supported models directly from Hugging Face, using preconfigured settings that guarantee compatibility with the torchtune framework. The supported model list in torchtune covers many popular LLMs—Llama 2, Llama 3 (in multiple versions), Mistral, Gemma, Phi, Qwen, and more—which makes it a solid alternative if you want to avoid the common version conflicts seen with a more DIY approach.

Additionally, because torchtune can be installed in isolated environments (or even provided as containerized images), you can be sure that all its required libraries (e.g., specific versions of PyTorch, CUDA if needed, etc.) are properly pinned. This encapsulation prevents any clash with your other local installations.

In summary, if you’re looking for a downloadable, self-contained program that lets you download and fine-tune a model (from the torchtune-supported list) without dependency conflicts, torchtune is an excellent candidate to check out. It’s designed to take care of the under-the-hood details, letting you focus directly on model fine-tuning rather than environment management.

If you’re curious about the specifics of the supported models or the available fine-tuning recipes, exploring their cheatsheet and documentation can offer even more insight into how torchtune streamlines the process. You might also look into community discussions and examples on GitHub to see how others are leveraging this tool for various fine-tuning tasks [1](https://gist.github.com/razhangwei/f2841284f876034abe8660779329ac0a) [2](https://pytorch.org/torchtune/stable/api_ref_models.html).

# Old

Our default method perhaps in developer environment, where the user environment might prefer _OpenLLM_. We are scalable about choosing the fine-tuners for different tasks and models.

I prefer __PyTorch__ as it's a standard library: TensorFlow used by HuggingFace is constantly breaking in backwards compability with the books and in future, your own code. We want to use rather what is kind of _settled_, not providing with all kinds of surprise.

- __[torchtune](https://github.com/pytorch/torchtune)__
- _[Welcome to the torchtune Documentation](https://pytorch.org/torchtune/stable/index.html)_

- [torchtune Overview](https://pytorch.org/torchtune/stable/overview.html)

## Task done

Well currently I got, with clear wording, from CoPilot what I wanted, but this was:

Extremely hard to convince CoPilot or ChatGPT I want real download link not some nonsense talk at hugging face cards and their broken-version transformers ..a good old link to just download the tar.gz, not automations and registrations and more libraries ..to just fine-tune with pytorch. I don't understand why they think download links are _useless_ and have this nonsense menthality for providing _advanced_ exception to rules of downloading, as simple as clicking a link and not listing facebook models which want licence clicks.

I am trying to explain it while i have half hours and it has some hugging face bannering and advertizing studion input without accepting most simple requirements: I SAID i want FREE coding models 0.5B and 3.0B, I don't want to see those licences of random unrelated distributors. I want free open source model to train myself I said, and a working link, not different types of clever interfaces to provide something like nonsense around simple links. It's already clear we want tar.gz file no? It needs to exist at this link, simply exist nothing more, and no forms or banners or fancy companies with their advanced downloaders please.
Me: BUT I SAID CHECK THE LINKS!
(I start to think about completely avoiding Hugging Face, because they are really providing a nice and clever interface to their apis, consequently making simple requests work only with proper versions..) Versus somebody, who can just provide lasting links to their models and _directly downloads_.

https://github.com/QwenLM/Qwen2.5-Coder

Again something needed from _transformers_ ..I said I'm DOWNLOADING, like in good old 386 times when it already worked, and not TRANSFORMING or trying to use some advanced database system. I don't like people with problems managing their files - so, continued tomorrow as I get nothing in 1H and the gpts don't want to disable Llama and Facebook because they talk about licences, and Hugging Face with their advanced functionalities: I really don't need advanced functionalities at all, I want to train an AI.

The problem is: people generally like their resources, generally features.

I really want to install packages, not just mere web spiders who never know their own needs - if going to fine-tune, give me the components that's it, I don't have to solve the laws and your complex forms, it's clear I typically need either to fine-tune or run it, not read your interesting cards with download buttons maybe and many parameters not available for search.

(I leave this here, I hope later we have good sources and PyTorch support)

It's still on track with it's favourite products: I looked inside, there is tensorflow code. In the whole book: no tensorflow code. Understand I _did_ select tools.

And again some Hugging Face manual ..I SAID they cannot do pdf's and downloadable HTML collections, I don't want to search their automatic tools at all, I really want a download link for _everythin_. I don't want to even check for this. If I'm doing it offline, don't run with your services and "expectations", simpler tools would do, if they are properly developed into proper KISS projects and know offline people who look for download link, not your fancy way for more closed source text and fancy compilator links.

how to download this torch documentation? if I asked for download, I mean it literally and it's not the docs page