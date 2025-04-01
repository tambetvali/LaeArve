# Freedom

Suggesting models, cling to our criteria of Freedom:
- While it's acceptable one needs to create an account to download a model:
  - We do not think it's reliable source, which cannot provide their models at static download urls.
  - We do not like automated cache, which would download a model, not excluding randomly deleting it because it's "tmp" or "cache".
  - We need to download real data, in form of files, into appropriate folder, where we _do_ have all offline content.
  - Each associated document is downloadable.
  - We can fine-tune this trivially, and with PyTorch, and create gguf file.

Hugging Face:
- The download is _advanced_, while downloaders are not: for some time, downloading is simple and generally does not depend on many libraries. In case the downloader goes into version conflicts and other effects of advanced usage, we don't consider it _free_, and if no plain downloading in common formats exists, or it needs _building scripts_, it's generally also not _open source_ in definite sense. We make exceptions, where for example we don't know better tool than PyTorch, even if this also supports some extreme online community, which does not know how to download documentation into their computer and rely locally.
- Where we use online services, it has to be optional. For example CoPilot Code Assistant on side of Continue.

These are not so hard rules, but where we download 10-20 libraries, we do not need any advanced features, which need to be understanding in context of alien ecosystems and frameworks: you will see how my own standard evolves.
