# Story 2

What: Add support for the Slug service when creating a new user
Why: Users are asking for custom usernames rather than the pre-generated values.

Acceptance Criteria:

- Use the preferred_username in the message body to generate a new username.
- The SlugService will need to generate this username
- If the preferred_username is null, then use the existing pre-defined names

---

Comments:

> **From**: Jody Norris (Product Manager)
The backend team has informed me that they now accept pre-created usernames in their request. Add the field "username" to the body with the desired username.

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
    "requestedName": // the passed username
    "finalName": // the username to use
    "changed": bool
}
