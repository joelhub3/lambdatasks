# Story 2

What: Add support for the Slug service when creating a new user
Why: Users are asking for custom usernames rather than the pre-generated values.

The Slug service is responsible for validating a username and providing a close alternative if the requested name is not available. It should only be called if the user provides a username. The backend already has a mechanism to assign a random, unused username. We should use the backend's mechanism if the user has not provided a proposed username.

Acceptance Criteria:

- Use the preferred_username in the message body to create a new username using the Slug Service.
- Use the backend's existing mechanism for username assignment if no preferred_username is provided.

---

Comments:

> **From**: Jody Norris (Product Manager)
The backend team has informed me that they now accept pre-created usernames in their request. Add the field **"username"** to the body with the desired username.

---

> **From**: Prashob Kruthiventi (Lead Deveoper, Slug service)
The slug service uses a rest api. you can use:

POST https://localhost:9001/new-slug
Authorization: 1234  (we don't have a proper secret yet -- this will work while we sort out the proper secret)

{
    "proposedUsername": // username
}

The response is:

{
    "proposedUsername": // the passed username
    "finalName": // the username to use
    "changed": bool
}
