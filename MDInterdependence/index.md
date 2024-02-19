# Interdependence between the implementation

Spider and Server, for example, use the parser library from the Client. The purpose is that rather than minimalizing code amount in each single instance, we minimize total code amount and work for synchronization of Laegna Source Servers; we don't also expect that user is necessarily even using this parser, but perhaps they are working with their own Spider, and with Json.

Web based interface, in instance of our case, is the Client to the Server for user, but also for the Spider, which would use it directly otherwise - it also guarantees minimal installation to learn Laegna.
