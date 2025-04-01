# GitHub

Manually:
- We use it to backup our code
- We use it to register our versions and version our files, much like History function of Wikipedia

Automatically:
- We use it for Spiders to crawl older versions and run them locally, to serve older-version links
- We use it to rely on right versions of data when we refer to AI training history
- We use it to keep track of ID's of our files and their versions
- We also use it to compare differences between versions

Our client service should access versions and support different ways for navigating through versions, for example registering some permanent copys of specific versions and having a proxy for them; it should redirect and allow the running model, while with source, it would create a source tree and invoke a server on it before it can study it properly: website needs to provide Git link for that operation.

For these purposes and other, we should have proxy abilities for all our services:
- The Spider should be able to be Proxy layer for those addresses, taking care of everything what is omitted online; the Spider has full server code to create local access: it should be able, also, to run the services in your selected cloud service, by uploading the Server code and creating a client, which would access it and serve outside. The server should connect to permanent site, still able to share it's own content. We can have separate Spiders for separate services, as small service is easier to create and update - it should be rather API compability and functional standard layer, while no system must understand all of ours; for example, the client could use online system and their simple Spider would only manage the links to create working copies of historic states.
