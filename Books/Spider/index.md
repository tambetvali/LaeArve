# Functionality of Spider

## Initial functionality

Initially, it needs to support these, and a simple implementation should always exist with this functionality:
- Download Laegna Math Website or use it actively.
- Train AIs based on generated cards, converting them to Anki format in that purpose.

## Target functionality

### Source Management

Locate sources:
- Laegna Math Website: create access to pages and generators.
- Local Chat History: create access to local chat history.
- Document Collections: create access to local document collections.
- Crawl web: create access to compatible website structures.
  - We might include Notion.so and similar APIs.
- Create instances of Laegna Math Website and derivatives.
  - Be able to download the source and provide access without the website really being up.
- We might add support to behave like proxy to random DataSets.

### Document management

Do document preprocessing:
- Create embeddings and everything needed to train the pages.
- Teach everything with proper context tags (i.e. have context "Laegna Math" when teaching Laegna Math).
- Use tools to turn static documents to cards, and recognize cards to be already processed.

### AI model management

Model management:
- Be able to download models, which can be fine-tuned.
- Be able to incorporate fine-tuners, for example additional packages might depend on everything needed (such as Laegna-huggingface).
- Keep models in permanent and safe position, where they are not deleted automatically.
- Create copy of model in purpose of fine-tuning.

### Fine-tuning

Fine-tuning:
- It will be able to fine-tune models based on it's information.

### Exporting fine-tuned models

Export function:
- It's able to export to GGUF.
