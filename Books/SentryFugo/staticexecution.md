# Static Execution of Code

Let's provide a set of tools:
- Laegna Math Website with it's standards
- Laegna Math Spider for client-side

We need one proxy layer here:
- In case the developer does not use Flask server, but has their whole site statically in server, or simply in GitHub - in each case of static service, the Spider must be able to run another instance of Server and Client.
- For example, if only Server is made by user, with no _graphical access_, the Spider is able to run client: it lives together with the Client source, and it can start it to connect with the server, which should have simple interface to return it's internal data. The developer might struggle with creation of graphical content.
- For example, if there is no Server and no Client, the Spider could use the filesystem of Documentation, even the Python scripts (after we have added some protection - in my current plan I simply execute them whatever they are, given that over time there will be 20 developer users, we can manage the source somehow; we need experience to really automate it and I want to do this part-by-part: I mean automatic verification that it's not virus or spam generation, and/or execution in virtual machine or restricted environment; rather, initially we can manually read the code - especially, end-user website cannot access the GitHub database destructively, rather it would break one clone, and we won't let in completely stupid code). In this case, I'm interested: how people would implement safe execution of Python, perhaps Julia and Go, in a way which is not running very expensive virtualizations, which would slow down the execution, also how to do it with a few lines of code.

So we need this functionality in Spider:
- Execute the Server itself, also going to past versions of Git. For example, an user might run only the last version, whereas the Server System of user might be able to work with older versions and standards. The user might work with their favourite version, even personal fork, while others are using major versions or latest version.
- For example, run the version of 2 years ago.
- I don't know how to convince the browser or domain service to mock a page:
  - User creates the page, which is meant to be a placeholder of such execution, for example they have a page on their static website, which allows to be used with manual server: the server will get access right, and _for it's own user or clients_, it would generate the content and show it as this page. They could create Proxy service to other users and get accepted as such, so that other spiders would use their content.

Why we need all this?
- You control your environment and what you provide, and you are free of standards: for example, while your system is providing Wikipages to other system, while the critical part follows their API, you have custom functionality, which does not break it.
- Things we want to do: for example running expensive AI model on your page might be *extremely* needy in terms of resources; instead, other people run it in *their* systems and allow your users see it on your site or with direct connection.
  - As each user is creating as much content as much they have resources, for example leaving their most expensive content, especially given they would need to serve it, statically there.
  - Let's say one of my books will run an expensive process over database entered by an user. It knows several free and payd services to do this, but each of them needs specific registered user with an API key.
  - I don't also want to manage database of 5000 users: I would lose the data somehow, for example the cheap service I use suddenly stops working.
  - My user database is handled by some user management system, which also knows these users specifically, whereas other types of users are handled by other systems; for example it's an American system able to verify passport of Americans, but not Indians.
  - An user will plug into some of my pages, developing an advanced AI, which would generate content and embeddings for my dynamic content, for example providing it as a context to other lessons. They would even not have a server, but their Spider would be able to generate dynamic content and upload to their static server. At there, standard-compliant AI data would reside.

This standard is like Markdown: it builds on something we can already do. We can do these things, share AI models, and we can also automate them: for example, we need standards to serve pages of others, but then we would be extremely load-balanced, like a cloud service.